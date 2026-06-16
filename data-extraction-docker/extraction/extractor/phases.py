"""Discrete extraction phases.

Each phase processes one whole document (all pages, all-or-none), writes a single
kind of artifact, and records timing + metadata. Phases are independent and
re-runnable: re-run a phase to regenerate its artifact kind without touching the
others. The assemble phase consumes every prior artifact + meta and produces the
authoritative pagemap, the bulk markdown, and the review reports.

Phase order: render -> text -> markdown -> quality -> [describe] -> assemble.
(describe is optional and gated on the quality phase's flagged/empty pages.)
"""

from __future__ import annotations

import json
import logging
from importlib.metadata import PackageNotFoundError, version as pkg_version
from typing import Dict, List, Optional, Tuple

import fitz  # PyMuPDF

from . import quality as quality_mod
from . import report as report_mod
from .config import LOGGER_NAME, Settings
from .convert import DoclingPageConverter
from .describe import DescribeClient
from .meta import PhaseRecorder, read_meta, utcnow, write_meta
from .render import get_text_layer, page_label, pad_width, render_big, render_small
from .version import __version__

log = logging.getLogger(LOGGER_NAME)

# Phases that assemble folds into the pagemap lineage, in execution order.
# describe is gated on the quality phase's output, so it runs after quality.
PRIOR_PHASES = ["render", "text", "markdown", "quality", "describe"]


class Progress:
    """Running page counter across all documents in a phase run, so per-page
    logs read 'page 100/9000' rather than just 'page 100'."""

    def __init__(self, total: int) -> None:
        self.total = total
        self.done = 0

    def advance(self) -> int:
        self.done += 1
        return self.done


def _pkg_version(name: str) -> str:
    try:
        return pkg_version(name)
    except PackageNotFoundError:
        return "unknown"


def _open(settings: Settings, stem: str) -> Tuple["fitz.Document", int, int]:
    src = settings.pdf_dir / (stem + ".pdf")
    if not src.exists():
        raise FileNotFoundError("source PDF not found: %s" % src)
    doc = fitz.open(src)
    page_count = doc.page_count
    return doc, page_count, pad_width(page_count)


def _log_page(phase, stem, label, n, page_count, progress, extra=""):
    """Per-page progress. With a corpus Progress, shows the running count across
    all docs (page 100/9000); otherwise the per-doc count (page 100/377)."""
    if progress is not None:
        done, total = progress.advance(), progress.total
    else:
        done, total = n, page_count
    msg = "  %s %s %s  page %d/%d" % (phase, stem, label, done, total)
    log.info(msg + (" " + extra if extra else ""))


# --- phase: render ---------------------------------------------------------
def render_doc(settings: Settings, stem: str, progress: Optional["Progress"] = None) -> Dict:
    doc, page_count, width = _open(settings, stem)
    rec = PhaseRecorder(
        "render", "pymupdf", _pkg_version("pymupdf"),
        params={
            "small_width": settings.small_width,
            "big_dpi": settings.big_dpi,
            "jpeg_quality": settings.jpeg_quality,
        },
    )
    try:
        for n in range(page_count):
            label = page_label(n + 1, width)
            page = doc[n]
            with rec.time_page(label):
                render_small(page, settings.doc_jpeg_dir(stem) / "small" / (label + ".jpg"), settings)
                render_big(page, settings.doc_jpeg_dir(stem) / "big" / (label + ".jpg"), settings)
            _log_page("render", stem, label, n + 1, page_count, progress)
        meta = rec.to_dict(stem, page_count)
    finally:
        doc.close()
    write_meta(settings, stem, "render", meta)
    return meta


# --- phase: text -----------------------------------------------------------
def text_doc(settings: Settings, stem: str) -> Dict:
    doc, page_count, width = _open(settings, stem)
    rec = PhaseRecorder("text", "pymupdf", _pkg_version("pymupdf"), params={})
    out_dir = settings.doc_text_dir(stem)
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        for n in range(page_count):
            label = page_label(n + 1, width)
            with rec.time_page(label):
                text = get_text_layer(doc[n])
                (out_dir / (label + ".txt")).write_text(text, encoding="utf-8")
        meta = rec.to_dict(stem, page_count)
    finally:
        doc.close()
    write_meta(settings, stem, "text", meta)
    return meta


