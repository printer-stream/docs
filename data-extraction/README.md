# data-extraction (static outputs)

Generated artifacts only. No code lives here - build code is in
`../data-extraction-docker/`. See `../DESIGN.md` for the full design.

| Path         | Phase    | Contents                                             |
|--------------|----------|------------------------------------------------------|
| `jpeg/`      | render   | Per-page JPEG renders (`small/` previews + `big/`)    |
| `text/`      | text     | Raw PDF text-layer slices (intermediate)             |
| `markdown/`  | markdown | Per-page slices (`page-NN.md`) + bulk (`document.md`) |
| `describe/`  | describe | Optional VLM page descriptions (intermediate)        |
| `quality/`   | quality  | Per-page QA metrics + flagged-page review report      |
| `pagemap/`   | assemble | Source-of-truth page<->artifact map per doc          |
| `meta/`      | (all)    | Per-doc, per-phase timing + toolchain metadata       |
| `index/`     | -        | Pre-generated search index(es), one subdir per type  |

Extraction runs as discrete phases (render, text, markdown, [describe], quality,
assemble); each produces one artifact kind and its own `meta/<stem>/<phase>.json`.
See `../data-extraction-docker/extraction/` and `../DESIGN.md`.

Binaries (`*.jpg`, the FTS5 `*.db`) are stored via Git LFS; see
`../.gitattributes`. Run `git lfs install` once before committing them.

Layout key: `<vendor>/<doc>/...`, e.g. `star/star_graphic_cm_en/...`. `page-NN`
is zero-padded to the document's page-count width, and `page-NN.md` pairs 1:1
with `jpeg/.../page-NN.jpg`. The `pagemap/` JSON is authoritative - downstream
code reads it instead of recomputing paths.
