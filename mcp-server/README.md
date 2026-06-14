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

> Requires Python 3.10+ (the `mcp` package does not support 3.9; CI and Render
> pin 3.13). On startup the
> server logs every step. The slow part is loading the embedding model (a few
> seconds warm, longer on first run while it downloads + caches). You will see:
>
> ```
> INFO [printerrr-docs] === printerrr-docs MCP server starting ===
> INFO [printerrr-docs] Index ready in 0.08s: 1 document(s), 59 chunk(s)
> INFO [printerrr-docs] Loading embedding model 'BAAI/bge-small-en-v1.5' ...
> INFO [printerrr-docs] Embedding model loaded in 5.33s (dim=384)
> INFO [printerrr-docs] Warm-up complete in 6.79s -- server ready to serve queries
> INFO Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
> ```
>
> Logging env vars: `DOCS_LOG_LEVEL=DEBUG` for per-query detail (FTS/vector hit
> counts, embed timing); `DOCS_VERBOSE_DEPS=1` to also show the underlying
> HuggingFace/httpx download chatter (hidden by default).

## Validation

After building the index, verify the index and the server before deploying.

### 1. Verify the index file

```bash
python - <<'PY'
import sqlite3, sqlite_vec
from pathlib import Path
db = sqlite3.connect("index/specs.db")
db.enable_load_extension(True); sqlite_vec.load(db); db.enable_load_extension(False)
docs   = db.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
chunks = db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
vecs   = db.execute("SELECT COUNT(*) FROM vec_chunks").fetchone()[0]
fts    = db.execute("SELECT COUNT(*) FROM fts_chunks").fetchone()[0]
print(f"documents={docs} chunks={chunks} vec_chunks={vecs} fts_chunks={fts}")
assert chunks == vecs == fts, "chunk / vector / fts counts must match"
print("OK: index is internally consistent")
PY
```

Expected: `chunks`, `vec_chunks`, and `fts_chunks` are equal and non-zero.

### 2. Exercise the tools directly (no HTTP)

```bash
cd mcp-server && python - <<'PY'
import server
server.warm_up()                                   # logs index + model load timing
print("docs   :", [d["stem"] for d in server.list_documents()])
print("summary:", server.get_document_summary("star/star_graphic_cm_en")["title"])
hits = server.search_specs("how to print a bit image graphic", k=3)
for h in hits:
    print(f"  p{h['page']:>3}  {h['score']}  {h['image_small']}")
print("page 1 :", server.get_page("star/star_graphic_cm_en", 1)["image_big"])
PY
```

Each `search_specs` result must include a `page` and the matching
`image_small` / `image_big` path for that page.

### 3. Smoke-test the HTTP transport

Start the server, then in another shell:

```bash
# Should return HTTP 200
curl -s -o /dev/null -w "init: %{http_code}\n" \
  -X POST http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"curl","version":"0"}}}'
```

For full interactive testing, use the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector
# Transport: Streamable HTTP   URL: http://127.0.0.1:8000/mcp
```

## Measuring search quality

`evaluate.py` quantifies retrieval quality with **recall@k**, **MRR@10**, and
query latency. It is self-supervised: for a sample of pages it derives a query
the page should answer, runs `search_specs`, and checks where the source page
ranks. (It calls `search_specs` directly, isolating retrieval quality from the
HTTP transport.)

```bash
cd mcp-server

# No-LLM mode: queries built from page headings / salient tokens (zero deps).
python evaluate.py --sample 30 --no-llm

# LLM mode: natural questions per page -> realistic test of conceptual search.
# Uses OpenAI if OPENAI_API_KEY is set (or any OpenAI-compatible endpoint via
# OPENAI_BASE_URL + DOCS_EVAL_LLM=1, e.g. a local Ollama/LM Studio model).
export OPENAI_API_KEY=sk-...
python evaluate.py --sample 30
```

Sample output:

```
=== Search quality ===
queries          : 20  (fallback generated)
recall@1         : 0.850  (17/20)
recall@3         : 1.000  (20/20)
recall@5         : 1.000  (20/20)
MRR@10           : 0.917
latency p50 / p95: 26 ms / 875 ms
```

Notes:
- **recall@k** = fraction of queries whose source page appears in the top k.
  **MRR@10** = mean of 1/rank of the source page. Higher is better; 1.0 is perfect.
- No-LLM numbers are optimistic (queries share vocabulary with the page).
  LLM-generated queries are the honest measure of conceptual retrieval -- use
  them before trusting the numbers.
- Re-run after changing the embedding model, chunking, or fusion weights to
  catch regressions. The `--seed` flag keeps the page sample reproducible.

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
