# index

Pre-generated search index(es), one subdirectory per index type so types can be
built and compared side by side.

```
fulltext/   # SQLite FTS5 (primary). Dual tokenizer: unicode61 + trigram.
vector/     # reserved for later embeddings/vector comparison
manifest.json   # builder version, params, doc/page counts, checksums
```

The fulltext index is built by `../../data-extraction-docker/indexing/` and baked
into both mcp-server image variants. The `*.db` file is tracked via Git LFS. The
tokenizer is tuned so symbol-heavy command tokens (`ESC @`, `GS ( L`, hex
`1B 40`) stay findable - see `../../DESIGN.md`.
