# Design: complete rewrite of the PDF -> search -> MCP pipeline

Status: accepted (2026-06-16). Supersedes the previous embeddings/vector-based
process. This document is the source of truth for the rebuild; per-stage READMEs
link back here.

## Goal

Turn a corpus of niche printer/device specification PDFs (ESC/POS, HPGL, line
mode, hardware manuals) into machine-readable artifacts that ground an MCP
server. The hard requirements are domain-specific:

- Preserve meaning. These are control-language specs; a mangled `GS ( L` or a
  dropped hex byte is a correctness bug, not a cosmetic one.
- Findability. A user must be able to locate an exact command/term.
- Recall. Search must not silently miss a page that contains the answer.

Resource usage is not the priority (extraction is a one-time job), but we will
not push every page through a top-tier hosted model.

## Corpus shape (why the design is what it is)

12 PDFs across epson/hp/jvc/star, roughly 2,500-3,000 pages. The corpus is
heterogeneous:

- Most docs are born-digital with a real text layer plus embedded figures.
- At least one (`pdf/hp/FFONS49JUMXQZJH.pdf`: 230 images, no detectable text
  pages) is effectively scanned/image-only.
- Several use object streams, so a clean text layer is not guaranteed per page.

A single extractor is therefore the wrong tool. The pipeline is tiered and
quality-gated so each page gets the cheapest method that clears the bar, and the
bad minority is escalated.

## Architecture

One-way data flow, three independently runnable Dockerized stages:

```
pdf/ ──▶ [1] extraction ──▶ [2] indexing ──▶ [3] mcp-server
         jpeg + markdown      search index     serves all + MCP/HTTP
```

### Directory layout

Code and static outputs are kept strictly separate.

```
pdf/<vendor>/<doc>.pdf                 # sources

data-extraction/                       # STATIC OUTPUTS ONLY (binaries via Git LFS)
  jpeg/<vendor>/<doc>/small/page-NN.jpg   # render phase: ~1024px previews
  jpeg/<vendor>/<doc>/big/page-NN.jpg     # render phase: full-resolution renders
  text/<vendor>/<doc>/page-NN.txt         # text phase: raw text-layer slices
  markdown/<vendor>/<doc>/page-NN.md      # markdown phase: per-page slices ("md")
  markdown/<vendor>/<doc>/document.md     # assemble phase: full doc ("md-bulk")
  describe/<vendor>/<doc>/page-NN.txt     # describe phase (optional): VLM descriptions
  quality/<vendor>/<doc>.json             # quality phase: per-page QA metrics
  quality/report.html                     # assemble phase: review of flagged pages
  pagemap/<vendor>/<doc>.json             # assemble phase: source-of-truth map
  pagemap/schema.json                     # JSON Schema for the pagemap contract
  meta/<vendor>/<doc>/<phase>.json        # per-phase timing + toolchain metadata
  index/
    fulltext/                             # primary index (now)
    vector/                               # reserved (later) - lets us compare types
    manifest.json                         # builder version, params, counts, checksums

data-extraction-docker/                # CODE (build contexts)
  extraction/   Dockerfile + extractor/QA code
  indexing/     Dockerfile + index-builder code

mcp-server/                            # CODE (Python 3.13 service)
```

Notes:

- `markdown/` holds both per-page slices (`page-NN.md`) and the bulk
  single-file render (`document.md`). The task names one path,
  `./data-extraction/markdown`; keeping both under it avoids a second tree while
  preserving the md / md-bulk distinction the MCP image bakes.
- `page-NN` is zero-padded to the width of the document's page count. The 1:1
  mapping `page-NN.md` <-> `jpeg/.../page-NN.jpg` is what lets search cite a page
  and show its render. Nothing downstream assumes filename math: `pagemap` is
  authoritative.
- `index/<type>/` makes index types siblings so we can build and compare them
  (fulltext now, vector later) instead of guessing one design up front.

## Stage 1: data extraction (PDF -> JPEG + Markdown)

Tiered, quality-gated. Implemented in `data-extraction-docker/extraction/`.

- Tier A (primary): Docling (Apache-2.0) for layout-aware Markdown - table
  structure (TableFormer), reading order on multi-column manuals, exports clean
  Markdown, runs fully local, no per-page API cost. Marker is the alternative;
  we keep it only as a sample-comparison probe, not a second pipeline.
- Tier B (fallback / cross-check): OCR for pages with missing or garbled text
  layers (the scanned HP doc, image-only pages). Also an independent signal to
  detect bad text-layer extraction.
- Tier C (selective, gated, off by default): re-transcribe only pages that fail
  the quality gate (mangled command tables, figure-dense pages) with a VLM. Kept
  off under GitHub-hosted CI; enabled only when private runners exist. Never all
  pages, never a top-tier hosted model by default.
- JPEG rendering: small (~1024px) + big (full-res), driven off the same page
  enumeration that produces the markdown, so the 1:1 mapping is guaranteed and
  recorded in `pagemap`.

