"""MCP server exposing full-text search over the printer-spec corpus.

Transport: Streamable HTTP (remote-hostable, e.g. on Render).
Tools:
  list_documents()                  -> all docs with vendor/title/page count
  get_document_summary(stem)        -> what devices/technologies a doc covers
  search_specs(query, vendor?, k?)  -> FTS5-ranked page results, each with a page
                                       number, snippet, and page-image URLs (plus
                                       the surrounding pages' images)
  get_page(stem, page)              -> full page Markdown + image URLs

Search is pure SQLite FTS5 (keyword + exact command-token / hex lookups). The
former embedding/vector half was removed (see TASK-1-SIMPLIFY.md), so there is no
model to load and startup is fast.

Page images are served as URLs. With DOCS_STATIC_BASE_URL set they point at that
base (e.g. a CDN); otherwise this server serves them itself under /static.

Logging: thorough ASCII-only logs on every step. Set DOCS_LOG_LEVEL=DEBUG for
per-query detail.
"""
from __future__ import annotations

import logging
import re
import sqlite3
import time
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import FileResponse, PlainTextResponse, Response

from version import __version__
from config import cfg

logging.basicConfig(
    level=cfg.log_level.upper(),
    format="%(asctime)s %(levelname)-7s [%(name)s] %(message)s",
)
log = logging.getLogger("printer-stream-docs")

# Quiet noisy third-party loggers so our own step-by-step logs stay readable.
if not cfg.verbose_deps:
    for noisy in ("httpx", "httpcore", "urllib3"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

mcp = FastMCP(
    "printer-stream-docs",
    host=cfg.host,
    port=cfg.port,
)

_db: sqlite3.Connection | None = None

# Directories whose files may be served over /static (page images + Markdown).
_STATIC_ROOTS = [Path(cfg.jpeg_dir).resolve(), Path(cfg.md_dir).resolve()]


def db() -> sqlite3.Connection:
    """Open (once) a read-only connection to the committed index."""
    global _db
    if _db is None:
        log.info("Opening index database: %s", cfg.index_path)
        if not cfg.index_path.exists():
            log.error("Index not found at %s -- run mcp-server/indexer.py first", cfg.index_path)
            raise FileNotFoundError(
                f"Index not found at {cfg.index_path}. Run mcp-server/indexer.py first."
            )
        size_kb = cfg.index_path.stat().st_size // 1024
        log.info("Index file size: %d KB", size_kb)
        t0 = time.perf_counter()
        conn = sqlite3.connect(
            f"file:{cfg.index_path}?mode=ro",
            uri=True,
            check_same_thread=False,
        )
        conn.row_factory = sqlite3.Row
        _verify_index_compatibility(conn)
        ndocs = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        nchunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        log.info(
            "Index ready in %.2fs: %d document(s), %d chunk(s)",
            time.perf_counter() - t0, ndocs, nchunks,
        )
        _db = conn
    return _db


def _verify_index_compatibility(conn: sqlite3.Connection) -> None:
    """Fail fast if the index was built by an older (embedding-era) indexer."""
    try:
        rows = conn.execute("SELECT key, value FROM meta").fetchall()
    except sqlite3.OperationalError as exc:
        raise RuntimeError(
            "Index has no 'meta' table -- it was built by an older indexer. "
            "Rebuild it with mcp-server/indexer.py."
        ) from exc
    meta = {row["key"]: row["value"] for row in rows}
    if "embed_model" in meta or meta.get("search") != "fts5":
        raise RuntimeError(
            "Index was built with the old hybrid (embedding) indexer. "
            "Rebuild it with mcp-server/indexer.py."
        )
    log.info("Index metadata: search=%s schema_version=%s built_at=%s",
             meta.get("search"), meta.get("schema_version"), meta.get("built_at"))


def warm_up() -> None:
    """Eagerly open the index so the first query is fast and startup is visible."""
    log.info("Warm-up starting: opening index")
    t0 = time.perf_counter()
    db()
    log.info("Warm-up complete in %.2fs -- server ready to serve queries",
             time.perf_counter() - t0)


def _image_url(rel_path: str) -> str:
    """Build the served URL for a repo-relative image/markdown path."""
    if not rel_path:
        return ""
    base = cfg.static_base_url.rstrip("/")
    return f"{base}/{rel_path}" if base else f"/static/{rel_path}"


_WORD_RE = re.compile(r"\w+", re.UNICODE)


def _run_fts(conn: sqlite3.Connection, query: str, pool: int) -> list[sqlite3.Row]:
    """Run an FTS5 MATCH, tolerating queries that use FTS operator characters.

    Raw user queries can hit FTS5 special syntax — a paren ('GS ( k'), or a token
    read as a column filter ('model-dependent' -> "no such column"). Any such
    error on the raw query triggers a retry with the bare word tokens quoted,
    which preserves the terms (implicit AND) while neutralising the operators.
    Errors from the (always-valid) sanitized form propagate as real failures.
    """
    sql = ("SELECT rowid, rank FROM fts_chunks WHERE fts_chunks MATCH ? "
           "ORDER BY rank LIMIT ?")
    try:
        return conn.execute(sql, (query, pool)).fetchall()
    except sqlite3.OperationalError as exc:
        log.debug("FTS raw query %r rejected (%s); retrying sanitized", query, exc)
    sanitized = " ".join(f'"{t}"' for t in _WORD_RE.findall(query))
    if not sanitized:
        return []
    return conn.execute(sql, (sanitized, pool)).fetchall()


def _neighbor_pages(conn: sqlite3.Connection, stem: str, page_no: int, span: int) -> list[dict]:
    """Return the surrounding pages of `stem` within +/- span (page no + images)."""
    if span <= 0:
        return []
    rows = conn.execute(
        "SELECT page_no, image_small, image_big FROM pages "
        "WHERE stem = ? AND page_no BETWEEN ? AND ? AND page_no <> ? ORDER BY page_no",
        (stem, page_no - span, page_no + span, page_no),
    ).fetchall()
    return [
        {
            "page": r["page_no"],
            "image_small_url": _image_url(r["image_small"]),
            "image_big_url": _image_url(r["image_big"]),
        }
        for r in rows
    ]


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
        raise ValueError(f"No document with stem '{stem}'.")
    log.info("get_document_summary -> %r (%d pages)", row["title"], row["page_count"])
    return dict(row)


@mcp.tool()
def search_specs(query: str, vendor: str | None = None, k: int = 8, neighbors: int = 1) -> list[dict]:
    """Search the corpus for a query and return ranked page-level results.

    Full-text (FTS5/BM25) retrieval over page bodies, headings, and per-document
    summaries, with exact matching of command tokens (ESC/GS mnemonics, hex). Each
    result includes the document, page number, a text snippet, URLs to that page's
    small/big JPEG renders, and the `neighbors` pages around it (+/- `neighbors`).
    """
    log.info("tool search_specs(query=%r, vendor=%r, k=%d, neighbors=%d)",
             query, vendor, k, neighbors)
    t0 = time.perf_counter()
    conn = db()
    pool = max(k * 5, 30)

    fts_rows = _run_fts(conn, query, pool)
    if not fts_rows:
        log.info("search_specs -> 0 result(s) in %.3fs", time.perf_counter() - t0)
        return []

    ranked = [r["rowid"] for r in fts_rows]
    rank_by_id = {r["rowid"]: r["rank"] for r in fts_rows}

    # Fetch all candidate chunks in one round-trip instead of N individual queries.
    placeholders = ",".join("?" * len(ranked))
    rows_by_id = {
        r["id"]: r
        for r in conn.execute(
            f"SELECT id, stem, vendor, page_no, text, image_small, image_big "
            f"FROM chunks WHERE id IN ({placeholders})",
            ranked,
        ).fetchall()
    }

    results: list[dict] = []
    seen: set[tuple] = set()
    for cid in ranked:
        row = rows_by_id.get(cid)
        if row is None or (vendor is not None and row["vendor"] != vendor):
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
                # FTS5 bm25 rank is negative (lower = better); flip for a positive score.
                "score": round(-rank_by_id[cid], 5),
                "snippet": text[:600] + ("..." if len(text) > 600 else ""),
                "image_small": row["image_small"],
                "image_big": row["image_big"],
                "image_small_url": _image_url(row["image_small"]),
                "image_big_url": _image_url(row["image_big"]),
                "neighbors": _neighbor_pages(conn, row["stem"], row["page_no"], neighbors),
            }
        )
        if len(results) >= k:
            break

    log.info(
        "search_specs -> %d result(s) in %.3fs (fts candidates=%d)",
        len(results), time.perf_counter() - t0, len(fts_rows),
    )
    return results


