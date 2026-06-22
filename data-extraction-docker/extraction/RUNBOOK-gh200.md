# Runbook: full extraction on a GH200 (Grace Hopper, 96 GB)

The GH200 is a Hopper GPU (FP8) + ARM64 Grace CPU. Use the **`h200` profile** as-is
(Hopper = FP8, so `Qwen3-VL-32B-Instruct-FP8` loads natively). The throughput
lever is **`concurrency`** (page requests kept in flight so vLLM batches them);
the `h200` profile sets it to 16 on the VLM phases. See `README.md` for the phase
contract and `profiles/h200.toml` for the model wiring.

## 0. Prereqs (ARM64!)

```bash
git clone <repo> && cd docs && git lfs install && git lfs pull   # need pdf/
# Build the images for ARM64 (Grace is aarch64). The extraction container is
# CPU-only here (it renders PDFs + calls the vLLM HTTP endpoint); the GPU work is
# in vLLM. If buildx for arm64 is awkward, just run the extractor in a venv.
docker buildx build --platform linux/arm64 -t printer-stream-extraction data-extraction-docker/extraction
docker buildx build --platform linux/arm64 -t printer-stream-indexing  data-extraction-docker/indexing
nvidia-smi
```

## 1. Serve the model (FP8, batching on)

```bash
pip install "vllm>=<ver-with-qwen3-vl>"        # use NVIDIA's GH200/arm64 build
export VLLM_API_KEY=x
vllm serve Qwen/Qwen3-VL-32B-Instruct-FP8 --port 8000 \
  --enable-prefix-caching \      # our prompt prefix is identical every call
  --max-num-seqs 32              # >= the profile's concurrency (16); raise to push harder
```
Smoke test: `curl -s localhost:8000/v1/models` and a 1-line vision completion.
Watch `nvidia-smi`: ~33 GB resident, leaving ~60 GB for KV cache.

> Quality first: 32B-FP8 is the best model that fits one 96 GB GPU, so keep it -
> do not downgrade to a smaller/faster model for speed (throughput comes from
> concurrency). If you want higher precision and have headroom, run the same model
> in BF16 (`Qwen/Qwen3-VL-32B-Instruct`, ~64 GB) - the only step up that fits.

## 2. Dry run on ONE document — the gate before the corpus

```bash
RUN="docker run --rm --network host -e VLLM_API_KEY=x -v $PWD:/work printer-stream-extraction --profile h200"
$RUN all-phases --stem star/star_graphic_cm_en      # render→text→markdown→quality→sections→assemble
$RUN describe   --stem star/star_graphic_cm_en
$RUN assemble   --stem star/star_graphic_cm_en      # re-fold describe into the pagemap
```
`--network host` lets the container reach vLLM on `localhost:8000`. **Verify:**
- **markdown faithfulness** — diff a command-table page's `.md` against its `.jpg`:
  exact commands/hex, intact tables, `<!-- figure: ... -->` notes, no invented commands.
- **throughput** — `meta/star/star_graphic_cm_en/markdown.json` → `per_page_seconds_avg`.
  **Multiply by 2808 for the corpus markdown estimate.** Tune: raise/lower
  `[markdown] concurrency` (and vLLM `--max-num-seqs`) and re-run one doc to find the knee.
- vlm-judge flags + reasons on figure pages; `sections/<stem>.json` page_labels look right.

Do not proceed unless faithfulness is good. Fallback if needed (same image, one flag):
`--profile cheap-gpu` (8B) or `--profile default` (Docling, no GPU).

## 3. Full corpus

```bash
$RUN all-phases --all          # 2808 pages; markdown is the long pole
$RUN describe   --all          # illustrated gate (figure pages)
$RUN assemble   --all
```
Watch the corpus page counter in the logs and `nvidia-smi` (should stay busy, not idle).

## 4. Index + eval

```bash
docker run --rm -v "$PWD":/work printer-stream-indexing build
docker run --rm -v "$PWD":/work printer-stream-indexing evaluate --unit section --k 10
docker run --rm -v "$PWD":/work printer-stream-indexing evaluate --unit page    --k 10
```
Confirm doc-hit recall holds (gate 0.8) and the figure queries improve: `GS / bit image`
(escpos page-090) and the HP 7475A p153 Y-cable schematic (`hp/FFONS49JUMXQZJH`).

## 5. Ship

```bash
git add data-extraction && git commit -m "Re-extract corpus with Qwen3-VL (h200/GH200)"
git pull --rebase origin main && git push      # CI reindexes, builds 2.5.0 images, redeploys
```

## Time + cost estimate (GH200 @ $1.99/hr)

2808 pages; `markdown` dominates and is the main uncertainty — calibrate with the
dry run. With `concurrency=16` + prefix caching:

| Step | Estimate |
|------|----------|
| Setup (arm64 build + 33 GB model download + vLLM warmup) | ~30-45 min (one-time) |
| render + text (CPU) | ~15 min |
| **markdown** (VLM, 32B-FP8, conc 16) | **~1-1.5 h** (the long pole) |
| quality (vlm-judge, figure pages, conc 16) | ~10-20 min |
| sections (headings, deterministic) | seconds |
| describe (illustrated subset, conc 16) | ~15-30 min |
| assemble + index + eval | ~5-10 min |
| **End-to-end** | **~2-3 h → ~$4-6** |

For contrast, **without** the concurrency tweak (one request at a time, the old
default) markdown alone is ~9 h with the GPU mostly idle → ~$18+ and ~7 h wasted.
That single knob is the difference.

## Speed levers (tune for total time, not cost)

These speed up the run **without touching output quality** (we keep dense 32B-FP8
and full 300-dpi renders - do not trade faithfulness for time):

1. **Saturate the GPU** - the dominant lever. Raise `concurrency` (16 -> 24 -> 32)
   and vLLM `--max-num-seqs` to match; stop when `per_page_seconds_avg` (in the
   markdown meta) stops dropping. The spare ~60 GB VRAM is KV-cache room for a
   bigger batch, not a reason to shrink the model. Diagnose with `nvidia-smi`:
   util >85% = GPU-bound (good).
2. **Hide the model load under render** - the model download + warmup is ~15-30 min
   of idle GPU. Start `render --all` (CPU-only) *while* `vllm serve` loads, and run
   phases corpus-wide rather than per-doc `all-phases` so the GPU stays continuously
   busy during markdown instead of stop-starting per document:
   ```bash
   vllm serve ... &              # loads the model (minutes)
   $RUN render --all             # CPU; overlaps the load for free
   $RUN text --all
   $RUN markdown --all           # GPU now hot, runs uninterrupted
   $RUN quality --all; $RUN describe --all; $RUN sections --all; $RUN assemble --all
   ```
3. **`--enable-prefix-caching`** - free; caches the identical prompt prefix.

Quality note: the obvious "speed" knobs that would cost quality - a smaller/faster
model (e.g. 30B-A3B) or a lower render dpi (fewer vision tokens) - are deliberately
**not** used here. Throughput comes from concurrency + batching, which leave the
output identical. If anything, spend spare headroom on quality (32B in BF16).

**Not worth it: a ramdisk / tmpfs.** The pipeline is compute-bound, not I/O-bound:
~1 GB of JPEGs over a multi-hour run is a few MB/s vs NVMe's ~GB/s, a page read is
~0.1 ms vs a ~1-2 s VLM call, and the Linux page cache (480 GB RAM) already serves
the just-written JPEGs from memory. A ramdisk would duplicate the page cache for
no measurable gain.
