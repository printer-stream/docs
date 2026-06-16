# markdown

Markdown rendered from the source PDFs by the extraction image.

```
<vendor>/<doc>/page-NN.md     # per-page slices ("md")
<vendor>/<doc>/document.md    # full-document single file ("md-bulk")
```

Per-page slices pair 1:1 with `../jpeg/<vendor>/<doc>/{small,big}/page-NN.jpg`.
Both the per-page and bulk renders are baked into the `mcp-server:<ver>-stuffed`
image. Quality is the priority: command mnemonics, hex bytes, and table
structure must survive extraction (see `../quality/` and `../../DESIGN.md`).
