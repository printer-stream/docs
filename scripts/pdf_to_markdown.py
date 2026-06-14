#!/usr/bin/env python3
"""Convert a PDF to Markdown using pymupdf4llm, with an OCR fallback.

Produces two artifacts that stay 1:1 aligned with the JPEG page renders:
  md-bulk/<stem>/README.md   full-document Markdown (one file)
  md/<stem>/page-NN.md       per-page Markdown slices, zero-padded to the
                             width of the total page count (matches page-NN.jpg)

Scanned / image-only PDFs carry no extractable text. When the extracted text
is below a per-page threshold, we run ocrmypdf to add a text layer and
re-extract from the OCR'd copy.

Usage:
  pdf_to_markdown.py <pdf_path> <stem>
    <stem> is the repo-relative path without the .pdf extension,
    e.g. star/star_graphic_cm_en
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf4llm

# Average characters per page below which a PDF is treated as scanned/image-only.
MIN_CHARS_PER_PAGE = 50


def extract(pdf_path: str) -> list[dict]:
    """Return one page-chunk dict per page; each has a Markdown 'text' field."""
    return pymupdf4llm.to_markdown(pdf_path, page_chunks=True)


def text_len(pages: list[dict]) -> int:
    return sum(len(p.get("text", "").strip()) for p in pages)


def looks_scanned(pages: list[dict]) -> bool:
    if not pages:
        return False
    return text_len(pages) / len(pages) < MIN_CHARS_PER_PAGE


def ocr(pdf_path: Path) -> Path | None:
    """Run ocrmypdf to add a text layer. Returns the OCR'd PDF path, or None."""
    out = Path(tempfile.mkdtemp()) / "ocr.pdf"
    try:
        subprocess.run(
            [
                "ocrmypdf",
                "--skip-text",      # keep existing text, OCR only image-only pages
                "--optimize", "0",
                "--quiet",
                str(pdf_path),
                str(out),
            ],
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"OCR fallback unavailable/failed for {pdf_path}: {exc}", file=sys.stderr)
        return None
    return out


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: pdf_to_markdown.py <pdf_path> <stem>")

    pdf_path = Path(sys.argv[1])
    stem = sys.argv[2]

    # page_chunks=True returns one dict per page; each has a 'text' field of Markdown.
    pages = extract(str(pdf_path))
    if looks_scanned(pages):
        print(f"{pdf_path}: little extractable text, attempting OCR...")
        ocr_pdf = ocr(pdf_path)
        if ocr_pdf is not None:
            ocr_pages = extract(str(ocr_pdf))
            if text_len(ocr_pages) > text_len(pages):
                pages = ocr_pages
                print(f"{pdf_path}: using OCR'd text.")

    total = len(pages) or 1
    width = len(str(total))

    bulk_dir = Path("md-bulk") / stem
    page_dir = Path("md") / stem
    bulk_dir.mkdir(parents=True, exist_ok=True)
    page_dir.mkdir(parents=True, exist_ok=True)

    parts = []
    for i, page in enumerate(pages, start=1):
        text = page.get("text", "").strip("\n")
        (page_dir / f"page-{i:0{width}d}.md").write_text(text + "\n", encoding="utf-8")
        parts.append(text)

    (bulk_dir / "README.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Converted {pdf_path} -> {total} page(s)")


if __name__ == "__main__":
    main()
