# pagemap

The authoritative page<->artifact map, one JSON file per document at
`<vendor>/<doc>.json`, validated against `schema.json`.

Each file ties every page number to its markdown slice, both JPEG renders, the
extraction method used (text-layer / ocr / vlm), and a quality score. Downstream
stages (indexing, mcp-server) read this instead of recomputing paths from
filename math, so changes to padding or naming never silently break the mapping.
