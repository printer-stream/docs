"""Docling-based per-page Markdown conversion.

Pages are converted one at a time (each split into a temporary single-page PDF)
so the per-page markdown maps 1:1 onto the page renders. The Docling converter
(and its loaded models) is built once and reused across pages.
"""

from __future__ import annotations

import logging
import tempfile
from pathlib import Path

import fitz  # PyMuPDF

from .config import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)


class DoclingPageConverter:
    """Wraps a Docling DocumentConverter for single-page conversion."""

    def __init__(self, do_ocr: bool = True) -> None:
        # Imported lazily so the rest of the package (and unit tests) do not
        # require the heavy Docling/torch stack just to import.
        from docling.document_converter import DocumentConverter, PdfFormatOption
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions

        opts = PdfPipelineOptions()
        opts.do_ocr = do_ocr
        opts.do_table_structure = True

        # Prefer the Tesseract CLI backend (light, no torch) over the EasyOCR
        # default. Fall back to whatever Docling ships if the option is absent.
        if do_ocr:
            try:
                from docling.datamodel.pipeline_options import TesseractCliOcrOptions

                opts.ocr_options = TesseractCliOcrOptions()
                log.info("OCR backend: tesseract CLI")
            except Exception:
                log.warning("TesseractCliOcrOptions unavailable; using Docling default OCR")

        self._converter = DocumentConverter(
            format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
        )
        log.info("Docling converter ready (do_ocr=%s)", do_ocr)

    def convert_page(self, doc: "fitz.Document", page_index: int) -> str:
        """Return the Markdown for a single 0-based page of an open PDF."""
        with tempfile.TemporaryDirectory() as tmp:
            single = Path(tmp) / ("page-%d.pdf" % (page_index + 1))
            out = fitz.open()
            try:
                out.insert_pdf(doc, from_page=page_index, to_page=page_index)
                out.save(str(single))
            finally:
                out.close()

            result = self._converter.convert(str(single))
            markdown = result.document.export_to_markdown()
            log.debug("Converted page %d -> %d chars markdown", page_index + 1, len(markdown))
            return markdown
