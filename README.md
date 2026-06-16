# docs

Machine-readable renders of printer/device specification PDFs, intended as a
data source for AI tools (full-text search and an MCP server).

The pipeline is being rebuilt from scratch; **[DESIGN.md](DESIGN.md)** is the
source of truth for the architecture and decisions.

## What's here

Each source PDF lives under `pdf/<vendor>/<doc>.pdf`. The pipeline turns it into
aligned text and image artifacts under `data-extraction/`, keyed by the
vendor-rooted stem `<vendor>/<doc>` (the source path with `pdf/` stripped):

| Path                                                       | Contents                          |
|------------------------------------------------------------|-----------------------------------|
| `data-extraction/markdown/<vendor>/<doc>/document.md`      | Full-document Markdown (one file)  |
| `data-extraction/markdown/<vendor>/<doc>/page-NN.md`       | Per-page Markdown slices           |
| `data-extraction/jpeg/<vendor>/<doc>/small/page-NN.jpg`    | ~1024px page previews              |
| `data-extraction/jpeg/<vendor>/<doc>/big/page-NN.jpg`      | Full-resolution page renders       |
| `data-extraction/pagemap/<vendor>/<doc>.json`              | Authoritative page<->artifact map  |
| `data-extraction/quality/<vendor>/<doc>.json`             | Per-page extraction QA metrics     |
| `data-extraction/index/<type>/`                            | Pre-generated search index(es)     |

`page-NN` is zero-padded to the width of the document's page count, so
`markdown/.../page-07.md` corresponds exactly to `jpeg/.../small/page-07.jpg`.
That 1:1 text-to-image mapping is what lets the search/MCP layer cite a page and
show its render. The mapping is recorded in `pagemap/<vendor>/<doc>.json`
(authoritative), so downstream code never relies on filename math.

## Structure

```
pdf/                    source PDFs (pdf/<vendor>/<doc>.pdf)
data-extraction/        static outputs only (binaries via Git LFS)
data-extraction-docker/ build code: extraction/ and indexing/ Docker images
mcp-server/             Python 3.13 MCP server (serves the corpus + search)
```

Code and static outputs are kept strictly separate: build code never lives in
`data-extraction/`, and outputs never live in `data-extraction-docker/`.

## Pipeline

1. PDF pushed under `pdf/`
2. Extraction (discrete phases, see below)
3. Indexing: full-text search index built from the Markdown
4. MCP server image built (`:<ver>` lean and `:<ver>-stuffed`) and deployed

Indexing and the image build are downstream of extraction and must wait for it.
This is wired in `.github/workflows/`: `extract.yml` (manual, heavy) ->
`index.yml` (auto after extract, with an eval gate) -> `build-mcp-server.yml`
(auto after index; builds the lean + stuffed images, pushes to GHCR, optional
Render deploy). Stages are chained with `workflow_run` and all check out Git LFS.
See [DESIGN.md](DESIGN.md).

### Extraction phases

Extraction is split into functionally singular phases rather than one opaque
pass, so each can be re-run, swapped, or extended independently, and intermediate
data is kept for troubleshooting (e.g. analysing where quality dropped). All
phases share one image (`data-extraction-docker/extraction/`).

| Phase | Input | Output |
|-------|-------|--------|
| `render`   | pdf           | `data-extraction/jpeg/<stem>/{small,big}/page-NN.jpg` |
| `text`     | pdf           | `data-extraction/text/<stem>/page-NN.txt` |
| `markdown` | pdf           | `data-extraction/markdown/<stem>/page-NN.md` |
| `quality`  | markdown+text | `data-extraction/quality/<stem>.json` |
| `assemble` | all the above | `data-extraction/pagemap/<stem>.json` + `document.md` + reports |

Principles:

- **All-or-none per (phase, document):** a phase regenerates its whole artifact
  kind for a document; there is no per-page resume state. Restart a phase to redo
  it, or insert a new phase (e.g. a VLM `describe` step) between existing ones.
- **Data + meta:** every phase writes `data-extraction/meta/<stem>/<phase>.json`
  with tool, version, params, start/end, total + per-page timing, and status.
  `assemble` folds a summary into the pagemap's `phases` field, so timing and
  quality lineage live with the results.

## Artifacts and Git LFS

`data-extraction/jpeg/**/*.jpg` and `data-extraction/index/**/*.db` are tracked
via Git LFS (see `.gitattributes`); Markdown and JSON stay as normal git text.
Run `git lfs install` once before committing binary artifacts.

## Tooling (see DESIGN.md for detail)

- **Text extraction:** Docling (layout-aware Markdown) with OCR fallback and a
  gated VLM tier for pages that fail quality checks. Quality is verified per page
  and flagged pages get a side-by-side review report.
- **Search index:** SQLite FTS5 with a tokenizer tuned to keep symbol-heavy
  command tokens findable (`ESC @`, `GS ( L`, hex `1B 40`). Full-text/keyword
  now; the `index/<type>/` layout leaves room to add and compare a vector index
  later.
