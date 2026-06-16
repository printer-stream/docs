# data-extraction-docker (build code)

Docker build contexts for the pipeline stages that produce the static artifacts
in `../data-extraction/`. Code lives here; outputs never do.

```
extraction/   PDF -> jpeg + markdown + pagemap + quality (Docling + OCR + render)
indexing/     markdown -> search index (SQLite FTS5) + manifest + eval
```

Each is an independently buildable/runnable Docker image, usable locally or in
CI. See `../DESIGN.md` for the design and `../data-extraction/` for the outputs
they write.
