"""Settings, path resolution, and logging setup.

All output paths are derived from a single repo root so the image can run
anywhere (locally or in CI) by pointing --root at the mounted repo.
"""

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass, field
from pathlib import Path

LOGGER_NAME = "extractor"


@dataclass
class Settings:
    """Runtime configuration for one extraction run."""

    root: Path
    small_width: int = 1024
    big_dpi: int = 200
    jpeg_quality: int = 85
    do_ocr: bool = True
    # A page whose PDF text layer has fewer characters than this is treated as
    # image-only; its markdown is credited to OCR ("ocr") rather than the text
    # layer ("text-layer") in the pagemap.
    text_layer_min_chars: int = 40
    # Pages scoring below this are flagged for manual review.
    quality_threshold: float = 0.5
    # Which JPEG render the describe phase sends to the VLM ("small" or "big").
    describe_image: str = "big"

    # Repo-relative output roots (kept relative for the pagemap, which records
    # repo-relative paths).
    pdf_root: str = field(default="pdf")
    out_root: str = field(default="data-extraction")

    def __post_init__(self) -> None:
        self.root = Path(self.root).resolve()

    # --- absolute filesystem locations -------------------------------------
    @property
    def pdf_dir(self) -> Path:
        return self.root / self.pdf_root

    @property
    def jpeg_dir(self) -> Path:
        return self.root / self.out_root / "jpeg"

    @property
    def markdown_dir(self) -> Path:
        return self.root / self.out_root / "markdown"

    @property
    def pagemap_dir(self) -> Path:
        return self.root / self.out_root / "pagemap"

    @property
    def quality_dir(self) -> Path:
        return self.root / self.out_root / "quality"

    @property
    def text_dir(self) -> Path:
        return self.root / self.out_root / "text"

    @property
    def describe_dir(self) -> Path:
        return self.root / self.out_root / "describe"

    @property
    def meta_dir(self) -> Path:
        return self.root / self.out_root / "meta"

    def doc_jpeg_dir(self, stem: str) -> Path:
        return self.jpeg_dir / stem

    def doc_markdown_dir(self, stem: str) -> Path:
        return self.markdown_dir / stem

    def doc_text_dir(self, stem: str) -> Path:
        return self.text_dir / stem

    def doc_describe_dir(self, stem: str) -> Path:
        return self.describe_dir / stem

    def meta_path(self, stem: str, phase: str) -> Path:
        return self.meta_dir / stem / f"{phase}.json"

    def pagemap_path(self, stem: str) -> Path:
        return self.pagemap_dir / f"{stem}.json"

    def quality_json_path(self, stem: str) -> Path:
        return self.quality_dir / f"{stem}.json"

    def quality_html_path(self, stem: str) -> Path:
        return self.quality_dir / f"{stem}.html"

    def corpus_report_path(self) -> Path:
        return self.quality_dir / "report.html"

    # --- repo-relative locations (recorded in the pagemap) -----------------
    def rel_source_pdf(self, stem: str) -> str:
        return f"{self.pdf_root}/{stem}.pdf"

    def rel_markdown(self, stem: str, label: str) -> str:
        return f"{self.out_root}/markdown/{stem}/{label}.md"

    def rel_jpeg(self, stem: str, size: str, label: str) -> str:
        return f"{self.out_root}/jpeg/{stem}/{size}/{label}.jpg"

    def rel_text(self, stem: str, label: str) -> str:
        return f"{self.out_root}/text/{stem}/{label}.txt"

    def rel_describe(self, stem: str, label: str) -> str:
        return f"{self.out_root}/describe/{stem}/{label}.txt"


def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configure logging to stderr. No print() anywhere in this package."""
    numeric = getattr(logging, level.upper(), logging.INFO)
    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
    )
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(numeric)
    return logging.getLogger(LOGGER_NAME)
