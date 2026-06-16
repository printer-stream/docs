# jpeg

Per-page JPEG renders of the source PDFs, produced by the extraction image.

```
<vendor>/<doc>/small/page-NN.jpg   # ~1024px-wide previews
<vendor>/<doc>/big/page-NN.jpg     # full-resolution renders
```

`page-NN` is zero-padded to the document's page-count width and pairs 1:1 with
`../markdown/<vendor>/<doc>/page-NN.md`. Files are tracked via Git LFS.
