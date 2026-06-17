# extraction image

One image, run as a sequence of discrete **phases**. Each phase produces a single
kind of artifact for a whole document (all-or-none) and records its own timing +
metadata, so phases can be re-run, swapped, or have new ones inserted between them
independently. See `../../DESIGN.md`.

| Phase | Input | Output |
|-------|-------|--------|
| `render`   | pdf            | `data-extraction/jpeg/<stem>/{small,big}/page-NN.jpg` |
| `text`     | pdf            | `data-extraction/text/<stem>/page-NN.txt` (raw text layer) |
| `markdown` | pdf            | `data-extraction/markdown/<stem>/page-NN.md` (Docling; slow) |
| `quality`  | markdown+text  | `data-extraction/quality/<stem>.json` |
| `describe` | jpeg + quality | `data-extraction/describe/<stem>/page-NN.txt` (VLM; optional) |
| `assemble` | all the above  | `data-extraction/pagemap/<stem>.json`, `document.md`, reports |

Every phase also writes `data-extraction/meta/<stem>/<phase>.json` (tool, version,
params, start/end, duration, per-page timing, status). `assemble` folds a summary
of those into the pagemap's `phases` field.

The `describe` phase is optional and off by default (not part of `all-phases`). It
gives pages a VLM-written description so figures the markdown can't convey (e.g. a
wiring schematic) become searchable. `--gate` selects which pages:

- `illustrated` (default) - pages with a figure (`<!-- image -->`) plus
  flagged/empty pages. A text-rich page can still hide a diagram the text never
  describes, so flagged/empty alone is not enough.
- `flagged` - only quality-flagged + image-only/empty pages (cheapest).
- `all` - every page.

It needs any OpenAI-compatible vision endpoint - a local model (Ollama, vLLM) or a
hosted one:

```bash
# Endpoint/model/key default from DESCRIBE_BASE_URL / DESCRIBE_MODEL / DESCRIBE_API_KEY.
# Local via Ollama (no GPU needed; Metal on macOS):
docker run --rm -v "$PWD":/work \
  -e DESCRIBE_BASE_URL=http://host.docker.internal:11434/v1 \
  -e DESCRIBE_MODEL=qwen2.5vl -e DESCRIBE_API_KEY=ollama \
  printer-stream-extraction describe --all          # --gate illustrated (default)
# or a GPU box with vLLM: DESCRIBE_BASE_URL=http://<host>:8000/v1 DESCRIBE_MODEL=Qwen/Qwen2.5-VL-7B-Instruct
# then re-run assemble so the pagemap references the new descriptions:
docker run --rm -v "$PWD":/work printer-stream-extraction assemble --all
```

## Build

```
docker build -t printer-stream-extraction data-extraction-docker/extraction
```

## Run

From the repo root (mounts the repo so outputs land in `data-extraction/`).
Each phase takes a scope: `--all`, `--stem <vendor/doc>`, or
`--shard-index i --shard-count n`.

```bash
# All phases over the whole corpus (render -> text -> markdown -> quality -> assemble)
docker run --rm -v "$PWD":/work printer-stream-extraction all-phases --all

# A single phase over one doc (e.g. just re-render JPEGs)
docker run --rm -v "$PWD":/work printer-stream-extraction render --stem star/star_graphic_cm_en

# Just re-run the markdown (slow) phase, sharded across N CI runners
docker run --rm -v "$PWD":/work printer-stream-extraction markdown --shard-index 0 --shard-count 4

# Re-run only quality + assemble after tweaking the gate (cheap, no Docling)
docker run --rm -v "$PWD":/work printer-stream-extraction quality --all --quality-threshold 0.55
docker run --rm -v "$PWD":/work printer-stream-extraction assemble --all

# Manifest for the CI matrix; corpus QA report
docker run --rm -v "$PWD":/work printer-stream-extraction manifest
docker run --rm -v "$PWD":/work printer-stream-extraction report
```

Mount a model cache to avoid re-downloading Docling models each run:
`-v "$HOME/.cache/printer-stream-models":/models`.

## Re-running and sharding

The atomic unit is (phase, document): a phase regenerates its artifact kind for
each document it is given, in full. To redo work, re-run the phase - there is no
per-page resume state to reason about ("all or none artifacts of the same kind").
Because phases are decoupled, you can re-run only the cheap phases (quality,
assemble) after a gate change without re-running Docling, or swap the `markdown`
phase implementation without touching renders.

Sharding is doc-level: each shard runs the phase over a subset of whole
documents. Page-level distribution of one huge doc across runners would need a
merge step and is intentionally out of scope for now; the trigger to add it (or
to move to private runners) is the two large docs timing out on GitHub-hosted
runners.
