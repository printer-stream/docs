"""Registered backends and gates. Each strategy is one factory; selecting it is a
profile setting. Add a strategy = add a factory + @register; remove = delete it.

Implemented now (step 1): markdown 'docling', quality 'heuristic', describe gates
'all'/'flagged'/'illustrated'. VLM markdown/quality-judge and section backends
register in later steps; selecting an unregistered name fails with a clear error.
Heavy imports (docling, providers) are lazy so this module imports cheaply.
"""

from __future__ import annotations

import json
import logging
from typing import List

from .config import LOGGER_NAME
from .registry import Registry

log = logging.getLogger(LOGGER_NAME)

MARKDOWN = Registry("markdown backend")
QUALITY = Registry("quality backend")
SECTIONS = Registry("sections backend")
GATES = Registry("describe gate")


# --- markdown backends -----------------------------------------------------
class _DoclingMarkdown:
    name = "docling"

    def __init__(self, settings, cfg) -> None:
        from .convert import DoclingPageConverter  # lazy: heavy (docling/torch)

        self.model = None
        self._conv = DoclingPageConverter(do_ocr=bool(cfg.get("do_ocr", True)))

    def page(self, doc, page_index: int) -> str:
        return self._conv.convert_page(doc, page_index)


@MARKDOWN.register("docling")
def _make_docling(settings, cfg):
    return _DoclingMarkdown(settings, cfg)


class _VlmMarkdown:
    """Transcribe a page image to Markdown via an OpenAI-compatible VLM. Renders
    the page in memory (no dependency on the on-disk render phase)."""

    name = "vlm"

    def __init__(self, settings, cfg) -> None:
        from . import providers  # lazy

        self._client = providers.client_from(cfg.get("provider"))
        self.model = self._client.model
        # dpi for the model's input image; defaults to the profile's big render dpi.
        self._dpi = int(cfg.get("dpi", settings.big_dpi))
        self._quality = int(settings.jpeg_quality)

    def page(self, doc, page_index: int) -> str:
        from .render import jpeg_bytes  # lazy (pulls fitz)
        from .prompts import MARKDOWN_PROMPT

        img = jpeg_bytes(doc[page_index], self._dpi / 72.0, self._quality)
        return self._client.vision(MARKDOWN_PROMPT, img)


@MARKDOWN.register("vlm")
def _make_vlm_markdown(settings, cfg):
    return _VlmMarkdown(settings, cfg)


# --- quality backends ------------------------------------------------------
class _HeuristicQuality:
    name = "heuristic"
    model = None

    def __init__(self, settings, cfg) -> None:
        self._threshold = float(cfg.get("threshold", 0.5))

    def assess(self, markdown: str, text: str):
        from . import quality as quality_mod  # lazy (stdlib, but keep symmetric)

        return quality_mod.assess_page(markdown, text, self._threshold)


@QUALITY.register("heuristic")
def _make_heuristic(settings, cfg):
    return _HeuristicQuality(settings, cfg)


# --- describe gates --------------------------------------------------------
def _flagged_labels(settings, stem: str) -> set:
    q_path = settings.quality_json_path(stem)
    if not q_path.exists():
        log.warning("describe gate: no quality json for %s; run the quality phase first", stem)
        return set()
    data = json.loads(q_path.read_text(encoding="utf-8"))
    return {lb for lb, p in data.get("pages", {}).items() if p.get("flagged") or p.get("empty")}


@GATES.register("all")
def _gate_all(settings, stem: str, labels: List[str]) -> List[str]:
    return list(labels)


@GATES.register("flagged")
def _gate_flagged(settings, stem: str, labels: List[str]) -> List[str]:
    flagged = _flagged_labels(settings, stem)
    return [lb for lb in labels if lb in flagged]


@GATES.register("illustrated")
def _gate_illustrated(settings, stem: str, labels: List[str]) -> List[str]:
    flagged = _flagged_labels(settings, stem)
    md_dir = settings.doc_markdown_dir(stem)
    selected = set(flagged)
    for lb in labels:
        md_path = md_dir / (lb + ".md")
        if md_path.exists() and "<!-- image -->" in md_path.read_text(encoding="utf-8"):
            selected.add(lb)
    return [lb for lb in labels if lb in selected]
