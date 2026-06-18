# indexing image

Builds the pre-generated search index from the extraction outputs. Pure standard
library (SQLite FTS5 + trigram). See `../../DESIGN.md`.

Output: `data-extraction/index/<type>/specs.db` (default type `fulltext`) plus
`data-extraction/index/manifest.json`. The `.db` is tracked via Git LFS and baked
into both mcp-server image variants.

## What it builds

Retrieval is **section-first**: a command/topic is a logical unit that may span
several pages, so a section (not a page) is the primary search result. Pages stay
indexed as a fallback and as the displayable artifact. A single SQLite file with:

- `sections` - the primary unit, read from `data-extraction/sections/<stem>.json`:
  title, heading path, level, body, and the **page range/labels it covers**
  (`page_start`, `page_end`, `page_labels` as a JSON array) so a result can cite
  and show its pages.
- `sections_fts` - ranked section full-text, `unicode61` tokenizer extended with
  command-significant `tokenchars` (`@/*^<>=&|~#+`) so phrases like `GS / bit`
  match while normal prose search is unharmed. Ranked with `bm25` column weights
  (title > heading_path > body).
- `sections_trgm` - `trigram` substring/symbol recall net for sections.
- `pages` / `documents` - metadata + body (self-contained, fallback + display).
- `pages_fts` / `pages_trgm` - the page-level fallback search (same tokenizers).
- `documents_fts` - title/summary search; summaries are extractive (no LLM):
  vendor, title, detected command languages (ESC/POS, HPGL, ...), top headings.

Sections are backend-agnostic: the build consumes whichever `sections.json` the
extraction `sections` phase produced (`headings` by default, `llm-text` from a
GPU/hosted profile) - upgrading sectioning quality needs no index change. A doc
without `sections.json` is still indexed at the page level (a warning is logged).

`index/<type>/` keeps index types side by side so a future `vector/` index can be
built and compared against `fulltext/` with the same eval harness.

## Query building (important for the MCP server)

FTS5 MATCH treats `( ) " *` as query syntax, so raw user input like `GS ( k` is a
*syntax error*. `indexer/search.py` builds safe queries:

- `fts_and()` - AND of quoted per-word terms (the ranked keyword search): a
  multi-word query matches documents containing ALL terms, not only the exact
  phrase. This is the key behaviour - quoting the whole query as one phrase made
  most multi-word searches return nothing.
- `fts_phrase()` - the whole text as one quoted phrase, for the trigram index's
  exact substring/symbol matching (`GS ( k`, `1B 40`).
- `search_sections()` - the canonical (primary) path over the section tables:
  ranked AND, an OR top-up for recall, then the trigram net. `search_pages()` is
  the identical strategy over the page tables (the fallback). The MCP server
  mirrors both exactly (`mcp-server/app/db.py`): `search_specs` -> sections,
  `search_pages` -> pages.

## Build / evaluate

```bash
docker build -t printer-stream-indexing data-extraction-docker/indexing

# Build the index (runs the eval afterwards)
docker run --rm -v "$PWD":/work printer-stream-indexing build

# Re-run just the eval over eval/queries.json (sections by default)
docker run --rm -v "$PWD":/work printer-stream-indexing evaluate --k 10
docker run --rm -v "$PWD":/work printer-stream-indexing evaluate --unit page   # fallback path

# Gate in CI: fail if doc-hit recall drops
docker run --rm -v "$PWD":/work printer-stream-indexing evaluate --min-recall 0.9
```

The eval query set (`eval/queries.json`) is the objective measure of search
quality and the basis for comparing index types; extend it as the corpus grows.

Each query carries ground truth, and the harness reports:

- **doc-hit recall@k** - did an expected document appear in the top-k. This is
  the CI gate (`--min-recall`). Queries can be doc-level (`expect_stem`).
- **precision@k, recall@k, MRR, nDCG@k** - graded retrieval metrics for
  page-labeled queries (`"relevant": ["<stem>#<label>", ...]`). nDCG/MRR capture
  *ranking* quality (the relevant unit near the top), which precision@k misses when
  only 1-2 pages are relevant.

Ground truth stays page-level. `--unit section` (default) scores the section
path: a section counts as relevant if it covers any relevant page, and recall@k is
page coverage (fraction of relevant pages reached by a retrieved section).
`--unit page` scores the page fallback with the original page-level semantics.

These make quality measurable per change: e.g. a verbose query whose relevant
pages rank below incidental keyword matches shows up as low MRR/nDCG, and a
figure page that search can't reach (little extractable text) shows up as a
recall miss - the signal that the optional `describe` (VLM) phase is needed.
