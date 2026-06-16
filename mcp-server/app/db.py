"""Read-only access to the baked SQLite FTS5 index.

Mirrors the indexer's query contract: user text is always turned into a safe FTS5
phrase (raw input like 'GS ( k' is a MATCH syntax error). Ranked full-text plus a
trigram recall net, so command/symbol queries are found and nothing is missed.
"""

from __future__ import annotations

import contextlib
import logging
import sqlite3
from typing import Dict, List, Optional

from .config import APP_NAME, settings

log = logging.getLogger(APP_NAME)

TRIGRAM_MIN = 3

_PAGE_COLS = (
    "p.stem, p.vendor, p.doc, p.page, p.label, p.heading_path, "
    "p.jpeg_small, p.jpeg_big, p.markdown"
)


def fts_query(text: str) -> str:
    """Turn arbitrary user text into a safe FTS5 phrase query."""
    return '"' + text.replace('"', '""') + '"'


def _connect() -> sqlite3.Connection:
    con = sqlite3.connect("file:%s?mode=ro" % settings.db_path, uri=True, check_same_thread=False)
    con.row_factory = sqlite3.Row
    return con


@contextlib.contextmanager
def connection():
    con = _connect()
    try:
        yield con
    finally:
        con.close()


def _clamp_k(k: int) -> int:
    try:
        k = int(k)
    except (TypeError, ValueError):
        k = settings.search_k
    return max(1, min(k, settings.search_max_k))


def list_documents() -> List[Dict]:
    with connection() as c:
        rows = c.execute(
            "SELECT stem, vendor, doc, title, page_count, languages "
            "FROM documents ORDER BY vendor, doc"
        ).fetchall()
    return [dict(r) for r in rows]


def get_document(stem: str) -> Optional[Dict]:
    with connection() as c:
        r = c.execute(
            "SELECT stem, vendor, doc, title, page_count, languages, summary, source_pdf "
            "FROM documents WHERE stem = ?",
            (stem,),
        ).fetchone()
    return dict(r) if r else None


def search_fulltext(con, query: str, vendor: Optional[str], k: int) -> List[Dict]:
    where = "pages_fts MATCH ?"
    params: list = [fts_query(query)]
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
    return [dict(r) for r in con.execute(sql, params).fetchall()]


def search_trigram(con, query: str, vendor: Optional[str], k: int) -> List[Dict]:
    if len(query.strip()) < TRIGRAM_MIN:
        return []
    where = "pages_trgm MATCH ?"
    params: list = [fts_query(query)]
    if vendor:
        where += " AND p.vendor = ?"
        params.append(vendor)
    params.append(k)
    sql = (
        "SELECT " + _PAGE_COLS + ", '' AS snippet, bm25(pages_trgm) AS rank "
        "FROM pages_trgm JOIN pages p ON p.id = pages_trgm.rowid "
        "WHERE " + where + " ORDER BY rank LIMIT ?"
    )
    return [dict(r) for r in con.execute(sql, params).fetchall()]


def search_pages(con, query: str, vendor: Optional[str], k: int) -> List[Dict]:
    """Ranked full-text, topped up with trigram recall to fill k."""
    k = _clamp_k(k)
    hits = search_fulltext(con, query, vendor, k)
    seen = {(h["stem"], h["page"]) for h in hits}
    if len(hits) < k:
        for r in search_trigram(con, query, vendor, k):
            key = (r["stem"], r["page"])
            if key not in seen:
                hits.append(r)
                seen.add(key)
            if len(hits) >= k:
                break
    return hits[:k]


def neighbor_pages(con, stem: str, lo: int, hi: int) -> List[Dict]:
    rows = con.execute(
        "SELECT page, label, jpeg_small, jpeg_big FROM pages "
        "WHERE stem = ? AND page BETWEEN ? AND ? ORDER BY page",
        (stem, lo, hi),
    ).fetchall()
    return [dict(r) for r in rows]


def get_page(stem: str, page: int) -> Optional[Dict]:
    with connection() as c:
        r = c.execute(
            "SELECT stem, vendor, doc, page, label, heading_path, body, "
            "jpeg_small, jpeg_big, markdown, source, flagged "
            "FROM pages WHERE stem = ? AND page = ?",
            (stem, page),
        ).fetchone()
    return dict(r) if r else None
