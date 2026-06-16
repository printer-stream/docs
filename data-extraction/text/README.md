# text (intermediate)

Raw PDF text-layer slices, one per page, produced by the `text` phase.

```
<vendor>/<doc>/page-NN.txt
```

Kept as an intermediate for troubleshooting: it is the cheap baseline the
`quality` phase compares Docling's markdown against (text-layer agreement) and
the signal used to classify each page's `source` (text-layer vs ocr). Empty files
mean an image-only page. Normal git text (not LFS).
