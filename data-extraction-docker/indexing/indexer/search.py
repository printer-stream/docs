"""Query helpers shared by the eval harness and mirrored by the MCP server.

User text must never reach FTS5 MATCH raw - characters like ( ) " * are query
syntax (e.g. "GS ( k" is a syntax error). Two strategies are combined:

  - fts_and(): AND of quoted per-word terms -> documents containing ALL terms.
    This is the ranked keyword search; a multi-word query matches documents that
    contain every term, not only the exact phrase (the old behaviour, which made
    most multi-word queries return nothing).
  - fts_phrase(): the whole text as one quoted phrase -> exact substring match,
    used by the trigram index for symbol/command sequences ("GS ( k", "1B 40").

search_pages() / search_sections() combine them: ranked AND, an OR top-up for
recall, then the trigram net. Sections are the primary retrieval unit (a logical
chunk that may span pages); pages remain a fallback. The MCP server mirrors both.
"""

from __future__ import annotations

import sqlite3
from typing import List, Optional

# Trigram MATCH needs at least one full trigram (3 chars) to match anything.
TRIGRAM_MIN = 3

_PAGE_COLS = "p.stem, p.vendor, p.doc, p.page, p.label, p.heading_path"
_SECTION_COLS = (
    "s.stem, s.vendor, s.doc, s.section_no, s.title, s.heading_path, s.level, "
    "s.page_start, s.page_end, s.page_labels"
)


def fts_phrase(text: str) -> str:
    """Whole text as one quoted FTS5 phrase (exact substring for trigram)."""
    return '"' + text.replace('"', '""') + '"'


def _terms(text: str) -> List[str]:
    """Quoted per-word terms, dropping tokens with no alphanumeric content
    (a bare '(' tokenizes to an empty phrase, which is a MATCH syntax error)."""
    terms: List[str] = []
    for raw in text.split():
        if any(ch.isalnum() for ch in raw):
            terms.append('"' + raw.replace('"', '""') + '"')
    return terms


def fts_and(text: str) -> str:
    """AND of terms (FTS5 implicit operator between phrases is AND)."""
    return " ".join(_terms(text))


def fts_or(text: str) -> str:
    return " OR ".join(_terms(text))


def _rows(con: sqlite3.Connection, sql: str, params) -> List[dict]:
    con.row_factory = sqlite3.Row
    return [dict(r) for r in con.execute(sql, params).fetchall()]


def _fts_pages(con: sqlite3.Connection, match_expr: str, k: int, vendor: Optional[str]) -> List[dict]:
    where = "pages_fts MATCH ?"
    params: list = [match_expr]
    if vendor:
        where += " AND p.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT " + _PAGE_COLS + ", "
        "snippet(pages_fts, 0, '[', ']', ' ... ', 12) AS snippet, "
        "bm25(pages_fts) AS rank "
        "FROM pages_fts JOIN pages p ON p.id = pages_fts.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, params)


def search_fulltext(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    """Ranked full-text search: AND of the query's terms (BM25 ordering)."""
    match = fts_and(query)
    return _fts_pages(con, match, k, vendor) if match else []


def search_trigram(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    """Substring/symbol recall via the trigram index (exact phrase substring)."""
    if len(query.strip()) < TRIGRAM_MIN:
        return []
    where = "pages_trgm MATCH ?"
    params: list = [fts_phrase(query)]
    if vendor:
        where += " AND p.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT " + _PAGE_COLS + ", '' AS snippet, bm25(pages_trgm) AS rank "
        "FROM pages_trgm JOIN pages p ON p.id = pages_trgm.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, params)


def search_pages(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    """Canonical search: ranked AND, OR top-up for recall, then trigram net."""
    terms = _terms(query)
    hits = _fts_pages(con, " ".join(terms), k, vendor) if terms else []
    seen = {(h["stem"], h["page"]) for h in hits}

    def _add(rows: List[dict]) -> None:
        for r in rows:
            key = (r["stem"], r["page"])
            if key not in seen:
                hits.append(r)
                seen.add(key)
            if len(hits) >= k:
                break

    if len(hits) < k and len(terms) > 1:
        _add(_fts_pages(con, " OR ".join(terms), k, vendor))
    if len(hits) < k:
        _add(search_trigram(con, query, k, vendor))
    return hits[:k]


# --- sections (primary retrieval unit) -------------------------------------
# Mirrors the page path. sections_fts columns are (title, heading_path, body);
# bm25 weights rank a title/heading match above a body match. Dedup key is
# (stem, section_no).
def _fts_sections(con: sqlite3.Connection, match_expr: str, k: int, vendor: Optional[str]) -> List[dict]:
    where = "sections_fts MATCH ?"
    params: list = [match_expr]
    if vendor:
        where += " AND s.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT " + _SECTION_COLS + ", "
        "snippet(sections_fts, 2, '[', ']', ' ... ', 16) AS snippet, "
        "bm25(sections_fts, 5.0, 3.0, 1.0) AS rank "
        "FROM sections_fts JOIN sections s ON s.id = sections_fts.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, params)


def search_sections_trigram(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    if len(query.strip()) < TRIGRAM_MIN:
        return []
    where = "sections_trgm MATCH ?"
    params: list = [fts_phrase(query)]
    if vendor:
        where += " AND s.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT " + _SECTION_COLS + ", '' AS snippet, bm25(sections_trgm) AS rank "
        "FROM sections_trgm JOIN sections s ON s.id = sections_trgm.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, params)


def search_sections(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    """Canonical section search: ranked AND, OR top-up for recall, then trigram."""
    terms = _terms(query)
    hits = _fts_sections(con, " ".join(terms), k, vendor) if terms else []
    seen = {(h["stem"], h["section_no"]) for h in hits}

    def _add(rows: List[dict]) -> None:
        for r in rows:
            key = (r["stem"], r["section_no"])
            if key not in seen:
                hits.append(r)
                seen.add(key)
            if len(hits) >= k:
                break

    if len(hits) < k and len(terms) > 1:
        _add(_fts_sections(con, " OR ".join(terms), k, vendor))
    if len(hits) < k:
        _add(search_sections_trigram(con, query, k, vendor))
    return hits[:k]


def search_documents(con: sqlite3.Connection, query: str, k: int = 10) -> List[dict]:
    """Search document titles/summaries (AND of terms)."""
    match = fts_and(query) or fts_phrase(query)
    sql = (
        "SELECT d.stem, d.vendor, d.doc, d.title, d.languages, d.summary, "
        "       bm25(documents_fts) AS rank "
        "FROM documents_fts JOIN documents d ON d.id = documents_fts.rowid "
        "WHERE documents_fts MATCH ? ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, [match, k])
