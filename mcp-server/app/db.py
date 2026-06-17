"""Read-only access to the baked SQLite FTS5 index.

Mirrors the indexer's query contract: user text is always turned into a safe FTS5
phrase (raw input like 'GS ( k' is a MATCH syntax error). Ranked full-text plus a
trigram recall net, so command/symbol queries are found and nothing is missed.
"""

from __future__ import annotations

import contextlib
import json
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


def index_meta() -> Dict:
    """Index build metadata (created_at, indexer_version, counts). Empty if the
    baked index predates the index_meta table."""
    with connection() as c:
        try:
            rows = c.execute("SELECT key, value FROM index_meta").fetchall()
        except sqlite3.OperationalError:
            return {}
    return {r["key"]: r["value"] for r in rows}


def list_documents() -> List[Dict]:
    """Documents plus extraction lineage (source pdf, extracted_at, extractor
    version, per-phase timing). Falls back to the basic columns for an older
    index that lacks the lineage fields."""
    enriched = (
        "SELECT stem, vendor, doc, title, page_count, languages, source_pdf, "
        "extracted_at, pipeline_version, phases FROM documents ORDER BY vendor, doc"
    )
    basic = (
        "SELECT stem, vendor, doc, title, page_count, languages "
        "FROM documents ORDER BY vendor, doc"
    )
    with connection() as c:
        try:
            rows = c.execute(enriched).fetchall()
        except sqlite3.OperationalError:
            rows = c.execute(basic).fetchall()
    out: List[Dict] = []
    for r in rows:
        d = dict(r)
        if d.get("phases"):
            try:
                d["phases"] = json.loads(d["phases"])
            except (TypeError, json.JSONDecodeError):
                pass
        out.append(d)
    return out


def get_document(stem: str) -> Optional[Dict]:
    with connection() as c:
        r = c.execute(
            "SELECT stem, vendor, doc, title, page_count, languages, summary, source_pdf "
            "FROM documents WHERE stem = ?",
            (stem,),
        ).fetchone()
    return dict(r) if r else None


def _fts_pages(con, match_expr: str, vendor: Optional[str], k: int) -> List[Dict]:
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
    return [dict(r) for r in con.execute(sql, params).fetchall()]


def search_trigram(con, query: str, vendor: Optional[str], k: int) -> List[Dict]:
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
    return [dict(r) for r in con.execute(sql, params).fetchall()]


def search_pages(con, query: str, vendor: Optional[str], k: int) -> List[Dict]:
    """Canonical search: ranked AND of terms, OR top-up for recall, then trigram.

    A multi-word query matches documents containing all terms (not only the exact
    phrase); OR and trigram fill remaining slots so symbol/command sequences and
    looser matches are not missed.
    """
    k = _clamp_k(k)
    terms = _terms(query)
    hits = _fts_pages(con, " ".join(terms), vendor, k) if terms else []
    seen = {(h["stem"], h["page"]) for h in hits}

    def _add(rows: List[Dict]) -> None:
        for r in rows:
            key = (r["stem"], r["page"])
            if key not in seen:
                hits.append(r)
                seen.add(key)
            if len(hits) >= k:
                break

    if len(hits) < k and len(terms) > 1:
        _add(_fts_pages(con, " OR ".join(terms), vendor, k))
    if len(hits) < k:
        _add(search_trigram(con, query, vendor, k))
    return hits[:k]


def get_page_assets(stem: str, page: int) -> Optional[Dict]:
    """Just the render paths for a page (for get_page_image), no body."""
    with connection() as c:
        r = c.execute(
            "SELECT label, jpeg_small, jpeg_big FROM pages WHERE stem = ? AND page = ?",
            (stem, page),
        ).fetchone()
    return dict(r) if r else None


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
