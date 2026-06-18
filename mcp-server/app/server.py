"""FastMCP server: tools + plain-HTTP routes, served over streamable HTTP.

Tools are grounded in the baked SQLite index (db.py). Logging only, ASCII only.
The ASGI object `app` is what uvicorn serves; running this module directly uses
FastMCP's own runner.
"""

from __future__ import annotations

import json
import logging
import time
from typing import Dict, List, Optional

from mcp.server.fastmcp import FastMCP, Image
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from . import db, web
from .config import APP_NAME, settings, setup_logging
from .urls import asset_url, load_asset_bytes

try:
    from version import __version__
except Exception:  # pragma: no cover
    __version__ = "unknown"

log = setup_logging()

mcp = FastMCP(APP_NAME, host=settings.host, port=settings.port, stateless_http=True, json_response=True)


@mcp.tool()
def list_documents() -> List[Dict]:
    """List every document with vendor, title, page count, command sets, source
    PDF, and extraction lineage (extracted_at, extractor/pipeline version, and
    per-phase timing)."""
    docs = db.list_documents()
    log.info("list_documents -> %d docs", len(docs))
    return docs


@mcp.tool()
def get_document_summary(stem: str) -> Dict:
    """Return what a document covers (title, command sets, extractive summary).

    stem is the vendor-rooted path without extension, e.g. star/escpos_cm_en.
    """
    doc = db.get_document(stem)
    if doc is None:
        log.info("get_document_summary stem=%r -> not found", stem)
        return {"error": "document not found", "stem": stem}
    log.info("get_document_summary stem=%r -> ok", stem)
    return doc


def _page_list(con, stem: str, page_start: int, page_end: int) -> List[Dict]:
    """The pages a section covers, each with render image URLs."""
    return [
        {
            "page": p["page"],
            "label": p["label"],
            "image": {"small": asset_url(p["jpeg_small"]), "big": asset_url(p["jpeg_big"])},
        }
        for p in db.section_pages(con, stem, page_start, page_end)
    ]


@mcp.tool()
def search_specs(
    query: str, vendor: Optional[str] = None, k: int = settings.search_k
) -> List[Dict]:
    """Search the corpus and return ranked logical SECTIONS - the primary unit, a
    command/topic that may span several pages. Each result has a snippet, the pages
    it covers (with image URLs), and a section_id for get_section.

    query  : free text; command symbols are handled safely (e.g. 'GS ( k').
    vendor : optional filter, e.g. 'star'.
    k      : max results to return (default 15, capped at 50). Pass a larger k for
             broader recall; the default is a balance of recall vs context size.
    For an exact byte/symbol lookup at page granularity, use search_pages instead.
    """
    t0 = time.perf_counter()
    out: List[Dict] = []
    with db.connection() as con:
        hits = db.search_sections(con, query, vendor, k)
        for h in hits:
            try:
                labels = json.loads(h.get("page_labels") or "[]")
            except (TypeError, ValueError):
                labels = []
            out.append({
                "stem": h["stem"],
                "vendor": h["vendor"],
                "doc": h["doc"],
                "section_id": h["section_no"],
                "title": h["title"],
                "heading_path": h["heading_path"],
                "level": h["level"],
                "score": round(h["rank"], 4) if h["rank"] is not None else None,
                "snippet": h["snippet"],
                "page_start": h["page_start"],
                "page_end": h["page_end"],
                "page_labels": labels,
                "pages": _page_list(con, h["stem"], h["page_start"], h["page_end"]),
            })
    log.info(
        "search_specs q=%r vendor=%s k=%s -> %d sections in %.1fms",
        query, vendor, k, len(out), (time.perf_counter() - t0) * 1000.0,
    )
    return out


@mcp.tool()
def search_pages(
    query: str, vendor: Optional[str] = None, k: int = settings.search_k
) -> List[Dict]:
    """Page-level fallback search. Returns ranked PAGES with a snippet and image
    URLs - use when you need an exact byte/symbol match at page granularity and a
    section result from search_specs is too coarse. For normal topical search,
    prefer search_specs.

    query/vendor/k behave as in search_specs.
    """
    t0 = time.perf_counter()
    out: List[Dict] = []
    with db.connection() as con:
        hits = db.search_pages(con, query, vendor, k)
        for h in hits:
            out.append({
                "stem": h["stem"],
                "vendor": h["vendor"],
                "doc": h["doc"],
                "page": h["page"],
                "label": h["label"],
                "heading_path": h["heading_path"],
                "score": round(h["rank"], 4) if h["rank"] is not None else None,
                "snippet": h["snippet"],
                "image": {"small": asset_url(h["jpeg_small"]), "big": asset_url(h["jpeg_big"])},
                "markdown_url": asset_url(h["markdown"]),
            })
    log.info(
        "search_pages q=%r vendor=%s k=%s -> %d pages in %.1fms",
        query, vendor, k, len(out), (time.perf_counter() - t0) * 1000.0,
    )
    return out


