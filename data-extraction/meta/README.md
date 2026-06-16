# meta (phase metadata)

Per-document, per-phase metadata emitted by every extraction phase.

```
<vendor>/<doc>/render.json
<vendor>/<doc>/text.json
<vendor>/<doc>/markdown.json
<vendor>/<doc>/quality.json
<vendor>/<doc>/assemble.json
```

Each records the tool + version + params, start/end timestamps, total duration,
per-page timing, page count, and status. Kept as part of the results so we can
monitor where time and quality went (e.g. which pages were slow or flagged). The
`assemble` phase folds a compact summary of these into the pagemap's `phases`
field. Normal git text (not LFS).
