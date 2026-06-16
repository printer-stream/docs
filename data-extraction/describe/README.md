# describe (intermediate, optional)

Reserved for the optional `describe` phase: per-page natural-language
descriptions of the rendered JPEGs, produced by a vision model (local VLM or a
cheap hosted API).

```
<vendor>/<doc>/page-NN.txt
```

Purpose: give image-only / figure-heavy / low-text pages a searchable text
surface the keyword index can see, improving recall. These are a clearly
separate, supplementary signal - never merged into the authoritative
`../markdown/` slices - and are indexed at a lower weight. Off by default; see
`../../DESIGN.md`. Normal git text (not LFS).
