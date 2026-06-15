# docs

Machine-readable renders of printer/device specification PDFs, intended as a
data source for AI tools (search, RAG, and an MCP server).

## What's here

Each source PDF lives under `pdf/<vendor>/<doc>.pdf`. On push, GitHub Actions
generate aligned text and image artifacts (keyed by the vendor-rooted stem
`<vendor>/<doc>`, i.e. the source path with the leading `pdf/` stripped):

| Path                                    | Contents                             | Tool |
|-----------------------------------------|--------------------------------------|------|
| `md-bulk/<vendor>/<doc>/README.md`      | Full-document Markdown (one file)    | To be defined |
| `md/<vendor>/<doc>/page-NN.md`          | Per-page Markdown slices             | To be defined |
| `jpeg/<vendor>/<doc>/small/page-NN.jpg` | ~1024px page previews                | To be defined |
| `jpeg/<vendor>/<doc>/big/page-NN.jpg`   | Full-resolution page renders         | To be defined |

`page-NN` is zero-padded to the width of the document's page count, so a
`md/.../page-07.md` slice corresponds exactly to `jpeg/.../small/page-07.jpg`.
That 1:1 text-to-image mapping is what lets the search/MCP layer cite a page and
show its render. We probably need to additionally keep a mapping json file
in `./index/md-to-jpeg-pagemap.json` just to have a source of truth, and keep
away from the assumptions.

## Workflows

- `.github/workflows/pdf-to-markdown.yml` — Markdown extraction (bulk + per-page).
- `.github/workflows/pdf-to-jpeg.yml` — JPEG page renders.

Both share a `concurrency` group and rebase before pushing, so they never
collide on `main` even when triggered by the same PDF push.

Markdown and JPEG extraction must be waited upon by any logically downstream
procedures like index rebuild and such.

## Text extraction tooling

To be defined.

We need to keep a high quality of the markdown so the meaning was preserved.

Consider using OCR over the JPEGs if that would improve the yeilded result.

## Search index

At this point we need to stick to a full text / keyword search.
Later we'll add embeddings and vector search as well.
