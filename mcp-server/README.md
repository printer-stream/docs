# printerrr-docs MCP server

A Model Context Protocol server that lets AI tools (GitHub Copilot, Claude,
etc.) search the printer/device specification corpus in this repo and ground
answers in the exact page text and image.

## How it works

```
PDF push ──► md/ + jpeg/ (per-page text & images)
                 │
                 ├─ build-index.yml (CI) ─► index/specs.db  (committed)
                 │       chunks + FTS5 + vector embeddings + doc summaries
                 │
                 └─ Render web service loads index/specs.db read-only
                          │
                          └─ MCP tools over Streamable HTTP ──► Copilot / Claude
```

- **Text↔image alignment:** every page is `md/<doc>/page-NN.md` paired with
  `jpeg/<doc>/{small,big}/page-NN.jpg`. Search results carry both.
- **Hybrid search:** FTS5 keyword search (exact `ESC`/`GS`/hex command lookups)
  fused with vector search (conceptual questions) via Reciprocal Rank Fusion.
- **Summaries:** each document gets a "what devices/technologies it covers"
  blurb, exposed via `get_document_summary` and searchable.

## Tools

| Tool | Purpose |
|------|---------|
| `list_documents()` | All docs with vendor, title, page count |
| `get_document_summary(stem)` | What devices/technologies a doc covers |
| `search_specs(query, vendor?, k?)` | Ranked page results with snippet + image paths |
| `get_page(stem, page)` | Full page Markdown + image paths |

`stem` is the repo-relative path without extension, e.g. `star/star_graphic_cm_en`.

## Build the index

```bash
pip install -r mcp-server/requirements.txt
python mcp-server/indexer.py          # writes index/specs.db
```

Set `OPENAI_API_KEY` to generate higher-quality LLM summaries; otherwise an
extractive fallback is used. Embedding model defaults to
`BAAI/bge-small-en-v1.5` (CPU, no key) and runs in CI on every `md/` change.

## Run locally

```bash
pip install -r mcp-server/requirements.txt
cd mcp-server && python server.py     # Streamable HTTP on :8000 (/mcp)
```

## Deploy on Render

`render.yaml` (repo root) defines a Python web service. The index is committed,
so boot only loads it. Connect a client to `https://<service>.onrender.com/mcp`.

### Connect from VS Code / Copilot

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "printerrr-docs": {
      "type": "http",
      "url": "https://<service>.onrender.com/mcp"
    }
  }
}
```