# --- phase: markdown (Docling, the expensive one) --------------------------
def markdown_doc(
    settings: Settings, converter: DoclingPageConverter, stem: str,
    progress: Optional["Progress"] = None,
) -> Dict:
    doc, page_count, width = _open(settings, stem)
    rec = PhaseRecorder(
        "markdown", "docling", _pkg_version("docling"),
        params={"do_ocr": settings.do_ocr},
    )
    out_dir = settings.doc_markdown_dir(stem)
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        for n in range(page_count):
            label = page_label(n + 1, width)
            with rec.time_page(label):
                markdown = converter.convert_page(doc, n)
            (out_dir / (label + ".md")).write_text(markdown.rstrip() + "\n", encoding="utf-8")
            _log_page("markdown", stem, label, n + 1, page_count, progress, "(%d chars)" % len(markdown))
        meta = rec.to_dict(stem, page_count)
    finally:
        doc.close()
    write_meta(settings, stem, "markdown", meta)
    return meta


# --- phase: quality --------------------------------------------------------
def quality_doc(settings: Settings, stem: str) -> Dict:
    doc, page_count, width = _open(settings, stem)
    doc.close()  # only needed page_count/width here; inputs come from artifacts
    rec = PhaseRecorder(
        "quality", "builtin", __version__,
        params={"threshold": settings.quality_threshold},
    )
    md_dir = settings.doc_markdown_dir(stem)
    text_dir = settings.doc_text_dir(stem)

    quality_pages: Dict[str, Dict] = {}
    flagged_count = 0
    for n in range(1, page_count + 1):
        label = page_label(n, width)
        md_path = md_dir / (label + ".md")
        txt_path = text_dir / (label + ".txt")
        markdown = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
        text = txt_path.read_text(encoding="utf-8") if txt_path.exists() else ""

        q = quality_mod.assess_page(markdown, text, settings.quality_threshold)
        source = "text-layer" if len(text.strip()) >= settings.text_layer_min_chars else "ocr"
        if q.flagged:
            flagged_count += 1
        quality_pages[label] = {"source": source, **quality_mod.to_dict(q)}

    quality_doc_payload = {
        "stem": stem,
        "page_count": page_count,
        "flagged_count": flagged_count,
        "threshold": settings.quality_threshold,
        "pages": quality_pages,
    }
    q_out = settings.quality_json_path(stem)
    q_out.parent.mkdir(parents=True, exist_ok=True)
    q_out.write_text(
        json.dumps(quality_doc_payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    meta = rec.to_dict(stem, page_count, extra={"flagged_count": flagged_count})
    write_meta(settings, stem, "quality", meta)
    return meta


# --- phase: describe (optional VLM; gated to flagged + image-only pages) ----
def _describe_targets(settings: Settings, stem: str, width: int, page_count: int, all_pages: bool):
    if all_pages:
        return [page_label(n, width) for n in range(1, page_count + 1)]
    # Default gate: pages the quality phase flagged (figure/low-coverage) plus
    # pages with no extractable text at all ("empty" = blank OR image-only). The
    # latter is essential: a pure image-only page has no text layer, so it is
    # tagged empty rather than flagged, yet it is exactly what needs describing.
    # (Blank pages also match; describing them is cheap and harmless.)
    q_path = settings.quality_json_path(stem)
    if not q_path.exists():
        log.warning("describe: no quality json for %s; run the quality phase first", stem)
        return []
    data = json.loads(q_path.read_text(encoding="utf-8"))
    return [
        label for label, p in data.get("pages", {}).items()
        if p.get("flagged") or p.get("empty")
    ]


def describe_doc(
    settings: Settings, client: DescribeClient, stem: str, all_pages: bool = False
) -> Dict:
    doc, page_count, width = _open(settings, stem)
    doc.close()
    targets = _describe_targets(settings, stem, width, page_count, all_pages)
    rec = PhaseRecorder(
        "describe", "vlm", client.model,
        params={"base_url": client.base_url, "image": settings.describe_image, "all_pages": all_pages},
    )
    out_dir = settings.doc_describe_dir(stem)
    out_dir.mkdir(parents=True, exist_ok=True)
    size = settings.describe_image if settings.describe_image in ("small", "big") else "big"

    described = 0
    failed = 0
    total_targets = len(targets)
    for i, label in enumerate(targets, 1):
        jpeg = settings.doc_jpeg_dir(stem) / size / (label + ".jpg")
        if not jpeg.exists():
            log.warning("describe: missing %s; run the render phase first", jpeg)
            failed += 1
            continue
        try:
            with rec.time_page(label):
                text = client.describe_image(jpeg.read_bytes())
            (out_dir / (label + ".txt")).write_text(text.rstrip() + "\n", encoding="utf-8")
            described += 1
            log.info("  describe %s %s  page %d/%d (%d chars)", stem, label, i, total_targets, len(text))
        except Exception:
            failed += 1
            log.exception("describe failed for %s %s", stem, label)

    meta = rec.to_dict(
        stem, len(targets),
        status="ok" if failed == 0 else "partial",
        extra={"described": described, "failed": failed, "total_pages": page_count},
    )
    write_meta(settings, stem, "describe", meta)
    log.info("describe %s: %d described, %d failed", stem, described, failed)
    return meta


# --- phase: assemble -------------------------------------------------------
def _phase_lineage(settings: Settings, stem: str) -> Dict:
    """Compact per-phase timing/version summary read from each phase's meta."""
    lineage: Dict[str, Dict] = {}
    for phase in PRIOR_PHASES:
        m = read_meta(settings, stem, phase)
        if not m:
            continue
        lineage[phase] = {
            "tool": m.get("tool"),
            "tool_version": m.get("tool_version"),
            "duration_seconds": m.get("duration_seconds"),
            "per_page_seconds_avg": m.get("per_page_seconds_avg"),
            "started_at": m.get("started_at"),
            "ended_at": m.get("ended_at"),
            "params": m.get("params"),
            "status": m.get("status"),
        }
    return lineage


def assemble_doc(settings: Settings, stem: str) -> Dict:
    doc, page_count, width = _open(settings, stem)
    doc.close()
    rec = PhaseRecorder("assemble", "builtin", __version__, params={})
    vendor, _, name = stem.partition("/")
    md_dir = settings.doc_markdown_dir(stem)

    quality_doc_payload = {}
    q_path = settings.quality_json_path(stem)
    if q_path.exists():
        try:
            quality_doc_payload = json.loads(q_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Unreadable quality json %s", q_path)
    quality_pages = quality_doc_payload.get("pages", {})

    page_records: List[Dict] = []
    bulk_parts: List[str] = ["# %s\n" % name]
    flagged_pages: List[Dict] = []

    for n in range(1, page_count + 1):
        label = page_label(n, width)
        md_path = md_dir / (label + ".md")
        markdown = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
        qp = quality_pages.get(label, {})

        record = {
            "page": n,
            "label": label,
            "markdown": settings.rel_markdown(stem, label),
            "text": settings.rel_text(stem, label),
            "jpeg_small": settings.rel_jpeg(stem, "small", label),
            "jpeg_big": settings.rel_jpeg(stem, "big", label),
            "source": qp.get("source", "ocr"),
            "quality_score": qp.get("score"),
            "flagged": bool(qp.get("flagged", False)),
        }
        # Reference the optional VLM description when the describe phase produced one.
        if (settings.doc_describe_dir(stem) / (label + ".txt")).exists():
            record["describe"] = settings.rel_describe(stem, label)
        page_records.append(record)
        bulk_parts.append("\n\n<!-- page %d -->\n\n%s" % (n, markdown.rstrip()))
        if qp.get("flagged"):
            flagged_pages.append(
                {
                    "label": label,
                    "page": n,
                    "score": qp.get("score", 0.0),
                    "reasons": qp.get("reasons", []),
                    "md_abs": str(md_path),
                    "jpeg_abs": str(settings.doc_jpeg_dir(stem) / "small" / (label + ".jpg")),
                }
            )

    (md_dir / "document.md").write_text("".join(bulk_parts).rstrip() + "\n", encoding="utf-8")

    pagemap = {
        "stem": stem,
        "vendor": vendor,
        "doc": name,
        "source_pdf": settings.rel_source_pdf(stem),
        "page_count": page_count,
        "pad_width": width,
        "pipeline_version": __version__,
        "generated_at": utcnow(),
        "phases": _phase_lineage(settings, stem),
        "pages": page_records,
    }
    pm_path = settings.pagemap_path(stem)
    pm_path.parent.mkdir(parents=True, exist_ok=True)
    pm_path.write_text(json.dumps(pagemap, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    report_mod.write_doc_report(settings, stem, flagged_pages)
    meta = rec.to_dict(stem, page_count, extra={"flagged_count": len(flagged_pages)})
    write_meta(settings, stem, "assemble", meta)
    return meta


# --- convenience: all phases for one doc, in order -------------------------
def run_all_phases(
    settings: Settings,
    converter: DoclingPageConverter,
    stem: str,
    render_progress: Optional["Progress"] = None,
    markdown_progress: Optional["Progress"] = None,
) -> Dict:
    # Separate counters per page-logging phase so the corpus running count stays
    # correct across docs without double-counting render and markdown.
    render_doc(settings, stem, progress=render_progress)
    text_doc(settings, stem)
    markdown_doc(settings, converter, stem, progress=markdown_progress)
    quality_doc(settings, stem)
    return assemble_doc(settings, stem)