The extractor is manifest-driven and shardable: a doc manifest lets a CI matrix
split the corpus across parallel runners (doc-level sharding) to stay under the
runner time cap.

### Phase decomposition

Extraction is not one opaque pass; it is a sequence of discrete phases sharing one
image, each producing a single artifact kind for a whole document and recording
its own timing + metadata. This keeps intermediates for troubleshooting, lets us
re-run/replace one phase without redoing the others, and makes room to insert new
phases (e.g. a VLM `describe` step) between existing ones.

| Phase | Input | Output |
|-------|-------|--------|
| `render`   | pdf           | `jpeg/<stem>/{small,big}/page-NN.jpg` |
| `text`     | pdf           | `text/<stem>/page-NN.txt` (raw text layer) |
| `markdown` | pdf           | `markdown/<stem>/page-NN.md` (Docling; the slow phase) |
| `quality`  | markdown+text | `quality/<stem>.json` |
| `describe` | jpeg + quality | `describe/<stem>/page-NN.txt` (VLM; optional, off by default) |
| `assemble` | all the above | `pagemap/<stem>.json` + `markdown/<stem>/document.md` + reports |

`describe` runs after `quality`; its `--gate` selects pages - default
`illustrated` (any page with a figure placeholder plus flagged/empty pages, since
a text-rich page can still hide a diagram the text never describes), or `flagged`
/ `all`. It is excluded from the `all-phases` convenience and
only fires when an endpoint is configured. It is provider-pluggable via any
OpenAI-compatible vision endpoint (local vLLM or a hosted model) and writes
supplementary descriptions that the index treats as a separate, lower-signal
field - never merged into the authoritative markdown.

- Atomic unit is (phase, document): "all or none artifacts of the same kind", no
  per-page resume state. Re-run a phase to redo it.
- Each phase writes `meta/<stem>/<phase>.json` (tool, version, params,
  start/end, total + per-page timing, status). `assemble` folds a summary into the
  pagemap's `phases` field, so timing/quality lineage lives with the results.

### Quality verification

- Automated per-page metrics -> `quality/<vendor>/<doc>.json`: char/alnum ratio,
  dictionary hit-rate (gibberish detector), OCR-vs-text-layer agreement,
  table-cell counts, control-char/symbol preservation, and domain token checks
  (ESC/POS pages should contain mnemonics like `ESC @` / `GS ( L`; HPGL pages
  should contain `PU`/`PD`/`PA`).
- A confidence gate flags the low-scoring minority for Tier C and/or human
  review.
- Manual review is bounded: `quality/report.html` shows JPEG and extracted
  Markdown side-by-side for flagged pages only - eyeball ~5%, not 3,000 pages.
- Before the full run, hand-verify ~3-5 pages per doc (especially command-table
  pages) to validate the tool choice cheaply.

### Caveats

- Compute: ML extraction over ~3,000 pages is slow on GitHub-hosted runners
  (2 vCPU, 6h cap). Start there with sharding; spin up private runners of proper
  config if we hit timeouts or usage limits. The image runs unchanged on either;
  only the runner label changes.
- Determinism: ML extractors drift across versions. Pin tool + model versions
  and record them in `pagemap` / `manifest`.
- Hard tables: merged-cell command tables degrade in Markdown. The JPEG page
  stays the visual authority and Tier C is the escape hatch.

## Stage 2: indexing (Markdown -> search index)

Engine: SQLite FTS5. Single file -> trivially baked into the mcp-server image,
BM25 ranking, no runtime services, custom tokenizer support. Implemented in
`data-extraction-docker/indexing/`.

- Tokenizer is the make-or-break detail. Default tokenizers shatter `ESC/POS`,
  `GS ( L`, hex `1B 40` on punctuation and destroy findability. Plan: dual
  indexing - a `unicode61` index with extended token characters to keep command
  symbols intact (ranked search) plus a `trigram` index for substring/symbol
  recall ("not missing anything").
- Schema: page-level docs `{stem, vendor, doc, page, heading_path, body,
  summary}` plus a doc-level table for `list_documents` / summaries. Store enough
  to render snippets and resolve JPEG URLs via `pagemap`.
- Summaries: per-doc "what devices/technologies it covers", generated
  extractively (no LLM), ASCII-clean, stored in the index and searchable.
- `manifest.json` records builder version, params, doc/page counts, checksums.
- Eval harness: a fixed query set with expected pages measures recall/precision.
  It validates the index and lets us compare index types objectively later.

## Stage 3: MCP server

Python 3.13. Implemented in `mcp-server/`.

- Framework: official Python MCP SDK / FastMCP over streamable HTTP (works on
  Render; gives an HTTP surface for static assets and the landing page).
- Tools: `list_documents()`, `get_document_summary(stem)`,
  `search_specs(query, vendor?, k?, neighbors?)`, `get_page(stem, page)`, and
  `get_page_image(stem, page, size?)` - the last returns the rendered page as MCP
  image content (base64) so a vision-capable client can see figures/diagrams the
  Markdown cannot convey (search/get_page only return image URLs). `stem` is the
  vendor-rooted path without extension, e.g. `star/star_graphic_cm_en`.
