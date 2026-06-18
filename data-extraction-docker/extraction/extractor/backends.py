"""Registered backends and gates. Each strategy is one factory; selecting it is a
profile setting. Add a strategy = add a factory + @register; remove = delete it.

Implemented: markdown 'docling'/'vlm', quality 'heuristic'/'vlm-judge', sections
'headings'/'llm-text', describe gates 'all'/'flagged'/'illustrated'. The planned
'vlm-window' (page-image sliding-window) sections backend is not yet registered;
selecting an unregistered name fails with a clear error. Heavy imports (docling,
providers) are lazy so this module imports cheaply.
"""

from __future__ import annotations

import json
import logging
import re
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
# A quality backend's assess(markdown, text, get_image) returns a PageQuality.
# `get_image` is a zero-arg callable returning the page's big-render JPEG bytes (or
# None); text-only backends ignore it so no image is read.
class _HeuristicQuality:
    name = "heuristic"
    model = None

    def __init__(self, settings, cfg) -> None:
        self._threshold = float(cfg.get("threshold", 0.5))

    def assess(self, markdown: str, text: str, get_image=None):
        from . import quality as quality_mod  # lazy (stdlib, but keep symmetric)

        return quality_mod.assess_page(markdown, text, self._threshold)


@QUALITY.register("heuristic")
def _make_heuristic(settings, cfg):
    return _HeuristicQuality(settings, cfg)


class _VlmJudgeQuality:
    """Heuristic base, augmented by a VLM faithfulness check on figure pages only.

    The heuristic is blind to figures: a diagram reduced to '<!-- image -->' with
    no text still scores well on coverage. For pages that contain a figure marker,
    this asks the VLM whether the markdown captures the page (image + markdown in,
    'OK' or 'MISSING: ...' out) and, on a miss, flags the page and records why.
    Text-only and figureless pages keep the heuristic verdict (no model call).
    """

    name = "vlm-judge"

    def __init__(self, settings, cfg) -> None:
        from . import providers  # lazy

        self._client = providers.client_from(cfg.get("provider"))
        self.model = self._client.model
        self._threshold = float(cfg.get("threshold", 0.5))

    def assess(self, markdown: str, text: str, get_image=None):
        from . import quality as quality_mod
        from .prompts import JUDGE_PROMPT

        base = quality_mod.assess_page(markdown, text, self._threshold)
        has_figure = ("<!-- image -->" in markdown) or ("<!-- figure" in markdown)
        if not has_figure or get_image is None:
            return base
        img = get_image()
        if not img:
            return base
        try:
            verdict = self._client.vision(
                JUDGE_PROMPT + "\n\nExtracted Markdown:\n" + markdown, img, max_tokens=200
            ).strip()
        except Exception:
            log.exception("vlm-judge: model call failed; keeping heuristic verdict")
            return base
        if verdict and not verdict.upper().startswith("OK"):
            base.flagged = True
            base.score = min(base.score, 0.4)
            base.reasons = list(base.reasons) + ["vlm-judge: " + verdict[:200]]
        return base


@QUALITY.register("vlm-judge")
def _make_vlm_judge(settings, cfg):
    return _VlmJudgeQuality(settings, cfg)


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


# --- sections backends -----------------------------------------------------
# Each receives `pages` = [(page_number, label, markdown_text), ...] in order and
# returns a list of section dicts {title, level, heading_path, text, page_start,
# page_end, page_labels, char_count}. Phase assigns ids.
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def _split_text(text: str, max_chars: int) -> List[str]:
    if max_chars <= 0 or len(text) <= max_chars:
        return [text]
    parts: List[str] = []
    buf: List[str] = []
    size = 0
    for para in text.split("\n\n"):
        if size and size + len(para) > max_chars:
            parts.append("\n\n".join(buf))
            buf, size = [], 0
        buf.append(para)
        size += len(para) + 2
    if buf:
        parts.append("\n\n".join(buf))
    return parts


