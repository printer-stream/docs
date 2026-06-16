"""Plain-HTTP routes: landing page, tool catalog, health, version.

ASCII only, no emojis. The landing page serves search-engine robots and human
guests; the tool catalog is the "swagger-like" view of the MCP tools.
"""

from __future__ import annotations

import html
import json
import logging

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse

from . import db
from .config import APP_NAME, settings

try:
    from version import __version__
except Exception:  # pragma: no cover - version module always present in image
    __version__ = "unknown"

log = logging.getLogger(APP_NAME)

# Set by server.build_app() so the catalog can introspect live tool schemas.
_mcp = None

_FALLBACK_TOOLS = [
    {"name": "list_documents", "description": "All documents with vendor, title, page count, languages.", "schema": {}},
    {"name": "get_document_summary", "description": "What devices/technologies a document covers.", "schema": {"stem": "string"}},
    {"name": "search_specs", "description": "Ranked page results with snippet and image URLs.", "schema": {"query": "string", "vendor": "string?", "k": "int", "neighbors": "int"}},
    {"name": "get_page", "description": "Full page Markdown plus image URLs.", "schema": {"stem": "string", "page": "int"}},
]

_STYLE = (
    "body{font-family:-apple-system,Segoe UI,Helvetica,Arial,monospace;margin:2rem auto;"
    "max-width:60rem;padding:0 1rem;line-height:1.5;color:#1a1a1a;}"
    "h1{margin-bottom:0.2rem;} .sub{color:#666;margin-top:0;}"
    "table{border-collapse:collapse;width:100%;margin:1rem 0;}"
    "td,th{border:1px solid #ddd;padding:0.35rem 0.6rem;text-align:left;font-size:0.9rem;}"
    "code{background:#f3f3f3;padding:0.1rem 0.3rem;border-radius:3px;}"
    "pre{background:#f6f6f6;padding:0.6rem;overflow:auto;border-radius:4px;}"
    "section{border-top:1px solid #eee;padding-top:0.5rem;} a{color:#0645ad;}"
)


def bind(mcp) -> None:
    global _mcp
    _mcp = mcp


def _page(title: str, body: str) -> str:
    return (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
        "<title>%s</title><style>%s</style></head><body>%s"
        "<footer><hr><p class='sub'>%s v%s</p></footer></body></html>"
        % (html.escape(title), _STYLE, body, APP_NAME, html.escape(__version__))
    )


async def healthz(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


async def version_endpoint(request: Request) -> JSONResponse:
    return JSONResponse({"name": APP_NAME, "version": __version__})


async def landing(request: Request) -> HTMLResponse:
    docs = db.list_documents()
    base = settings.resolved_static_base_url
    mode = ("served from %s" % html.escape(base)) if base else "self-served (relative /static)"
    rows = "".join(
        "<tr><td>%s</td><td>%s</td><td>%d</td><td>%s</td><td><code>%s</code></td></tr>"
        % (
            html.escape(d["vendor"]),
            html.escape(d["title"] or ""),
            d["page_count"] or 0,
            html.escape(d["languages"] or ""),
            html.escape(d["stem"]),
        )
        for d in docs
    )
    body = (
        "<h1>Printer Stream Docs</h1>"
        "<p class='sub'>Machine-readable printer/device specification corpus, "
        "served over the Model Context Protocol.</p>"
        "<p>MCP endpoint: <code>/mcp</code> (streamable HTTP). "
        "Tool catalog: <a href='/docs'>/docs</a>. "
        "Health: <a href='/healthz'>/healthz</a>. Static assets: %s.</p>"
        "<h2>Documents (%d)</h2>"
        "<table><tr><th>Vendor</th><th>Title</th><th>Pages</th><th>Command sets</th><th>stem</th></tr>%s</table>"
        % (mode, len(docs), rows)
    )
    return HTMLResponse(_page("Printer Stream Docs", body))


async def docs_page(request: Request) -> HTMLResponse:
    tools = []
    if _mcp is not None:
        try:
            for t in await _mcp.list_tools():
                tools.append(
                    {
                        "name": t.name,
                        "description": t.description or "",
                        "schema": getattr(t, "inputSchema", {}) or {},
                    }
                )
        except Exception:
            log.exception("Failed to introspect tools for /docs")
    if not tools:
        tools = _FALLBACK_TOOLS

    blocks = "".join(
        "<section><h2><code>%s</code></h2><p>%s</p><pre>%s</pre></section>"
        % (
            html.escape(t["name"]),
            html.escape(t["description"]),
            html.escape(json.dumps(t["schema"], indent=2, ensure_ascii=True)),
        )
        for t in tools
    )
    body = (
        "<h1>Tool catalog</h1>"
        "<p class='sub'>Tools exposed at the <code>/mcp</code> endpoint. Use an MCP "
        "client (or the MCP Inspector) to call them.</p>" + blocks
    )
    return HTMLResponse(_page("Tool catalog", body))
