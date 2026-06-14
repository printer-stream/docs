"""MCP server exposing search over the printer-spec corpus.

Transport: Streamable HTTP (remote-hostable, e.g. on Render).
Tools:
  list_documents()                  -> all docs with vendor/title/page count
  get_document_summary(stem)        -> what devices/technologies a doc covers
  search_specs(query, vendor?, k?)  -> hybrid (FTS5 + vector) ranked results,
                                       each with page number + JPEG image paths
  get_page(stem, page)              -> full page Markdown + image paths
"""
from __future__ import annotations

import os
import sqlite3
import struct

import sqlite_vec
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

from corpus import INDEX_PATH

EMBED_MODEL = os.environ.get("DOCS_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
RRF_K = 60  # reciprocal-rank-fusion constant

mcp = FastMCP(
    "printerrr-docs",
    host=os.environ.get("HOST", "0.0.0.0"),
    port=int(os.environ.get("PORT", "8000")),
)

_db: sqlite3.Connection | None = None
_model: SentenceTransformer | None = None


def db() -> sqlite3.Connection:
    global _db
    if _db is None:
        if not INDEX_PATH.exists():
            raise FileNotFoundError(
                f"Index not found at {INDEX_PATH}. Run mcp-server/indexer.py first."
            )
        conn = sqlite3.connect(f"file:{INDEX_PATH}?mode=ro", uri=True, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        conn.enable_load_extension(False)
        _db = conn
    return _db


def model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def _serialize(vec) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


@mcp.tool()
def list_documents() -> list[dict]:
    """List every available document with its vendor, title, and page count."""
    rows = db().execute(
        "SELECT stem, vendor, title, page_count FROM documents ORDER BY stem"
    ).fetchall()
    return [dict(r) for r in rows]


@mcp.tool()
def get_document_summary(stem: str) -> dict:
    """Return the summary of what devices/technologies a document covers."""
    row = db().execute(
        "SELECT stem, vendor, title, summary, page_count FROM documents WHERE stem = ?",
        (stem,),
    ).fetchone()
    if row is None:
        return {"error": f"No document with stem '{stem}'."}
    return dict(row)


@mcp.tool()
def search_specs(query: str, vendor: str | None = None, k: int = 8) -> list[dict]:
    """Search the corpus for a query and return ranked page-level results.

    Hybrid retrieval: FTS5 keyword search (exact command tokens / hex codes)
    fused with semantic vector search (conceptual questions) via Reciprocal
    Rank Fusion. Each result includes the document, page number, a text
    snippet, and the small/big JPEG image paths for that page.
    """
    conn = db()
    pool = max(k * 5, 30)

    # Keyword ranks (FTS5).
    fts_ranks: dict[int, int] = {}
    try:
        fts_rows = conn.execute(
            "SELECT rowid FROM fts_chunks WHERE fts_chunks MATCH ? "
            "ORDER BY rank LIMIT ?",
            (query, pool),
        ).fetchall()
        for rank, r in enumerate(fts_rows):
            fts_ranks[r["rowid"]] = rank
    except sqlite3.OperationalError:
        pass  # malformed FTS query -> rely on vector search

    # Semantic ranks (vector KNN).
    emb = model().encode([query], normalize_embeddings=True)[0]
    vec_rows = conn.execute(
        "SELECT rowid FROM vec_chunks WHERE embedding MATCH ? "
        "ORDER BY distance LIMIT ?",
        (_serialize(emb), pool),
    ).fetchall()
    vec_ranks = {r["rowid"]: rank for rank, r in enumerate(vec_rows)}

    # Reciprocal Rank Fusion.
    scores: dict[int, float] = {}
    for ranks in (fts_ranks, vec_ranks):
        for cid, rank in ranks.items():
            scores[cid] = scores.get(cid, 0.0) + 1.0 / (RRF_K + rank)

    ranked = sorted(scores, key=scores.get, reverse=True)

    results: list[dict] = []
    seen: set[tuple] = set()
    for cid in ranked:
        row = conn.execute(
            "SELECT stem, vendor, page_no, kind, text, image_small, image_big "
            "FROM chunks WHERE id = ?",
            (cid,),
        ).fetchone()
        if row is None or (vendor and row["vendor"] != vendor):
            continue
        key = (row["stem"], row["page_no"])
        if key in seen:
            continue
        seen.add(key)
        text = row["text"]
        results.append(
            {
                "stem": row["stem"],
                "vendor": row["vendor"],
                "page": row["page_no"],
                "score": round(scores[cid], 5),
                "snippet": text[:600] + ("..." if len(text) > 600 else ""),
                "image_small": row["image_small"],
                "image_big": row["image_big"],
            }
        )
        if len(results) >= k:
            break
    return results


@mcp.tool()
def get_page(stem: str, page: int) -> dict:
    """Return the full Markdown text and image paths for a specific page."""
    row = db().execute(
        "SELECT stem, vendor, page_no, text, image_small, image_big "
        "FROM chunks WHERE stem = ? AND page_no = ? AND kind = 'body'",
        (stem, page),
    ).fetchone()
    if row is None:
        return {"error": f"No page {page} in document '{stem}'."}
    return dict(row)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
