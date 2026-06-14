"""MCP server exposing search over the printer-spec corpus.

Transport: Streamable HTTP (remote-hostable, e.g. on Render).
Tools:
  list_documents()                  -> all docs with vendor/title/page count
  get_document_summary(stem)        -> what devices/technologies a doc covers
  search_specs(query, vendor?, k?)  -> hybrid (FTS5 + vector) ranked results,
                                       each with page number + JPEG image paths
  get_page(stem, page)              -> full page Markdown + image paths

Logging: thorough ASCII-only logs on every step. The slow part of startup is
loading the sentence-transformers embedding model (downloaded on first run,
then cached); it is preloaded eagerly with progress logs so a cold start is
easy to follow. Set DOCS_LOG_LEVEL=DEBUG for per-query detail.
"""
from __future__ import annotations

import logging
import os
import sqlite3
import struct
import time

import sqlite_vec
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

from corpus import INDEX_PATH

EMBED_MODEL = os.environ.get("DOCS_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
RRF_K = 60  # reciprocal-rank-fusion constant

logging.basicConfig(
    level=os.environ.get("DOCS_LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)-7s [%(name)s] %(message)s",
)
log = logging.getLogger("printer-stream-docs")

# Quiet noisy third-party loggers so our own step-by-step logs stay readable.
# Set DOCS_VERBOSE_DEPS=1 to see the underlying HF/httpx download chatter.
if not os.environ.get("DOCS_VERBOSE_DEPS"):
    for noisy in ("httpx", "httpcore", "sentence_transformers",
                  "transformers", "urllib3", "filelock"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

mcp = FastMCP(
    "printer-stream-docs",
    host=os.environ.get("HOST", "0.0.0.0"),
    port=int(os.environ.get("PORT", "8000")),
)

_db: sqlite3.Connection | None = None
_model: SentenceTransformer | None = None


def db() -> sqlite3.Connection:
    """Open (once) a read-only connection to the committed index."""
    global _db
    if _db is None:
        log.info("Opening index database: %s", INDEX_PATH)
        if not INDEX_PATH.exists():
            log.error("Index not found at %s -- run mcp-server/indexer.py first", INDEX_PATH)
            raise FileNotFoundError(
                f"Index not found at {INDEX_PATH}. Run mcp-server/indexer.py first."
            )
        size_kb = INDEX_PATH.stat().st_size // 1024
        log.info("Index file size: %d KB", size_kb)
        t0 = time.perf_counter()
        conn = sqlite3.connect(
            f"file:{INDEX_PATH}?mode=ro",
            uri=True,
            check_same_thread=False
        )
        conn.row_factory = sqlite3.Row
        log.info("Loading sqlite-vec extension...")
        # conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        # conn.enable_load_extension(False)
        ndocs = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        nchunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        log.info(
            "Index ready in %.2fs: %d document(s), %d chunk(s)",
            time.perf_counter() - t0, ndocs, nchunks,
        )
        _db = conn
    return _db


def model() -> SentenceTransformer:
    """Load (once) the embedding model. This is the slow part of a cold start."""
    global _model
    if _model is None:
        log.info("Loading embedding model '%s' (first run downloads + caches it; "
                 "this can take a while)...", EMBED_MODEL)
        t0 = time.perf_counter()
        _model = SentenceTransformer(EMBED_MODEL)
        try:
            dim = _model.get_embedding_dimension()
        except AttributeError:  # older sentence-transformers
            dim = _model.get_sentence_embedding_dimension()
        log.info("Embedding model loaded in %.2fs (dim=%d)",
                 time.perf_counter() - t0, dim)
    return _model


def warm_up() -> None:
    """Eagerly initialize the slow resources so the first query is fast and
    the startup cost is visible in the logs."""
    log.info("Warm-up starting: index + embedding model")
    t0 = time.perf_counter()
    db()
    model()
    # Run one trivial encode so lazy backend init happens now, not on first query.
    log.info("Running a warm-up embedding...")
    model().encode(["warm up"], normalize_embeddings=True)
    log.info("Warm-up complete in %.2fs -- server ready to serve queries",
             time.perf_counter() - t0)


def _serialize(vec) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


@mcp.tool()
def list_documents() -> list[dict]:
    """List every available document with its vendor, title, and page count."""
    log.info("tool list_documents()")
    t0 = time.perf_counter()
    rows = db().execute(
        "SELECT stem, vendor, title, page_count FROM documents ORDER BY stem"
    ).fetchall()
    log.info("list_documents -> %d doc(s) in %.3fs", len(rows), time.perf_counter() - t0)
    return [dict(r) for r in rows]


@mcp.tool()
def get_document_summary(stem: str) -> dict:
    """Return the summary of what devices/technologies a document covers."""
    log.info("tool get_document_summary(stem=%r)", stem)
    row = db().execute(
        "SELECT stem, vendor, title, summary, page_count FROM documents WHERE stem = ?",
        (stem,),
    ).fetchone()
    if row is None:
        log.warning("get_document_summary: no document with stem %r", stem)
        return {"error": f"No document with stem '{stem}'."}
    log.info("get_document_summary -> %r (%d pages)", row["title"], row["page_count"])
    return dict(row)


@mcp.tool()
def search_specs(query: str, vendor: str | None = None, k: int = 8) -> list[dict]:
    """Search the corpus for a query and return ranked page-level results.

    Hybrid retrieval: FTS5 keyword search (exact command tokens / hex codes)
    fused with semantic vector search (conceptual questions) via Reciprocal
    Rank Fusion. Each result includes the document, page number, a text
    snippet, and the small/big JPEG image paths for that page.
    """
    log.info("tool search_specs(query=%r, vendor=%r, k=%d)", query, vendor, k)
    t0 = time.perf_counter()
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
        log.debug("FTS5 matched %d chunk(s)", len(fts_ranks))
    except sqlite3.OperationalError as exc:
        log.debug("FTS5 query rejected (%s); relying on vector search", exc)

    # Semantic ranks (vector KNN).
    t_emb = time.perf_counter()
    emb = model().encode([query], normalize_embeddings=True)[0]
    log.debug("Query embedded in %.3fs", time.perf_counter() - t_emb)
    vec_rows = conn.execute(
        "SELECT rowid FROM vec_chunks WHERE embedding MATCH ? "
        "ORDER BY distance LIMIT ?",
        (_serialize(emb), pool),
    ).fetchall()
    vec_ranks = {r["rowid"]: rank for rank, r in enumerate(vec_rows)}
    log.debug("Vector search matched %d chunk(s)", len(vec_ranks))

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
    log.info(
        "search_specs -> %d result(s) in %.3fs (fts=%d, vec=%d, fused=%d)",
        len(results), time.perf_counter() - t0,
        len(fts_ranks), len(vec_ranks), len(scores),
    )
    return results


@mcp.tool()
def get_page(stem: str, page: int) -> dict:
    """Return the full Markdown text and image paths for a specific page."""
    log.info("tool get_page(stem=%r, page=%d)", stem, page)
    row = db().execute(
        "SELECT stem, vendor, page_no, text, image_small, image_big "
        "FROM chunks WHERE stem = ? AND page_no = ? AND kind = 'body'",
        (stem, page),
    ).fetchone()
    if row is None:
        log.warning("get_page: no page %d in document %r", page, stem)
        return {"error": f"No page {page} in document '{stem}'."}
    log.info("get_page -> %s page %d (%d chars)", stem, page, len(row["text"]))
    return dict(row)


if __name__ == "__main__":
    log.info("=== printer-stream-docs MCP server starting ===")
    log.info("Embedding model : %s", EMBED_MODEL)
    log.info("Index path      : %s", INDEX_PATH)
    log.info("Bind address    : %s:%s", os.environ.get("HOST", "0.0.0.0"), os.environ.get("PORT", "8000"))
    log.info("Transport       : streamable-http (endpoint /mcp)")
    warm_up()
    log.info("Starting HTTP transport; press Ctrl-C to stop")
    mcp.run(transport="streamable-http")
