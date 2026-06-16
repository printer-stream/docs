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
| `assemble` | all the above  | `data-extraction/pagemap/<stem>.json`, `document.md`, reports |

Every phase also writes `data-extraction/meta/<stem>/<phase>.json` (tool, version,
params, start/end, duration, per-page timing, status). `assemble` folds a summary
of those into the pagemap's `phases` field. A future `describe` phase
(jpeg -> VLM description) slots in before `quality`.

## Build

```
docker build -t printerrr-extraction data-extraction-docker/extraction
```

## Run

From the repo root (mounts the repo so outputs land in `data-extraction/`).
Each phase takes a scope: `--all`, `--stem <vendor/doc>`, or
`--shard-index i --shard-count n`.

```bash
# All phases over the whole corpus
docker run --rm -v "$PWD":/work printerrr-extraction run --all

# A single phase over one doc (e.g. just re-render JPEGs)
docker run --rm -v "$PWD":/work printerrr-extraction render --stem star/star_graphic_cm_en

# Just re-run the markdown (slow) phase, sharded across N CI runners
docker run --rm -v "$PWD":/work printerrr-extraction markdown --shard-index 0 --shard-count 4

# Re-run only quality + assemble after tweaking the gate (cheap, no Docling)
docker run --rm -v "$PWD":/work printerrr-extraction quality --all --quality-threshold 0.55
docker run --rm -v "$PWD":/work printerrr-extraction assemble --all

# Manifest for the CI matrix; corpus QA report
docker run --rm -v "$PWD":/work printerrr-extraction manifest
docker run --rm -v "$PWD":/work printerrr-extraction report
```

Mount a model cache to avoid re-downloading Docling models each run:
`-v "$HOME/.cache/printerrr-models":/models`.

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
