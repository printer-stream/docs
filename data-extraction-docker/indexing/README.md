# indexing image

Builds the pre-generated search index from the extraction outputs. Pure standard
library (SQLite FTS5 + trigram). See `../../DESIGN.md`.

Output: `data-extraction/index/<type>/specs.db` (default type `fulltext`) plus
`data-extraction/index/manifest.json`. The `.db` is tracked via Git LFS and baked
into both mcp-server image variants.

## What it builds

A single SQLite file with:

- `pages` / `documents` - metadata + body (self-contained for retrieval).
- `pages_fts` - ranked full-text, `unicode61` tokenizer extended with
  command-significant `tokenchars` (`@/*^<>=&|~#+`) so phrases like `GS / bit`
  match while normal prose search is unharmed.
- `pages_trgm` - `trigram` index: the substring/symbol recall net so no query is
  silently missed (hex bytes, `GS ( k`, partial tokens).
- `documents_fts` - title/summary search; summaries are extractive (no LLM):
  vendor, title, detected command languages (ESC/POS, HPGL, ...), top headings.

`index/<type>/` keeps index types side by side so a future `vector/` index can be
built and compared against `fulltext/` with the same eval harness.

## Query escaping (important for the MCP server)

FTS5 MATCH treats `( ) " *` as query syntax, so raw user input like `GS ( k` is a
*syntax error*. `indexer/search.py` exposes `fts_query()` which turns arbitrary
text into a safe phrase query, plus `search_fulltext` / `search_trigram` /
`search_documents`. The MCP server must reuse these (do not pass raw user text to
MATCH).

## Build / evaluate

```bash
docker build -t printerrr-indexing data-extraction-docker/indexing

# Build the index (runs the eval afterwards)
docker run --rm -v "$PWD":/work printerrr-indexing build

# Re-run just the eval (recall@k over eval/queries.json)
docker run --rm -v "$PWD":/work printerrr-indexing evaluate --k 10

# Gate in CI: fail if recall drops
docker run --rm -v "$PWD":/work printerrr-indexing evaluate --min-recall 0.9
```

The eval query set (`eval/queries.json`) is the objective measure of search
quality and the basis for comparing index types; extend it as the corpus grows.
