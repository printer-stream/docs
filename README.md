# docs

Machine-readable renders of printer/device specification PDFs, intended as a
data source for AI tools (search, RAG, and an MCP server).

## What's here

Each source PDF lives under `pdf/<vendor>/<doc>.pdf`. On push, GitHub Actions
generate aligned text and image artifacts (keyed by the vendor-rooted stem
`<vendor>/<doc>`, i.e. the source path with the leading `pdf/` stripped):

| Path | Contents | Tool |
|------|----------|------|
| `md-bulk/<vendor>/<doc>/README.md` | Full-document Markdown (one file) | pymupdf4llm |
| `md/<vendor>/<doc>/page-NN.md` | Per-page Markdown slices | pymupdf4llm |
| `jpeg/<vendor>/<doc>/small/page-NN.jpg` | ~1024px page previews | poppler `pdftoppm` |
| `jpeg/<vendor>/<doc>/big/page-NN.jpg` | Full-resolution page renders | poppler `pdftoppm` |

`page-NN` is zero-padded to the width of the document's page count, so a
`md/.../page-07.md` slice corresponds exactly to `jpeg/.../small/page-07.jpg`.
That 1:1 text↔image mapping is what lets the search/MCP layer cite a page and
show its render.

## Workflows

- `.github/workflows/pdf-to-markdown.yml` — Markdown extraction (bulk + per-page).
- `.github/workflows/pdf-to-jpeg.yml` — JPEG page renders.

Both share a `concurrency` group and rebase before pushing, so they never
collide on `main` even when triggered by the same PDF push.

## Text extraction tooling

We currently use **[pymupdf4llm](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)**
(PyMuPDF) because it emits per-page Markdown, keeps tables readable, and is
pure-pip (no system dependencies). It does **not** OCR scanned/image-only PDFs.

Alternatives kept on hand for future needs:

| Tool | Output | Tables | OCR / scanned | Notes |
|------|--------|--------|---------------|-------|
| **pymupdf4llm** (current) | Markdown, per-page | Good | No | Fast, CPU-only, pip install |
| **Docling** (IBM) | Markdown + JSON | Excellent | Yes (built-in) | Strong structure, heavier deps |
| **Marker** | Markdown | Very good | Yes | High quality, prefers a GPU |
| **MinerU** | Markdown / JSON | Excellent | Yes | Great for formulas / scientific docs |
| **pdftotext** (poppler) | Plain text | Poor | No | Original tool; fast but mangles tables |
| **ocrmypdf** + Tesseract | (PDF pre-pass) | — | Yes | Add an OCR text layer before extraction |

For scanned PDFs, run an `ocrmypdf` pre-pass to add a text layer, then extract
as usual.
