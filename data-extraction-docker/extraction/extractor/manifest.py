"""Discover source PDFs and split them into shards for parallel CI runners."""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

import fitz  # PyMuPDF

from .config import LOGGER_NAME, Settings

log = logging.getLogger(LOGGER_NAME)


@dataclass
class DocInfo:
    stem: str          # vendor-rooted, e.g. star/star_graphic_cm_en
    source_pdf: str    # repo-relative, e.g. pdf/star/star_graphic_cm_en.pdf
    page_count: int


def discover_docs(settings: Settings) -> List[DocInfo]:
    """Find every pdf/<vendor>/<doc>.pdf and read its page count."""
    docs: List[DocInfo] = []
    for pdf_path in sorted(settings.pdf_dir.rglob("*.pdf")):
        rel = pdf_path.relative_to(settings.root).as_posix()
        stem = pdf_path.relative_to(settings.pdf_dir).with_suffix("").as_posix()
        try:
            with fitz.open(pdf_path) as doc:
                page_count = doc.page_count
        except Exception:
            log.exception("Failed to open %s; skipping", rel)
            continue
        docs.append(DocInfo(stem=stem, source_pdf=rel, page_count=page_count))
        log.debug("Discovered %s (%d pages)", stem, page_count)
    log.info("Discovered %d source PDFs under %s", len(docs), settings.pdf_dir)
    return docs


def select_shard(docs: List[DocInfo], shard_index: int, shard_count: int) -> List[DocInfo]:
    """Round-robin assignment over the sorted doc list for even-ish balance."""
    if shard_count <= 1:
        return docs
    if not 0 <= shard_index < shard_count:
        raise ValueError(
            "shard_index %d out of range for shard_count %d" % (shard_index, shard_count)
        )
    subset = [d for i, d in enumerate(docs) if i % shard_count == shard_index]
    log.info(
        "Shard %d/%d selected %d of %d docs", shard_index, shard_count, len(subset), len(docs)
    )
    return subset


def write_manifest(docs: List[DocInfo], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(d) for d in docs]
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    log.info("Wrote manifest with %d docs to %s", len(docs), path)
