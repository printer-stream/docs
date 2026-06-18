# sections

Logical document chunks produced by the `sections` phase, one JSON file per
document at `<vendor>/<doc>.json`.

A page is a print-media artifact; the logical unit for retrieval is the
section/command/topic, which may span pages. Each section records its title,
heading path, level, text, and the **page range** it covers (`page_start`,
`page_end`, `page_labels`) so retrieval can still cite and show the page renders.

Backends (selected by profile `[sections]`): `headings` (deterministic, splits on
Markdown headings; the default) and `llm-text` (a text LLM over the markdown with
page markers). The indexing stage consumes these to offer section-level search
(a follow-up round). See `../../DESIGN.md`.
