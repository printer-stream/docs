"""Query helpers shared by the eval harness and (later) the MCP server.

FTS5 MATCH treats characters like ( ) " * as query syntax, so raw user input
such as "GS ( k" is a syntax error. fts_query() turns arbitrary user text into a
safe phrase query. Two backends are exposed: ranked full-text (unicode61 + BM25)
and substring recall (trigram).
"""

from __future__ import annotations

import sqlite3
from typing import List, Optional

# Trigram MATCH needs at least one full trigram (3 chars) to match anything.
TRIGRAM_MIN = 3


def fts_query(text: str) -> str:
    """Turn arbitrary user text into a safe FTS5 phrase query."""
    return '"' + text.replace('"', '""') + '"'


def _rows(con: sqlite3.Connection, sql: str, params) -> List[dict]:
    con.row_factory = sqlite3.Row
    return [dict(r) for r in con.execute(sql, params).fetchall()]


def search_fulltext(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    """Ranked full-text search (unicode61 tokenizer, BM25 ordering)."""
    where = "pages_fts MATCH ?"
    params: list = [fts_query(query)]
    if vendor:
        where += " AND p.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT p.stem, p.vendor, p.doc, p.page, p.label, p.heading_path, "
        "       snippet(pages_fts, 0, '[', ']', ' ... ', 12) AS snippet, "
        "       bm25(pages_fts) AS rank "
        "FROM pages_fts JOIN pages p ON p.id = pages_fts.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, params)


def search_trigram(
    con: sqlite3.Connection, query: str, k: int = 10, vendor: Optional[str] = None
) -> List[dict]:
    """Substring/symbol recall via the trigram index."""
    if len(query.strip()) < TRIGRAM_MIN:
        return []
    where = "pages_trgm MATCH ?"
    params: list = [fts_query(query)]
    if vendor:
        where += " AND p.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT p.stem, p.vendor, p.doc, p.page, p.label, p.heading_path, "
        "       bm25(pages_trgm) AS rank "
        "FROM pages_trgm JOIN pages p ON p.id = pages_trgm.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, params)


def search_documents(con: sqlite3.Connection, query: str, k: int = 10) -> List[dict]:
    """Search document titles/summaries (for summary-style lookups)."""
    sql = (
        "SELECT d.stem, d.vendor, d.doc, d.title, d.languages, d.summary, "
        "       bm25(documents_fts) AS rank "
        "FROM documents_fts JOIN documents d ON d.id = documents_fts.rowid "
        "WHERE documents_fts MATCH ? ORDER BY rank LIMIT ?"
    )
    return _rows(con, sql, [fts_query(query), k])
