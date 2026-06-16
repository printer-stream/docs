"""FastMCP server: tools + plain-HTTP routes, served over streamable HTTP.

Tools are grounded in the baked SQLite index (db.py). Logging only, ASCII only.
The ASGI object `app` is what uvicorn serves; running this module directly uses
FastMCP's own runner.
"""

from __future__ import annotations

import logging
import time
from typing import Dict, List, Optional

from mcp.server.fastmcp import FastMCP
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from . import db, web
from .config import APP_NAME, settings, setup_logging
from .urls import asset_url

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


@mcp.tool()
def search_specs(
    query: str, vendor: Optional[str] = None, k: int = settings.search_k, neighbors: int = 1
) -> List[Dict]:
    """Search the corpus. Returns ranked pages with a snippet and image URLs.

    query  : free text; command symbols are handled safely (e.g. 'GS ( k').
    vendor : optional filter, e.g. 'star'.
    k      : max results. neighbors: also return image URLs for +/-N pages.
    """
    t0 = time.perf_counter()
    out: List[Dict] = []
    with db.connection() as con:
        hits = db.search_pages(con, query, vendor, k)
        for h in hits:
            entry = {
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
            }
            if neighbors and neighbors > 0:
                nb = db.neighbor_pages(con, h["stem"], h["page"] - neighbors, h["page"] + neighbors)
                entry["neighbors"] = [
                    {"page": n["page"], "image_small": asset_url(n["jpeg_small"])}
                    for n in nb
                    if n["page"] != h["page"]
                ]
            out.append(entry)
    log.info(
        "search_specs q=%r vendor=%s k=%s neighbors=%s -> %d hits in %.1fms",
        query, vendor, k, neighbors, len(out), (time.perf_counter() - t0) * 1000.0,
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
