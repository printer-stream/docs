"""Command-line entrypoint. One subcommand per phase.

  manifest   discover PDFs, emit a doc manifest as JSON (for the CI matrix)
  render     pdf  -> jpeg/<stem>/{small,big}/page-NN.jpg
  text       pdf  -> text/<stem>/page-NN.txt
  markdown   pdf  -> markdown/<stem>/page-NN.md      (Docling; the slow phase)
  quality    md+text -> quality/<stem>.json
  assemble   all  -> pagemap/<stem>.json + document.md + reports
  run        render+text+markdown+quality+assemble, in order
  report     aggregate per-doc QA -> quality/report.html

Each phase processes whole documents (all-or-none) and writes meta/<stem>/<phase>.json.
Scope is chosen with --all, --stem, or --shard-index/--shard-count.

Logging goes to stderr; only the manifest JSON is written to stdout.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Callable, List

from . import manifest as manifest_mod
from . import phases as phases_mod
from . import report as report_mod
from .config import LOGGER_NAME, Settings, setup_logging
from .version import __version__

log = logging.getLogger(LOGGER_NAME)

# Phases that need the (expensive) Docling converter built once before the loop.
_NEEDS_CONVERTER = {"markdown", "run"}


def _add_scope(p: argparse.ArgumentParser) -> None:
    sel = p.add_mutually_exclusive_group(required=True)
    sel.add_argument("--all", action="store_true", help="Every discovered doc")
    sel.add_argument("--stem", help="One doc, e.g. star/star_graphic_cm_en")
    sel.add_argument("--shard-index", type=int, help="This shard's index (with --shard-count)")
    p.add_argument("--shard-count", type=int, help="Total number of shards")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="extractor", description="PDF extraction pipeline")
    p.add_argument("--root", default=".", help="Repo root containing pdf/ and data-extraction/")
    p.add_argument("--log-level", default="INFO", help="DEBUG, INFO, WARNING, ERROR")
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="command", required=True)

    m = sub.add_parser("manifest", help="Discover PDFs and emit a doc manifest as JSON")
    m.add_argument("--out", default=None, help="Write JSON here (default: stdout)")

    for phase in ("render", "text", "markdown", "quality", "assemble", "run"):
        sp = sub.add_parser(phase, help="Phase: %s" % phase)
        _add_scope(sp)
        if phase in ("markdown", "run"):
            sp.add_argument("--no-ocr", action="store_true", help="Disable OCR in Docling")
        if phase in ("quality", "run"):
            sp.add_argument(
                "--quality-threshold", type=float, default=None, help="Flag pages below this"
            )

    # describe: optional VLM phase. Endpoint/model/key default from the
    # environment so secrets are not passed on the command line.
    dp = sub.add_parser("describe", help="Phase: VLM page descriptions (gated to flagged pages)")
    _add_scope(dp)
    dp.add_argument("--describe-base-url", default=os.environ.get("DESCRIBE_BASE_URL"),
                    help="OpenAI-compatible base URL, e.g. http://localhost:8000/v1")
    dp.add_argument("--describe-model", default=os.environ.get("DESCRIBE_MODEL"),
                    help="Model id, e.g. Qwen/Qwen2.5-VL-7B-Instruct or gpt-4o-mini")
    dp.add_argument("--describe-api-key", default=os.environ.get("DESCRIBE_API_KEY", ""),
                    help="API key (default from DESCRIBE_API_KEY)")
    dp.add_argument("--describe-image", choices=["small", "big"], default="big",
                    help="Which render to send to the VLM")
    dp.add_argument("--all-pages", action="store_true",
                    help="Describe every page (default: only quality-flagged pages)")

    sub.add_parser("report", help="Aggregate per-doc QA into quality/report.html")
    return p


def _resolve_docs(settings: Settings, args: argparse.Namespace) -> List[manifest_mod.DocInfo]:
    if args.stem:
        src = settings.pdf_dir / (args.stem + ".pdf")
        if not src.exists():
            raise SystemExit("source PDF not found: %s" % src)
        import fitz

        with fitz.open(src) as d:
            return [manifest_mod.DocInfo(args.stem, settings.rel_source_pdf(args.stem), d.page_count)]

    docs = manifest_mod.discover_docs(settings)
    if args.shard_index is not None:
        if args.shard_count is None:
            raise SystemExit("--shard-index requires --shard-count")
        return manifest_mod.select_shard(docs, args.shard_index, args.shard_count)
    return docs  # --all


def _cmd_manifest(settings: Settings, args: argparse.Namespace) -> int:
    docs = manifest_mod.discover_docs(settings)
    if args.out:
        manifest_mod.write_manifest(docs, Path(args.out))
    else:
        sys.stdout.write(json.dumps([asdict(d) for d in docs], indent=2, ensure_ascii=True) + "\n")
    return 0


def _run_phase(settings: Settings, args: argparse.Namespace, phase: str) -> int:
    if getattr(args, "no_ocr", False):
        settings.do_ocr = False
    if getattr(args, "quality_threshold", None) is not None:
        settings.quality_threshold = args.quality_threshold

    docs = _resolve_docs(settings, args)
    if not docs:
        log.warning("No documents selected; nothing to do")
        return 0

    converter = None
    if phase in _NEEDS_CONVERTER:
        from .convert import DoclingPageConverter

        converter = DoclingPageConverter(do_ocr=settings.do_ocr)

    client = None
    if phase == "describe":
        if not args.describe_base_url or not args.describe_model:
            raise SystemExit(
                "describe requires --describe-base-url and --describe-model "
                "(or DESCRIBE_BASE_URL / DESCRIBE_MODEL)"
            )
        settings.describe_image = args.describe_image
        from .describe import DescribeClient

        client = DescribeClient(
            base_url=args.describe_base_url,
            model=args.describe_model,
            api_key=args.describe_api_key or "",
        )

    fn: Callable[[str], object]
    if phase == "render":
        fn = lambda stem: phases_mod.render_doc(settings, stem)
    elif phase == "text":
        fn = lambda stem: phases_mod.text_doc(settings, stem)
    elif phase == "markdown":
        fn = lambda stem: phases_mod.markdown_doc(settings, converter, stem)
    elif phase == "quality":
        fn = lambda stem: phases_mod.quality_doc(settings, stem)
    elif phase == "describe":
        fn = lambda stem: phases_mod.describe_doc(settings, client, stem, all_pages=args.all_pages)
    elif phase == "assemble":
        fn = lambda stem: phases_mod.assemble_doc(settings, stem)
    elif phase == "run":
        fn = lambda stem: phases_mod.run_doc(settings, converter, stem)
    else:
        raise SystemExit("unknown phase: %s" % phase)

    failures = 0
    for doc in docs:
        try:
            log.info("Phase %s starting on %s", phase, doc.stem)
            fn(doc.stem)
        except Exception:
            failures += 1
            log.exception("Phase %s failed on %s", phase, doc.stem)

    # Phases that change QA refresh the corpus-level report for convenience.
    if phase in ("quality", "assemble", "run"):
        report_mod.write_corpus_report(settings)

    log.info("Phase %s done: %d docs, %d failures", phase, len(docs), failures)
    return 1 if failures else 0


def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    setup_logging(args.log_level)
    log.info("extractor %s starting: command=%s root=%s", __version__, args.command, args.root)
    settings = Settings(root=Path(args.root))

    if args.command == "manifest":
        return _cmd_manifest(settings, args)
    if args.command == "report":
        report_mod.write_corpus_report(settings)
        return 0
    return _run_phase(settings, args, args.command)


if __name__ == "__main__":
    sys.exit(main())