@mcp.tool()
def get_page(stem: str, page: int) -> Dict:
    """Return a page's full Markdown plus image URLs.

    stem is the vendor-rooted path without extension; page is 1-based.
    """
    row = db.get_page(stem, page)
    if row is None:
        log.info("get_page stem=%r page=%s -> not found", stem, page)
        return {"error": "page not found", "stem": stem, "page": page}
    log.info("get_page stem=%r page=%s -> %d chars", stem, page, len(row.get("body") or ""))
    return {
        "stem": row["stem"],
        "vendor": row["vendor"],
        "doc": row["doc"],
        "page": row["page"],
        "label": row["label"],
        "heading_path": row["heading_path"],
        "body": row["body"],
        "source": row["source"],
        "flagged": bool(row["flagged"]),
        "image": {"small": asset_url(row["jpeg_small"]), "big": asset_url(row["jpeg_big"])},
        "markdown_url": asset_url(row["markdown"]),
    }


@mcp.tool()
def get_section(stem: str, section_id: int) -> Dict:
    """Return a logical section's full Markdown plus the pages it covers.

    A section is the primary retrieval unit (a command/topic that may span pages).
    stem is the vendor-rooted path without extension; section_id comes from a
    search_specs result. The returned `pages` list is what the section belongs to,
    each with image URLs and per-page markdown.
    """
    row = db.get_section(stem, section_id)
    if row is None:
        log.info("get_section stem=%r section=%s -> not found", stem, section_id)
        return {"error": "section not found", "stem": stem, "section_id": section_id}
    try:
        labels = json.loads(row.get("page_labels") or "[]")
    except (TypeError, ValueError):
        labels = []
    with db.connection() as con:
        pages = db.section_pages(con, stem, row["page_start"], row["page_end"])
    log.info("get_section stem=%r section=%s -> %d chars", stem, section_id, len(row.get("body") or ""))
    return {
        "stem": row["stem"],
        "vendor": row["vendor"],
        "doc": row["doc"],
        "section_id": row["section_no"],
        "title": row["title"],
        "heading_path": row["heading_path"],
        "level": row["level"],
        "body": row["body"],
        "page_start": row["page_start"],
        "page_end": row["page_end"],
        "page_labels": labels,
        "pages": [
            {
                "page": p["page"],
                "label": p["label"],
                "image": {"small": asset_url(p["jpeg_small"]), "big": asset_url(p["jpeg_big"])},
                "markdown_url": asset_url(p["markdown"]),
            }
            for p in pages
        ],
    }


@mcp.tool()
def get_page_image(stem: str, page: int, size: str = "small") -> Image:
    """Return a page's rendered image so a vision-capable client can actually see
    it - for figures, diagrams, and dense tables the Markdown cannot convey.

    stem is the vendor-rooted path without extension; page is 1-based.
    size: 'small' (~1024px, default; keep payloads modest) or 'big' (full-res).
    Fetch one page on demand; do not request images for every search hit.
    """
    if size not in ("small", "big"):
        size = "small"
    row = db.get_page_assets(stem, page)
    if row is None:
        raise ValueError("page not found: %s page %s" % (stem, page))
    rel = row["jpeg_big"] if size == "big" else row["jpeg_small"]
    data = load_asset_bytes(rel)
    log.info("get_page_image stem=%r page=%s size=%s -> %d bytes", stem, page, size, len(data))
    return Image(data=data, format="jpeg")


def build_app():
    """Build the ASGI app: MCP endpoint + landing/docs/health/version (+ static)."""
    web.bind(mcp)
    app = mcp.streamable_http_app()  # serves the MCP endpoint at /mcp, with lifespan

    # Prepend our exact-path routes so they are matched before the MCP app.
    extra = [
        Route("/", web.landing, methods=["GET"]),
        Route("/healthz", web.healthz, methods=["GET"]),
        Route("/version", web.version_endpoint, methods=["GET"]),
        Route("/documents", web.documents_json, methods=["GET"]),
        Route("/docs", web.docs_page, methods=["GET"]),
    ]
    sd = settings.static_directory()
    if sd is not None:
        extra.append(Mount("/static", app=StaticFiles(directory=str(sd)), name="static"))
        log.info("Serving static assets from %s under /static", sd)
    else:
        log.info("No static directory; relying on DOCS_STATIC_BASE_URL (CDN) for assets")

    app.router.routes[:0] = extra
    log.info("%s v%s ready (MCP at /mcp)", APP_NAME, __version__)
    return app


app = build_app()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
