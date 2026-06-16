"""Extractive, no-LLM document summaries.

Builds a short "what this document covers" blurb from the document's own text:
the vendor, a title, detected command languages, and the most prominent section
headings. ASCII only.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import List, Tuple

_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")

# Each language: a label and a set of marker patterns. A language is reported
# when its markers are reasonably dense in the document text.
_LANG_MARKERS = [
    ("ESC/POS", re.compile(r"\b(ESC/POS|ESC\s*@|GS\s*\(|FS\s)\b"), 3),
    # Real HP-GL signals: explicit name, pen up/down/abs/rel, or numbered pens
    # (SP1..). Avoids matching bare "SP"/"PA" etc. that occur in ESC/POS prose.
    ("HPGL", re.compile(r"\bHP-?GL\b|\b(?:PU|PD|PA|PR)\b|\bSP\d\b"), 5),
    ("Star Line Mode", re.compile(r"\bline\s*mode\b", re.I), 2),
    ("ESC/P", re.compile(r"\bESC/P\b"), 1),
]


def extract_headings(text: str) -> List[str]:
    out = []
    for line in text.splitlines():
        m = _HEADING.match(line.strip())
        if m:
            title = m.group(1).strip()
            if title:
                out.append(title)
    return out


def detect_languages(text: str) -> List[str]:
    found = []
    for label, pattern, min_hits in _LANG_MARKERS:
        if len(pattern.findall(text)) >= min_hits:
            found.append(label)
    return found


def pick_title(headings: List[str], doc: str) -> str:
    for h in headings:
        # Skip bare page markers / the auto-added doc-name heading.
        if h.lower() != doc.lower() and len(h) > 2:
            return h
    return doc


def top_headings(headings: List[str], limit: int = 8) -> List[str]:
    counts = Counter(h for h in headings if 2 < len(h) <= 80)
    return [h for h, _ in counts.most_common(limit)]


def make_summary(vendor: str, doc: str, page_count: int, full_text: str) -> Tuple[str, str, str]:
    """Return (title, languages_csv, summary_text)."""
    headings = extract_headings(full_text)
    title = pick_title(headings, doc)
    languages = detect_languages(full_text)
    tops = top_headings(headings)

    parts = ["%s %s." % (vendor, title), "%d pages." % page_count]
    if languages:
        parts.append("Command sets: %s." % ", ".join(languages))
    if tops:
        parts.append("Sections: %s." % "; ".join(tops))
    summary = " ".join(parts)
    return title, ", ".join(languages), summary
