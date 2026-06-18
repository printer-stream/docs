"""Command-line entrypoint. One subcommand per phase.

  manifest   discover PDFs, emit a doc manifest as JSON (for the CI matrix)
  render     pdf  -> jpeg/<stem>/{small,big}/page-NN.jpg
  text       pdf  -> text/<stem>/page-NN.txt
  markdown   pdf  -> markdown/<stem>/page-NN.md      (backend: docling | vlm)
  quality    md+text -> quality/<stem>.json          (backend: heuristic | vlm-judge)
  describe   jpeg -> describe/<stem>/page-NN.txt      (VLM; gate-selected pages)
  assemble   all  -> pagemap/<stem>.json + document.md + reports
  all-phases render+text+markdown+quality+assemble, in order
  report     aggregate per-doc QA -> quality/report.html

Which engine/model each phase uses comes from the selected --profile (a TOML file
under profiles/). Scope is chosen with --all, --stem, or --shard-index/--shard-count.
Logging goes to stderr; only the manifest JSON is written to stdout.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Callable, List

from . import backends as backends_mod
from . import manifest as manifest_mod
from . import phases as phases_mod
from . import providers
from . import report as report_mod
from .config import LOGGER_NAME, Settings, setup_logging
from .profiles import load_profile
from .version import __version__

log = logging.getLogger(LOGGER_NAME)


def _add_scope(p: argparse.ArgumentParser) -> None:
    sel = p.add_mutually_exclusive_group(required=True)
    sel.add_argument("--all", action="store_true", help="Every discovered doc")
    sel.add_argument("--stem", help="One doc, e.g. star/star_graphic_cm_en")
    sel.add_argument("--shard-index", type=int, help="This shard's index (with --shard-count)")
    p.add_argument("--shard-count", type=int, help="Total number of shards")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="extractor", description="PDF extraction pipeline")
    p.add_argument("--root", default=".", help="Repo root containing pdf/ and data-extraction/")
    p.add_argument("--profile", default="default",
                   help="Profile name (profiles/<name>.toml) or path; selects each phase's backend/model")
    p.add_argument("--log-level", default="INFO", help="DEBUG, INFO, WARNING, ERROR")
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="command", required=True)

    m = sub.add_parser("manifest", help="Discover PDFs and emit a doc manifest as JSON")
    m.add_argument("--out", default=None, help="Write JSON here (default: stdout)")

    for phase in ("render", "text", "markdown", "quality", "assemble", "all-phases"):
        help_text = (
            "Run all phases in order (render, text, markdown, quality, assemble)"
            if phase == "all-phases" else "Phase: %s" % phase
        )
        _add_scope(sub.add_parser(phase, help=help_text))

    dp = sub.add_parser("describe", help="Phase: VLM page descriptions (provider + gate from profile)")
    _add_scope(dp)
    dp.add_argument("--gate", default=None,
                    help="Override the profile's describe gate (a registered gate name)")

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


def _make_markdown_backend(settings: Settings):
    cfg = settings.profile.markdown
    return backends_mod.MARKDOWN.get(cfg["backend"])(settings, cfg)


def _make_quality_backend(settings: Settings):
    cfg = settings.profile.quality
    return backends_mod.QUALITY.get(cfg["backend"])(settings, cfg)


def _run_phase(settings: Settings, args: argparse.Namespace, phase: str) -> int:
    docs = _resolve_docs(settings, args)
    if not docs:
        log.warning("No documents selected; nothing to do")
        return 0

    # Corpus-wide running page counters so per-page logs read "page 100/9000".
    total_pages = sum(d.page_count for d in docs)
    render_progress = phases_mod.Progress(total_pages) if phase in ("render", "all-phases") else None
    markdown_progress = phases_mod.Progress(total_pages) if phase in ("markdown", "all-phases") else None

    # Build the model-bearing backends once (loads converters/clients a single time).
    fn: Callable[[str], object]
    if phase == "render":
        fn = lambda stem: phases_mod.render_doc(settings, stem, progress=render_progress)
    elif phase == "text":
        fn = lambda stem: phases_mod.text_doc(settings, stem)
    elif phase == "markdown":
        backend = _make_markdown_backend(settings)
        fn = lambda stem: phases_mod.markdown_doc(settings, backend, stem, progress=markdown_progress)
    elif phase == "quality":
        backend = _make_quality_backend(settings)
        fn = lambda stem: phases_mod.quality_doc(settings, backend, stem)
    elif phase == "describe":
        cfg = settings.profile.describe
        client = providers.client_from(cfg.get("provider"))
        gate = args.gate or cfg.get("gate", "illustrated")
        fn = lambda stem: phases_mod.describe_doc(settings, client, stem, gate=gate)
    elif phase == "assemble":
        fn = lambda stem: phases_mod.assemble_doc(settings, stem)
    elif phase == "all-phases":
        md_backend = _make_markdown_backend(settings)
        q_backend = _make_quality_backend(settings)
        fn = lambda stem: phases_mod.run_all_phases(
            settings, md_backend, q_backend, stem,
            render_progress=render_progress, markdown_progress=markdown_progress,
        )
    else:
        raise SystemExit("unknown phase: %s" % phase)

    n_docs = len(docs)
    failures = 0
    for i, doc in enumerate(docs, 1):
        try:
            log.info(
                "Phase %s starting on %s [doc %d/%d, %d pages, %d total]",
                phase, doc.stem, i, n_docs, doc.page_count, total_pages,
            )
            fn(doc.stem)
        except Exception:
            failures += 1
            log.exception("Phase %s failed on %s", phase, doc.stem)

    # Phases that change QA refresh the corpus-level report for convenience.
    if phase in ("quality", "assemble", "all-phases"):
        report_mod.write_corpus_report(settings)

    log.info("Phase %s done: %d docs, %d failures", phase, len(docs), failures)
    return 1 if failures else 0


def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    setup_logging(args.log_level)
    profile = load_profile(args.profile)
    log.info("extractor %s starting: command=%s profile=%s root=%s",
             __version__, args.command, profile.name, args.root)
    settings = Settings(root=Path(args.root), profile=profile)

    if args.command == "manifest":
        return _cmd_manifest(settings, args)
    if args.command == "report":
        report_mod.write_corpus_report(settings)
        return 0
    return _run_phase(settings, args, args.command)


if __name__ == "__main__":
    sys.exit(main())
