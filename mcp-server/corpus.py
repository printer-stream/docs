"""Shared helpers: locate the repo, discover documents, derive image paths.

The repo root is the parent of this `mcp-server/` directory, i.e. the folder
that holds `md/`, `md-bulk/`, and `jpeg/`.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(os.environ.get("DOCS_REPO_ROOT", Path(__file__).resolve().parent.parent))
MD_DIR = REPO_ROOT / "md"
MD_BULK_DIR = REPO_ROOT / "md-bulk"
JPEG_DIR = REPO_ROOT / "jpeg"
INDEX_PATH = Path(os.environ.get("DOCS_INDEX_PATH", REPO_ROOT / "index" / "specs.db"))

_PAGE_RE = re.compile(r"page-(\d+)\.md$")
_HEADING_RE = re.compile(r"^#{1,6}\s+(.*\S)\s*$", re.MULTILINE)


@dataclass
class Page:
    page_no: int
    text: str
    image_small: str  # repo-relative
    image_big: str    # repo-relative


@dataclass
class Document:
    stem: str          # e.g. "star/star_graphic_cm_en"
    vendor: str        # first path component, e.g. "star"
    pages: list[Page] = field(default_factory=list)

    @property
    def title(self) -> str:
        # First non-empty heading or line of page 1, else a humanized stem.
        if self.pages:
            m = _HEADING_RE.search(self.pages[0].text)
            if m:
                return m.group(1).strip()
            for line in self.pages[0].text.splitlines():
                if line.strip():
                    return line.strip()
        return self.stem.split("/")[-1].replace("_", " ")


def headings(text: str) -> list[str]:
    return [m.group(1).strip() for m in _HEADING_RE.finditer(text)]


def discover_documents() -> list[Document]:
    """Find every document under md/ that has page-NN.md slices."""
    docs: dict[str, Document] = {}
    for page_file in sorted(MD_DIR.rglob("page-*.md")):
        m = _PAGE_RE.search(page_file.name)
        if not m:
            continue
        stem = page_file.parent.relative_to(MD_DIR).as_posix()
        page_no = int(m.group(1))
        small = JPEG_DIR / stem / "small" / f"{page_file.stem}.jpg"
        big = JPEG_DIR / stem / "big" / f"{page_file.stem}.jpg"
        doc = docs.setdefault(
            stem, Document(stem=stem, vendor=stem.split("/")[0])
        )
        doc.pages.append(
            Page(
                page_no=page_no,
                text=page_file.read_text(encoding="utf-8"),
                image_small=small.relative_to(REPO_ROOT).as_posix(),
                image_big=big.relative_to(REPO_ROOT).as_posix(),
            )
        )
    for doc in docs.values():
        doc.pages.sort(key=lambda p: p.page_no)
    return [docs[k] for k in sorted(docs)]