- Static serving: `/static/jpeg/...` and `/static/md/...`. When
  `DOCS_STATIC_BASE_URL` is set the server returns CDN URLs and does not serve
  static itself; when unset it self-serves and returns relative URLs. Switching
  to a CDN is exactly that one env var - no rebuild.
- Landing page (`/`) for robots and guests: corpus overview, vendor/doc list,
  version, how to connect. Plus `/healthz` and `/version`.
- "Swagger-like UI": there is no literal OpenAPI/Swagger for MCP tools, so we
  auto-generate an HTML tool catalog at `/docs` from the registered tools' JSON
  schemas, and point to the official MCP Inspector for live interaction.
- Logging only, never print. Thorough: every tool call (args, result counts,
  timing), index load, static hits. Level via env.
- `version.py` holds `__version__`, surfaced on the landing page and `/version`.
- ASCII only. No emojis anywhere.

### Two image variants (same Dockerfile, build target/arg)

- `mcp-server:<ver>` (lean): application + search index baked, no static files.
  Static comes from a mounted volume or a CDN (`DOCS_STATIC_BASE_URL`). This is
  the future CDN target.
- `mcp-server:<ver>-stuffed`: additionally bakes md, md-bulk, and jpegs. Fully
  self-contained - serves static by itself, or uses a CDN if
  `DOCS_STATIC_BASE_URL` is configured.

Both load the same baked index; the only difference is whether static assets are
inside the image.

## Artifacts and CI/CD

- Storage: Git LFS. `.gitattributes` tracks `*.jpg` and the FTS5 `*.db`;
  markdown/json stay as normal git text. Caveat: GitHub LFS has storage and
  bandwidth quotas and the mcp-server build pulls LFS objects on checkout; if we
  hit the bandwidth ceiling, that is the trigger to move static to a CDN (already
  the planned direction). Requires `git lfs install` locally and in CI before the
  first binary commit.
- Pipeline order: extraction -> indexing -> image build (both variants) ->
  deploy (Render). Implemented as three workflows chained with `workflow_run`
  (which fires even for GITHUB_TOKEN commits, unlike `push`), each with a
  concurrency group and LFS checkout:
  - `extract.yml` - manual (`workflow_dispatch`); inputs choose the phase and
    scope (all / one stem). Builds the extraction image (buildx + gha cache),
    runs the phase, commits outputs to LFS. Single job for now; if a run hits the
    6h cap, escalate to a private runner or dispatch per-stem (doc-level matrix
    fan-in with an artifact collect step is the documented next step).
  - `index.yml` - auto after a successful Extract (plus path-push and dispatch);
    builds the index, runs the eval gate (`evaluate --min-recall`), commits the
    index to LFS.
  - `build-mcp-server.yml` - auto after a successful Index (plus push to
    `mcp-server/**` and dispatch); builds + pushes `:<ver>` and `:<ver>-stuffed`
    to GHCR, then triggers a Render deploy if `RENDER_DEPLOY_HOOK_URL` is set.
- Version: image tags come from each component's `version.py` (`__version__`).
  Bump it to publish a new tag; `:latest` / `:latest-stuffed` always move.

## Pagemap contract

`data-extraction/pagemap/<vendor>/<doc>.json`, validated against
`data-extraction/pagemap/schema.json`. One record per document; one entry per
page tying together the page number, its markdown slice, both JPEG renders, the
extraction method used, and its quality score. This is the only authority for
page<->artifact mapping; downstream code reads it instead of recomputing paths.

## Open / deferred

- Vector index under `index/vector/` for later comparison.
- VLM Tier C enabled once private runners exist.
- CDN cutover (set `DOCS_STATIC_BASE_URL`) once LFS bandwidth or image size
  warrants it.

## Sequenced action items

1. Scaffold `data-extraction/` (outputs) and `data-extraction-docker/`
   (extraction, indexing); add `.gitattributes` (LFS); define the pagemap
   contract. [in progress]
2. Extraction image: Docling + OCR + JPEG render + QA + flagged-page report;
   manifest-driven and shardable; validate on a golden sample.
3. Full extraction run via sharded matrix workflow -> commit md + jpeg to LFS;
   manual review of flagged pages only.
4. Indexing image: SQLite FTS5 dual tokenizer, extractive summaries,
   `manifest.json`, eval harness.
5. mcp-server rewrite: FastMCP HTTP, the four tools, static serving, landing +
   `/docs`, logging-only/ASCII-only, `version.py`; Dockerfile producing both
   `:<ver>` and `:<ver>-stuffed`.
6. Wire workflows: extraction (matrix) -> indexing -> image build (both
   variants) -> Render deploy, ordered via `needs:` / `workflow_run`, with LFS
   checkout.
7. Backfill the TBD README sections as each stage lands.
