"""JPEG rendering and text-layer reads via PyMuPDF."""

from __future__ import annotations

import logging
from pathlib import Path

import fitz  # PyMuPDF

from .config import LOGGER_NAME, Settings

log = logging.getLogger(LOGGER_NAME)


def pad_width(page_count: int) -> int:
    """Zero-pad width for page-NN labels; minimum 2 for tidy short docs."""
    return max(2, len(str(page_count)))


def page_label(page_number: int, width: int) -> str:
    """1-based page number -> 'page-07'."""
    return "page-%0*d" % (width, page_number)


def get_text_layer(page: "fitz.Page") -> str:
    """Raw text-layer content of a page (empty for image-only pages)."""
    return page.get_text("text") or ""


def jpeg_bytes(page: "fitz.Page", zoom: float, quality: int = 85) -> bytes:
    """Render a page to JPEG bytes in memory (used by the vlm markdown backend to
    feed the model without depending on the on-disk render phase)."""
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    return pix.tobytes(output="jpeg", jpg_quality=quality)


def _save_jpeg(page: "fitz.Page", zoom: float, out_path: Path, quality: int) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(jpeg_bytes(page, zoom, quality))


def render_small(page: "fitz.Page", out_path: Path, settings: Settings) -> None:
    """Render a ~small_width-wide preview JPEG."""
    width = max(1.0, page.rect.width)
    zoom = settings.small_width / width
    _save_jpeg(page, zoom, out_path, settings.jpeg_quality)
    log.debug("Rendered small jpeg %s (zoom=%.3f)", out_path, zoom)


def render_big(page: "fitz.Page", out_path: Path, settings: Settings) -> None:
    """Render a full-resolution JPEG at big_dpi."""
    zoom = settings.big_dpi / 72.0
    _save_jpeg(page, zoom, out_path, settings.jpeg_quality)
    log.debug("Rendered big jpeg %s (zoom=%.3f)", out_path, zoom)
