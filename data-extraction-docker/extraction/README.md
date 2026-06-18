# extraction image

One image, run as a sequence of discrete **phases**. Each phase produces a single
kind of artifact for a whole document (all-or-none) and records its own timing +
metadata, so phases can be re-run, swapped, or have new ones inserted between them
independently. Which engine/model each phase uses is not hard-coded - it comes
from the selected **profile** (`--profile`). See `../../DESIGN.md`.

| Phase | Input | Output | Backend (profile section) |
|-------|-------|--------|---------------------------|
| `render`   | pdf            | `data-extraction/jpeg/<stem>/{small,big}/page-NN.jpg` | - (`[render]`) |
| `text`     | pdf            | `data-extraction/text/<stem>/page-NN.txt` (raw text layer) | - |
| `markdown` | pdf            | `data-extraction/markdown/<stem>/page-NN.md` | `docling` \| `vlm` (`[markdown]`) |
| `quality`  | markdown+text  | `data-extraction/quality/<stem>.json` | `heuristic` \| `vlm-judge` (`[quality]`) |
| `describe` | jpeg + quality | `data-extraction/describe/<stem>/page-NN.txt` (optional) | VLM (`[describe]`) |
| `sections` | markdown       | `data-extraction/sections/<stem>.json` (logical chunks) | `headings` \| `llm-text` (`[sections]`) |
| `assemble` | all the above  | `data-extraction/pagemap/<stem>.json`, `document.md`, reports | - |

`all-phases` runs `render -> text -> markdown -> quality -> assemble` in order.
`describe` and `sections` are separate, opt-in phases (not in `all-phases`).

Every phase also writes `data-extraction/meta/<stem>/<phase>.json` (tool, version,
backend + model, params, start/end, duration, per-page timing, status). `assemble`
folds a summary of those into the pagemap's `phases` field, so the lineage of
*which backend/model produced each artifact* travels with the results.

## Profiles

A profile is a TOML file under `profiles/` selected with the global `--profile`
flag (name or path; default `default`). It sets each phase's backend, model, and
parameters in one place - swapping models is a profile edit, never a code change.

```bash
docker run ... printer-stream-extraction --profile h200 markdown --all
```

Secrets never live in profiles. A provider block names an **env var** to read the
key from (`api_key_env`); the value comes from the environment at run time:

```toml
[markdown]
backend = "vlm"
[markdown.provider]
base_url = "https://api.openai.com/v1"
model = "gpt-4o-mini"
api_key_env = "OPENAI_API_KEY"   # the key is read from $OPENAI_API_KEY, not stored
max_tokens = 4096
```

Selecting a backend that isn't registered (e.g. the planned `vlm-window` sections
backend) fails immediately with the list of available names.

### Built-in profiles (the downgrade matrix)

Same image, same artifacts, same contracts at every tier - only quality/cost and
where it runs change. Pick the lowest tier that meets your quality bar.

| Profile | Runs on | markdown | quality | describe | sections | Needs |
|---------|---------|----------|---------|----------|----------|-------|
| `default`   | shared GitHub runner, **no GPU, no network** | `docling` (local) | `heuristic` | off | `headings` | nothing |
| `hosted`    | shared runner, no GPU | `vlm` gpt-4o-mini | `heuristic` | on (gpt-4o-mini) | `llm-text` gpt-4o-mini | `OPENAI_API_KEY` (a few $ for the corpus) |
| `cheap-gpu` | a 24-48 GB local GPU (vLLM/Ollama) | `vlm` Qwen3-VL-8B | `heuristic` | on (8B) | `llm-text` Qwen3-VL-8B | a small GPU + `VLLM_API_KEY` (any value) |
| `h200`      | one big-VRAM CUDA GPU | `vlm` Qwen3-VL-32B-FP8 | `vlm-judge` (32B-FP8) | on (32B-FP8) | `llm-text` (32B-FP8) | an H200-class GPU + `VLLM_API_KEY` (any value) |

`default` is the floor: it reproduces the classic Docling + heuristic pipeline and
needs no GPU and no API key, so the corpus can always be rebuilt on a free runner.