class _HeadingsSections:
    name = "headings"
    model = None

    def __init__(self, settings, cfg) -> None:
        self._max_chars = int(cfg.get("max_chars", 6000))

    def build(self, pages: List[tuple]) -> List[dict]:
        labels = {num: label for num, label, _ in pages}
        raw: List[tuple] = []  # (meta, text)
        stack: List[tuple] = []  # (level, title)
        cur = None

        def flush():
            nonlocal cur
            if cur is None:
                return
            text = "\n".join(cur["lines"]).strip()
            if text:  # skip heading-only sections; their title lives on in children's heading_path
                raw.append((cur, text))
            cur = None

        for num, _label, md in pages:
            for line in md.splitlines():
                m = _HEADING_RE.match(line)
                if m:
                    flush()
                    level, title = len(m.group(1)), m.group(2).strip()
                    while stack and stack[-1][0] >= level:
                        stack.pop()
                    stack.append((level, title))
                    cur = {"title": title, "level": level,
                           "heading_path": " > ".join(t for _, t in stack),
                           "lines": [], "page_start": num, "page_end": num, "pages": {num}}
                else:
                    if cur is None:  # front matter before the first heading
                        cur = {"title": "(front matter)", "level": 0, "heading_path": "",
                               "lines": [], "page_start": num, "page_end": num, "pages": {num}}
                    cur["lines"].append(line)
                    cur["page_end"] = num
                    cur["pages"].add(num)
        flush()

        out: List[dict] = []
        for meta, text in raw:
            page_labels = [labels[n] for n in sorted(meta["pages"])]
            chunks = _split_text(text, self._max_chars)
            for ci, chunk in enumerate(chunks):
                title = meta["title"] if len(chunks) == 1 else "%s (part %d)" % (meta["title"], ci + 1)
                out.append({
                    "title": title, "level": meta["level"], "heading_path": meta["heading_path"],
                    "text": chunk, "page_start": meta["page_start"], "page_end": meta["page_end"],
                    "page_labels": page_labels, "char_count": len(chunk),
                })
        return out


@SECTIONS.register("headings")
def _make_headings(settings, cfg):
    return _HeadingsSections(settings, cfg)


def _parse_section_starts(raw: str) -> List[dict]:
    s = raw.strip()
    i, j = s.find("["), s.rfind("]")
    if i == -1 or j == -1 or j < i:
        return []
    try:
        data = json.loads(s[i:j + 1])
    except json.JSONDecodeError:
        return []
    return [d for d in data if isinstance(d, dict) and d.get("start_page")]


class _LlmTextSections:
    name = "llm-text"

    def __init__(self, settings, cfg) -> None:
        from . import providers  # lazy

        self._client = providers.client_from(cfg.get("provider"))
        self.model = self._client.model
        self._max_tokens = int((cfg.get("provider") or {}).get("max_tokens", 4096))

    def build(self, pages: List[tuple]) -> List[dict]:
        from .prompts import SECTIONS_PROMPT

        labels = {num: label for num, label, _ in pages}
        nums = [num for num, _, _ in pages]
        doc_md = "\n\n".join("<!-- page %d -->\n%s" % (num, md) for num, _l, md in pages)
        raw = self._client.text_only(SECTIONS_PROMPT + "\n\n" + doc_md, max_tokens=self._max_tokens)
        starts = _parse_section_starts(raw)
        if not starts:
            log.warning("sections llm-text: model returned no parseable starts; empty result")
            return []
        starts.sort(key=lambda d: int(d.get("start_page", nums[0])))

        lo, hi = min(nums), max(nums)
        out: List[dict] = []
        for k, st in enumerate(starts):
            sp = max(lo, min(int(st.get("start_page", lo)), hi))
            ep = (int(starts[k + 1].get("start_page", sp)) - 1) if k + 1 < len(starts) else hi
            ep = max(sp, min(ep, hi))
            text = "\n\n".join(md for num, _l, md in pages if sp <= num <= ep).strip()
            out.append({
                "title": str(st.get("title", "")), "level": int(st.get("level", 1)),
                "heading_path": str(st.get("title", "")), "text": text,
                "page_start": sp, "page_end": ep,
                "page_labels": [labels[n] for n in nums if sp <= n <= ep], "char_count": len(text),
            })
        return out


@SECTIONS.register("llm-text")
def _make_llm_text(settings, cfg):
    return _LlmTextSections(settings, cfg)
