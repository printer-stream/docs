# Printer Stream Docs - MCP server

A Model Context Protocol server (Python 3.13, FastMCP over streamable HTTP) that
lets AI tools search the printer/device specification corpus and ground answers
in the exact page text and image. See `../DESIGN.md`.

## How it works

The pipeline (PDF -> extraction -> indexing -> this server) bakes a pre-generated
SQLite FTS5 index into the image; the server queries it. Every page is
`markdown/<stem>/page-NN.md` paired with `jpeg/<stem>/{small,big}/page-NN.jpg`, so
results carry image URLs for the hit page and its neighbours.

- **Ranked full-text + trigram recall:** keyword/phrase search (BM25) plus a
  trigram net so command/symbol queries (`GS ( k`, hex `1B 40`) are not missed.
  User text is escaped to a safe FTS5 phrase (raw `GS ( k` is a MATCH syntax error).
- **Summaries:** each document has an extractive "what it covers" blurb.

## Tools

| Tool | Purpose |
|------|---------|
| `list_documents()` | All docs with vendor, title, page count, command sets |
| `get_document_summary(stem)` | What devices/technologies a doc covers |
| `search_specs(query, vendor?, k?, neighbors?)` | Ranked pages with snippet + image URLs (+ neighbour images) |
| `get_page(stem, page)` | Full page Markdown + image URLs |
| `get_page_image(stem, page, size?)` | The rendered page as image content (base64) a vision client can view; `size` small (default) or big |

`stem` is the vendor-rooted path without extension, e.g. `star/escpos_cm_en`.

`search_specs`/`get_page` return image *URLs* (a human or a client with a fetch
tool can open them). `get_page_image` returns the actual image as MCP image
content, so a vision-capable client can see the page directly - use it on demand
for figures/diagrams/dense tables, not for every search hit (payload size). The
bytes come from the baked static dir (stuffed image) or the CDN/base URL (lean).

## HTTP surface

| Path | Purpose |
|------|---------|
| `/mcp` | MCP endpoint (streamable HTTP) |
| `/` | Landing page (corpus overview) for robots and guests |
| `/docs` | Tool catalog (the "swagger-like" view; introspects live tool schemas) |
| `/documents` | JSON: source PDFs + extraction lineage (extracted_at, extractor version, per-phase timing) |
| `/version` | JSON: app version + index build info (created_at, indexer version, doc/page counts) |
| `/healthz` | Health JSON |
| `/static/...` | Static assets (only when self-serving; see below) |

The index build timestamp + indexer version (and per-document extraction
timestamp + extractor/pipeline version) are baked into the index DB at build
time, so they are served from the one baked artifact. `list_documents()` (MCP
tool) returns the same per-document lineage.

## Static assets / CDN

Image and markdown URLs are built from `DOCS_STATIC_BASE_URL` when set (CDN),
otherwise served by this process under `/static`. Switching to a CDN is exactly
setting that one env var - no rebuild.

## Configuration

Config is loaded from a `.env` file (see [.env.example](.env.example)) and any
matching environment variable overrides the `.env` value. Nothing reads the
environment directly; everything flows through one `pydantic-settings` object. In
production, set these via the environment (Render dashboard).

| Var | Default | Meaning |
|-----|---------|---------|
| `DOCS_DB_PATH` | `/app/index/specs.db` | Baked search index |
| `DOCS_STATIC_DIR` | `/app/static` | Static root; ignored if absent (lean image) |
| `DOCS_BASE_URL` | (unset) | Public base URL; builds absolute asset URLs |
| `DOCS_STATIC_BASE_URL` | = `DOCS_BASE_URL` | Static/CDN base; set to move static to a CDN |
| `PORT` | `10000` | Listen port (Render sets this) |
| `HOST` | `0.0.0.0` | Listen address |
| `LOG_LEVEL` | `INFO` | Logging level (logging only; no prints) |
| `DOCS_SEARCH_K` / `DOCS_SEARCH_MAX_K` | `8` / `50` | Default / max result count |

Asset URLs are absolute when `DOCS_BASE_URL` (or `DOCS_STATIC_BASE_URL`) is set,
otherwise relative `/static/...`. `DOCS_STATIC_BASE_URL` defaults to
`DOCS_BASE_URL`, so a server with its public URL configured returns absolute
image URLs that remote MCP clients can fetch; pointing it at a CDN is the only
change needed to move static off the server.

## Build (two variants, same Dockerfile, context = repo root)

```bash
VER=$(grep __version__ mcp-server/version.py | cut -d'"' -f2)
# Lean: index only; static via CDN or a mounted volume at /app/static
docker build -f mcp-server/Dockerfile --target lean    -t mcp-server:$VER .
# Stuffed: also bakes jpeg + markdown; fully self-contained
docker build -f mcp-server/Dockerfile --target stuffed -t mcp-server:$VER-stuffed .
```

## Run locally

```bash
docker run --rm -p 10000:10000 mcp-server:$VER-stuffed
# then: open http://localhost:10000/  and  http://localhost:10000/docs
```

Without Docker (needs the index built under data-extraction/index/fulltext/):

```bash
pip install -r mcp-server/requirements.txt
cd mcp-server
DOCS_DB_PATH=../data-extraction/index/fulltext/specs.db \
DOCS_STATIC_DIR=../data-extraction \
uvicorn app.server:app --port 10000
```

## Connect from VS Code / Copilot / Claude

Point your MCP client at the streamable-HTTP endpoint `http(s)://<host>/mcp`. For
interactive testing use the MCP Inspector. Deploys to Render as a Docker image.
