"""Measure search quality of the MCP server's full-text (FTS5) retrieval.

Strategy (self-supervised, no manual labels): for a sample of pages, derive a
query that the page should answer, run search_specs, and check where the source
page lands in the ranking. Reports recall@1/3/5, MRR@10, and query latency.

Query generation:
  - If OPENAI_API_KEY is set (or DOCS_EVAL_LLM=1 with a local OpenAI-compatible
    endpoint), an LLM writes a natural question per page -> realistic test of
    conceptual retrieval.
  - Otherwise, a no-LLM fallback builds queries from page headings / salient
    tokens -> weaker, but zero-dependency and good for regression checks.

Usage:
  python mcp-server/evaluate.py [--sample N] [--k 5] [--no-llm] [--seed 0]

Note: this calls search_specs() directly to isolate retrieval quality from the
HTTP transport. For transport/interactive testing use the MCP Inspector.
"""
from __future__ import annotations

import argparse
import logging
import random
import re
import time

import server  # reuses the same index + search_specs
from config import cfg
from corpus import discover_documents

try:
    from openai import OpenAI as _OpenAI  # type: ignore[import-untyped]
    _OPENAI_AVAILABLE = True
except ImportError:
    _OPENAI_AVAILABLE = False

log = logging.getLogger("printerrr-eval")

_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-]{3,}")
_STOP = {
    "the", "and", "for", "with", "this", "that", "from", "your", "are", "was",
    "page", "mode", "command", "specifications", "rev", "star", "line", "thermal",
    "printer", "section", "table", "contents", "figure", "note", "notes",
}


def llm_question(text: str) -> str | None:
    """Ask an LLM for one natural question answerable by this page."""
    if not (cfg.openai_api_key or cfg.eval_llm) or not _OPENAI_AVAILABLE:
        return None
    try:
        client = _OpenAI()  # honors OPENAI_API_KEY / OPENAI_BASE_URL
        resp = client.chat.completions.create(
            model=cfg.eval_model,
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You write one short, natural question that a developer "
                        "would ask, which THIS printer-spec page answers. Output "
                        "only the question."
                    ),
                },
                {"role": "user", "content": text[:3000]},
            ],
        )
        return resp.choices[0].message.content.strip()
    except Exception as exc:  # noqa: BLE001
        log.warning("LLM question generation failed (%s); using fallback", exc)
        return None


def fallback_query(text: str) -> str | None:
    """Build a query from salient terms when no LLM is available."""
    words = [w.lower() for w in _WORD_RE.findall(text)]
    salient: list[str] = []
    seen: set[str] = set()
    for w in words:
        if w in _STOP or w in seen:
            continue
        seen.add(w)
        salient.append(w)
        if len(salient) >= 6:
            break
    return " ".join(salient) if len(salient) >= 3 else None


def build_queries(sample: int, seed: int, use_llm: bool) -> list[tuple[str, str, int]]:
    """Return (query, stem, page_no) tuples for a sample of content pages."""
    rng = random.Random(seed)
    candidates = [
        (doc.stem, p.page_no, p.text)
        for doc in discover_documents()
        for p in doc.pages
        if len(p.text.strip()) > 200  # skip near-empty / cover pages
    ]
    rng.shuffle(candidates)

    queries: list[tuple[str, str, int]] = []
    for stem, page_no, text in candidates:
        if len(queries) >= sample:
            break
        q = (llm_question(text) if use_llm else None) or fallback_query(text)
        if q:
            queries.append((q, stem, page_no))
    return queries


def evaluate(sample: int, k: int, seed: int, use_llm: bool) -> None:
    server.warm_up()
    queries = build_queries(sample, seed, use_llm)
    if not queries:
        log.error("No queries could be built -- is the index populated?")
        return

    log.info("Evaluating %d query/page pair(s) (%s queries, k=%d)",
             len(queries), "LLM" if use_llm else "fallback", k)

    hits_at = {1: 0, 3: 0, 5: 0}
    rr_sum = 0.0
    latencies: list[float] = []
    failures: list[tuple[str, str, int]] = []

    for i, (query, stem, page_no) in enumerate(queries, start=1):
        t0 = time.perf_counter()
        results = server.search_specs(query, k=max(k, 10))
        latencies.append(time.perf_counter() - t0)

        rank = next(
            (idx for idx, r in enumerate(results, start=1)
             if r["stem"] == stem and r["page"] == page_no),
            None,
        )
        if rank is not None:
            rr_sum += 1.0 / rank
            for n in hits_at:
                if rank <= n:
                    hits_at[n] += 1
            log.debug("[%d] rank=%d  q=%r -> %s p%d", i, rank, query, stem, page_no)
        else:
            failures.append((query, stem, page_no))
            log.debug("[%d] MISS    q=%r -> expected %s p%d", i, query, stem, page_no)

    n = len(queries)
    lat = sorted(latencies)
    p50 = lat[len(lat) // 2]
    p95 = lat[min(len(lat) - 1, int(len(lat) * 0.95))]

    print("\n=== Search quality ===")
    print(f"queries          : {n}  ({'LLM' if use_llm else 'fallback'} generated)")
    print(f"recall@1         : {hits_at[1] / n:.3f}  ({hits_at[1]}/{n})")
    print(f"recall@3         : {hits_at[3] / n:.3f}  ({hits_at[3]}/{n})")
    print(f"recall@5         : {hits_at[5] / n:.3f}  ({hits_at[5]}/{n})")
    print(f"MRR@10           : {rr_sum / n:.3f}")
    print(f"latency p50 / p95: {p50 * 1000:.0f} ms / {p95 * 1000:.0f} ms")

    if failures:
        print(f"\n=== Misses ({len(failures)}) ===")
        for query, stem, page_no in failures[:15]:
            print(f"  expected {stem} p{page_no}: {query!r}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Evaluate MCP search quality")
    ap.add_argument("--sample", type=int, default=20, help="pages to sample")
    ap.add_argument("--k", type=int, default=5, help="cutoff for recall reporting")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--no-llm", action="store_true", help="force fallback queries")
    args = ap.parse_args()

    use_llm = (not args.no_llm) and bool(cfg.openai_api_key or cfg.eval_llm)
    evaluate(args.sample, args.k, args.seed, use_llm)


if __name__ == "__main__":
    main()
