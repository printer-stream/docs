"""Per-page extraction quality metrics and the confidence gate.

The gate's job is to catch extraction *failures* - gibberish OCR, dropped
content, garbled output - so a human reviews only those. It must NOT punish
pages that are legitimately low-prose (command/parameter tables, hex listings),
which are the most important pages in this corpus.

Design notes (calibrated against the real corpus):
- "Coverage" (md content volume vs the raw text layer) is the primary
  dropped-content signal. It is order-insensitive, so Docling reflowing a table
  does not look like a failure - only actually losing content does.
- Sequence-order "agreement" is kept as an informational metric only; it is not
  scored, because table reflow tanks it even when extraction is perfect.
- Command/hex/table density marks a page as content-rich; such pages are trusted
  unless coverage shows a real drop.
- A page with no markdown AND no text layer is a genuine blank (or image-only),
  not a failure; it is tagged, not flagged. Image-only pages are the target of
  the optional describe (VLM) phase, not the review queue.
"""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass, field
from typing import Dict, Optional

# ESC/POS and common control mnemonics; HPGL pen/plot commands.
_COMMAND_TOKENS = re.compile(
    r"\b(ESC|GS|FS|DLE|DC[1-4]|HT|LF|CR|FF|CAN|NUL|SOH|STX|ETX|EOT|ENQ|ACK|BEL)\b"
)
_HPGL_TOKENS = re.compile(r"\b(PU|PD|PA|PR|SP|VS|LT|SC|IP|DF|IN)\b")
_HEX_BYTES = re.compile(r"\b[0-9A-Fa-f]{2}[Hh]?\b")
_WORD = re.compile(r"[A-Za-z]{2,}")
_VOWEL = re.compile(r"[aeiouy]")
_NORMALIZE = re.compile(r"[^a-z0-9]+")

# A page is "content-rich" (and trusted) if it clears any of these.
_MIN_COMMANDS = 3
_MIN_TABLE_ROWS = 3
_MIN_HEX = 5
# Below this fraction of the text layer's content volume, suspect a real drop.
_LOW_COVERAGE = 0.5
_EMPTY_ALNUM = 10
_TEXT_COMPARE_MIN = 40


@dataclass
class PageQuality:
    char_count: int
    alnum_ratio: float
    wordlike_ratio: float
    table_rows: int
    command_hits: int
    hpgl_hits: int
    hex_hits: int
    coverage: Optional[float]
    textlayer_agreement: Optional[float]
    content_rich: bool
    empty: bool
    score: float
    flagged: bool
    reasons: list = field(default_factory=list)


def _normalize(text: str) -> str:
    return _NORMALIZE.sub(" ", text.lower()).strip()


def _alnum_count(text: str) -> int:
    return sum(1 for c in text if c.isalnum())


def assess_page(markdown: str, text_layer: str, threshold: float) -> PageQuality:
    md = markdown.strip()
    char_count = len(md)
    md_alnum = _alnum_count(md)
    alnum_ratio = md_alnum / char_count if char_count else 0.0

    tokens = _WORD.findall(md)
    wordlike = [t for t in tokens if _VOWEL.search(t.lower())]
    wordlike_ratio = (len(wordlike) / len(tokens)) if tokens else 0.0

    table_rows = sum(1 for line in md.splitlines() if line.lstrip().startswith("|"))
    command_hits = len(_COMMAND_TOKENS.findall(md))
    hpgl_hits = len(_HPGL_TOKENS.findall(md))
    hex_hits = len(_HEX_BYTES.findall(md))

    text_alnum = _alnum_count(text_layer)
    coverage: Optional[float] = None
    if text_alnum >= _TEXT_COMPARE_MIN:
        coverage = min(1.0, md_alnum / text_alnum)
    # Informational only (not scored): order-sensitive similarity.
    norm_text = _normalize(text_layer)
    agreement: Optional[float] = None
    if len(norm_text) >= _TEXT_COMPARE_MIN:
        agreement = difflib.SequenceMatcher(None, norm_text, _normalize(md)).ratio()

    content_rich = (
        (command_hits + hpgl_hits) >= _MIN_COMMANDS
        or table_rows >= _MIN_TABLE_ROWS
        or hex_hits >= _MIN_HEX
    )

    reasons: list = []
    empty = False

    if md_alnum < _EMPTY_ALNUM:
        if text_alnum < _EMPTY_ALNUM:
            # Genuine blank or image-only page: nothing to extract from text.
            empty = True
            score = 1.0
        else:
            # Text layer had content but markdown is empty -> real drop.
            score = 0.0
            reasons.append("markdown empty but text layer has %d chars" % text_alnum)
    elif content_rich:
        # Command/parameter/hex page: trust unless coverage shows a real drop.
        if coverage is not None and coverage < _LOW_COVERAGE:
            score = 0.4 + 0.4 * coverage
            reasons.append("content-rich but low coverage (%.2f)" % coverage)
        else:
            score = 0.85
    else:
        # Prose page: judge by word-likeness and content volume.
        if coverage is not None:
            score = 0.5 * wordlike_ratio + 0.5 * coverage
        else:
            score = wordlike_ratio
        if wordlike_ratio < 0.6:
            reasons.append("low word-likeness (%.2f)" % wordlike_ratio)
        if coverage is not None and coverage < 0.6:
            reasons.append("low coverage vs text layer (%.2f)" % coverage)

    flagged = (not empty) and score < threshold
    return PageQuality(
        char_count=char_count,
        alnum_ratio=round(alnum_ratio, 4),
        wordlike_ratio=round(wordlike_ratio, 4),
        table_rows=table_rows,
        command_hits=command_hits,
        hpgl_hits=hpgl_hits,
        hex_hits=hex_hits,
        coverage=round(coverage, 4) if coverage is not None else None,
        textlayer_agreement=round(agreement, 4) if agreement is not None else None,
        content_rich=content_rich,
        empty=empty,
        score=round(score, 4),
        flagged=flagged,
        reasons=reasons,
    )


def to_dict(q: PageQuality) -> Dict:
    return {
        "char_count": q.char_count,
        "alnum_ratio": q.alnum_ratio,
        "wordlike_ratio": q.wordlike_ratio,
        "table_rows": q.table_rows,
        "command_hits": q.command_hits,
        "hpgl_hits": q.hpgl_hits,
        "hex_hits": q.hex_hits,
        "coverage": q.coverage,
        "textlayer_agreement": q.textlayer_agreement,
        "content_rich": q.content_rich,
        "empty": q.empty,
        "score": q.score,
        "flagged": q.flagged,
        "reasons": q.reasons,
    }
