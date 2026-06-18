"""Command-line entrypoint: build | evaluate | manifest.

  build      pagemaps + markdown -> data-extraction/index/<type>/specs.db (+ manifest)
  evaluate   run the query set against the built index, report recall@k
  manifest   (re)write the index manifest from the existing db

Logging goes to stderr.
"""

from __future__ import annotations

import argparse
import logging
import sqlite3
import sys
from pathlib import Path
from typing import List

from . import build as build_mod
from . import evaluate as eval_mod
from . import manifest as manifest_mod
from .config import LOGGER_NAME, Settings, setup_logging
from .version import __version__

log = logging.getLogger(LOGGER_NAME)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="indexer", description="Build the search index")
    p.add_argument("--root", default=".", help="Repo root containing data-extraction/")
    p.add_argument("--index-type", default="fulltext", help="Subdir under data-extraction/index/")
    p.add_argument("--log-level", default="INFO")
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="command", required=True)

    b = sub.add_parser("build", help="Build the index and write the manifest")
    b.add_argument("--no-eval", action="store_true", help="Skip the post-build eval")

    e = sub.add_parser("evaluate", help="Run the eval query set against the built index")
    e.add_argument("--queries", default=None, help="Path to queries.json")
    e.add_argument("--k", type=int, default=10)
    e.add_argument("--unit", default="section", choices=["section", "page"],
                   help="Retrieval unit to evaluate (default: section)")
    e.add_argument("--min-recall", type=float, default=None, help="Exit non-zero below this")

    sub.add_parser("manifest", help="Rewrite the manifest from the existing db")
    return p


def _cmd_build(settings: Settings, args: argparse.Namespace) -> int:
    settings.db_path.parent.mkdir(parents=True, exist_ok=True)
    if settings.db_path.exists():
        settings.db_path.unlink()  # clean rebuild; "all or none"
    con = sqlite3.connect(str(settings.db_path))
    try:
        stats = build_mod.build_index(con, settings)
    finally:
        con.close()
    manifest_mod.write_manifest(settings, stats)

    if not args.no_eval:
        qp = eval_mod.default_queries_path()
        if qp.exists():
            eval_mod.run_eval(settings, qp, k=10)
        else:
            log.warning("No eval queries at %s; skipping post-build eval", qp)
    return 0


def _cmd_evaluate(settings: Settings, args: argparse.Namespace) -> int:
    if not settings.db_path.exists():
        raise SystemExit("index not found: %s (run build first)" % settings.db_path)
    qp = Path(args.queries) if args.queries else eval_mod.default_queries_path()
    metrics = eval_mod.run_eval(settings, qp, k=args.k, unit=args.unit)
    if args.min_recall is not None and metrics["recall_at_k"] < args.min_recall:
        log.error("recall@%d %.2f below threshold %.2f", args.k, metrics["recall_at_k"], args.min_recall)
        return 1
    return 0


def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    setup_logging(args.log_level)
    log.info("indexer %s starting: command=%s root=%s", __version__, args.command, args.root)
    settings = Settings(root=Path(args.root), index_type=args.index_type)

    if args.command == "build":
        return _cmd_build(settings, args)
    if args.command == "evaluate":
        return _cmd_evaluate(settings, args)
    if args.command == "manifest":
        if not settings.db_path.exists():
            raise SystemExit("index not found: %s" % settings.db_path)
        con = sqlite3.connect(str(settings.db_path))
        try:
            stats = {
                "doc_count": con.execute("SELECT count(*) FROM documents").fetchone()[0],
                "page_count": con.execute("SELECT count(*) FROM pages").fetchone()[0],
                "section_count": con.execute("SELECT count(*) FROM sections").fetchone()[0],
            }
        finally:
            con.close()
        manifest_mod.write_manifest(settings, stats)
        return 0
    raise SystemExit("unknown command: %s" % args.command)


if __name__ == "__main__":
    sys.exit(main())
