# Printer Stream Docs - MCP server

A Model Context Protocol server that lets AI tools (GitHub Copilot, Claude,
etc.) search the printer/device specification corpus in this repo and ground
answers in the exact page text and image.

## How it works

1. PDF file(s) pushed
2. Rendering starts: markdown per-page, markdown bulk, JPEG
3. Index is built
4. MCP Server Docker image is built
5. MCP Server is deployed

- **Text↔image alignment:** every page is `md/<doc>/page-NN.md` paired with
  `jpeg/<doc>/{small,big}/page-NN.jpg`. Search results carry image URLs for the
  hit page and the pages around it.
- **Full-text search:** keyword search over page bodies, headings, and summaries.
- **Summaries:** each document gets an extractive "what devices/technologies it
  covers" blurb, exposed via `get_document_summary` and searchable.

## Tools

| Tool | Purpose |
|------|---------|
| `list_documents()` | All docs with vendor, title, page count |
| `get_document_summary(stem)` | What devices/technologies a doc covers |
| `search_specs(query, vendor?, k?, neighbors?)` | Ranked page results with snippet, image URLs, and neighbouring-page images |
| `get_page(stem, page)` | Full page Markdown + image URLs |

`stem` is the repo-relative path without extension, e.g. `star/star_graphic_cm_en`.

Page images are returned as URLs built from `DOCS_STATIC_BASE_URL` (e.g. a CDN);
when it is unset the server serves them itself under `/static/...` and returns
relative URLs (`DOCS_BASE_URL`).

## Build the index

TBD

## Run locally

TBD

## Validation

TBD

## Measuring search quality

TBD

## Deploy on Render

Currently we use render.com with a manual deployment via a docker image.

### Connect from VS Code / Copilot

TBD

### Validate results from VS Code / Copilot

TBD
