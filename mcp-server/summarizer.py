"""Document summarisation (extractive, zero-dependency).

A short 'what this document covers' blurb built from the document's title and the
text of its leading pages. It is stored per document and indexed as a 'summary'
chunk so conceptual 'what covers X' queries can retrieve whole documents via
full-text search.

The former local seq2seq/transformers (flan-t5) backend was removed when the
server dropped its embedding stack; see TASK-1-SIMPLIFY.md. An extractive summary
is deterministic, free, and on-topic for this corpus (the leading pages carry the
title/overview that matters here).
"""
from __future__ import annotations

from corpus import Document

# Leading pages carry the title/overview; cap the source for a stable snippet.
_MAX_SOURCE_CHARS = 4000
_MAX_SUMMARY_CHARS = 500


def summarize(doc: Document) -> str:
    """Return a one-paragraph 'what this document covers' blurb."""
    source = "\n".join(p.text for p in doc.pages[:3])[:_MAX_SOURCE_CHARS]
    snippet = " ".join(source.split())[:_MAX_SUMMARY_CHARS]
    return f"{doc.title}. {snippet}"