## The pluggable backends

**markdown** - `docling` (layout-aware local conversion, the slow phase) or `vlm`
(transcribe the page image to Markdown via an OpenAI-compatible VLM; renders the
page in memory, so it doesn't depend on the `render` phase).

**quality** - `heuristic` (free, text-only metrics: coverage vs the text layer,
word-likeness, table/command/hex counts) or `vlm-judge`. `vlm-judge` keeps the
heuristic verdict everywhere, then on **figure pages only** (`<!-- image -->` /
`<!-- figure ... -->`) asks the VLM whether the Markdown faithfully captures the
page (image + Markdown in, `OK` or `MISSING: ...` out). On a miss it flags the
page, drops the score, and records the model's one-line reason - catching diagrams
the text silently drops (the heuristic scores an image-only page fine on
coverage). Figureless and not-yet-rendered pages make **zero** model calls, so the
cost is bounded to the pages that actually have figures.

**sections** - logical document chunks (a command/topic may span pages; a page is
a print-media artifact, not the retrieval unit). `headings` splits deterministically
on Markdown headings (carrying a heading path and the page range each section
covers); `llm-text` asks a text LLM to identify section boundaries over the
page-marked Markdown. Output is one `sections/<stem>.json` per document for
section-level retrieval (a later indexing round consumes it).

**describe** (optional, off in `all-phases`) - a supplementary VLM description so
figures the Markdown can't convey become searchable; the index treats it as a
separate, lower-signal field, never merged into the authoritative Markdown.
`--gate` (or `[describe].gate`) selects pages:

- `illustrated` (default) - pages with a figure placeholder plus flagged/empty
  pages. A text-rich page can still hide a diagram the text never describes, so
  flagged/empty alone is not enough.
- `flagged` - only quality-flagged + image-only/empty pages (cheapest).
- `all` - every page.

Gates are a registry: adding one is a single `@GATES.register("name")` function.

## Build

```
docker build -t printer-stream-extraction data-extraction-docker/extraction
```

## Run

From the repo root (mounts the repo so outputs land in `data-extraction/`).
Each phase takes a scope: `--all`, `--stem <vendor/doc>`, or
`--shard-index i --shard-count n`. `--profile` is global (before the phase).

```bash
# All phases over the whole corpus, default profile (Docling + heuristic, no GPU)
docker run --rm -v "$PWD":/work printer-stream-extraction all-phases --all

# Same, but VLM markdown + vlm-judge QA on an H200 box serving Qwen via vLLM
docker run --rm -v "$PWD":/work -e VLLM_API_KEY=x \
  printer-stream-extraction --profile h200 all-phases --all

# A single phase over one doc (e.g. just re-render JPEGs)
docker run --rm -v "$PWD":/work printer-stream-extraction render --stem star/star_graphic_cm_en

# Re-run only the markdown (slow) phase, sharded across N CI runners
docker run --rm -v "$PWD":/work printer-stream-extraction markdown --shard-index 0 --shard-count 4

# Re-run only the cheap phases after swapping a profile/gate (no Docling)
docker run --rm -v "$PWD":/work printer-stream-extraction quality --all
docker run --rm -v "$PWD":/work printer-stream-extraction assemble --all

# Optional describe over flagged+illustrated pages via a hosted model
docker run --rm -v "$PWD":/work -e OPENAI_API_KEY=sk-... \
  printer-stream-extraction --profile hosted describe --all     # --gate from profile
# then re-run assemble so the pagemap references the new descriptions
docker run --rm -v "$PWD":/work printer-stream-extraction assemble --all

# Logical sections (headings is deterministic and free; llm-text needs a provider)
docker run --rm -v "$PWD":/work printer-stream-extraction sections --all

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
assemble) after a profile/gate change without re-running the markdown phase, or
swap the `markdown` backend (docling <-> vlm) without touching renders.

Sharding is doc-level: each shard runs the phase over a subset of whole
documents. Page-level distribution of one huge doc across runners would need a
merge step and is intentionally out of scope for now; the trigger to add it (or
to move to private runners) is the two large docs timing out on GitHub-hosted
runners.