@mcp.tool()
def get_page(stem: str, page: int) -> dict:
    """Return the full Markdown text and image URLs for a specific page."""
    log.info("tool get_page(stem=%r, page=%d)", stem, page)
    row = db().execute(
        "SELECT stem, vendor, page_no, text, image_small, image_big "
        "FROM pages WHERE stem = ? AND page_no = ?",
        (stem, page),
    ).fetchone()
    if row is None:
        log.warning("get_page: no page %d in document %r", page, stem)
        raise ValueError(f"No page {page} in document '{stem}'.")
    log.info("get_page -> %s page %d (%d chars)", stem, page, len(row["text"]))
    out = dict(row)
    out["image_small_url"] = _image_url(row["image_small"])
    out["image_big_url"] = _image_url(row["image_big"])
    return out


@mcp.tool()
def version() -> dict:
    """Return the server version."""
    return {"version": __version__}


@mcp.custom_route("/static/{path:path}", methods=["GET"])
async def serve_static(request: Request) -> Response:
    """Serve page images / Markdown from the data tree (used when no CDN is set).

    Guards against path traversal: the resolved file must live inside one of the
    allowed data directories (jpeg/, md/), never elsewhere in the repo.
    """
    rel = request.path_params["path"]
    target = (Path(cfg.repo_root) / rel).resolve()
    if not target.is_file() or not any(
        target == root or root in target.parents for root in _STATIC_ROOTS
    ):
        return PlainTextResponse("Not found", status_code=404)
    return FileResponse(target)


if __name__ == "__main__":
    log.info("=== printer-stream-docs MCP server starting ===")
    log.info("Index path      : %s", cfg.index_path)
    log.info("Static base URL : %s", cfg.static_base_url or "(serving /static locally)")
    log.info("Bind address    : %s:%s", cfg.host, cfg.port)
    log.info("Transport       : streamable-http (endpoint /mcp)")
    warm_up()
    log.info("Starting HTTP transport; press Ctrl-C to stop")
    mcp.run(transport="streamable-http")
