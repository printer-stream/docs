# quality

Quality-assurance artifacts emitted by the extraction image.

```
<vendor>/<doc>.json   # per-page QA metrics
report.html           # side-by-side review of flagged pages only
```

Per-page metrics include char/alnum ratio, a dictionary hit-rate (gibberish
detector), OCR-vs-text-layer agreement, table-cell counts, control-char/symbol
preservation, and domain token checks (ESC/POS mnemonics, HPGL pen commands). A
confidence gate marks low-scoring pages as `flagged` in the pagemap; the HTML
report renders the source JPEG next to the extracted Markdown for those pages so
review is bounded to the suspect minority. See `../../DESIGN.md`.
