"""Search-quality eval harness.

Runs a fixed query set against the built index and reports, per query and in
aggregate, for the chosen retrieval unit (sections by default, pages as fallback):

  - doc hit: an expected document appears in the top-k -> recall_at_k (the CI
    gate metric; "did we surface the right document at all").
  - for page-labeled queries, graded metrics: precision@k, recall@k, MRR, nDCG@k.

Ground truth is page-level (eval/queries.json), so for the section unit a section
counts as relevant if it covers any relevant page; recall@k is page coverage (the
fraction of relevant pages covered by a retrieved section).

Ground truth per query:
  - "relevant": ["<stem>#<label>", ...]    page-level (preferred, enables graded metrics)
  - "expect_stem" + "expect_labels"         page-level (derived)
  - "expect_stem" only                      doc-level (contributes to doc-hit only)
"""

from __future__ import annotations

import json
import logging
import math
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Set

from .config import LOGGER_NAME, Settings
from .search import search_pages, search_sections

log = logging.getLogger(LOGGER_NAME)


def default_queries_path() -> Path:
    return Path(__file__).resolve().parent.parent / "eval" / "queries.json"


def _relevant_keys(item: Dict) -> Optional[Set[str]]:
    """Page-level ground truth as a set of '<stem>#<label>', or None (doc-level)."""
    if item.get("relevant"):
        return set(item["relevant"])
    stem, labels = item.get("expect_stem"), item.get("expect_labels")
    if stem and labels:
        return {"%s#%s" % (stem, lb) for lb in labels}
    return None


def _expected_stems(item: Dict) -> Set[str]:
    if item.get("relevant"):
        return {key.split("#", 1)[0] for key in item["relevant"]}
    if item.get("expect_stem"):
        return {item["expect_stem"]}
    return set()


def _dcg(flags: List[int]) -> float:
    return sum(f / math.log2(i + 1) for i, f in enumerate(flags, start=1))


def _result_flags(unit: str, results: List[Dict], rk: Set[str]) -> tuple:
    """Per-result relevance flags and the page-keys actually covered (top-k).

    Pages: a result is relevant if its '<stem>#<label>' is in rk.
    Sections: relevant if it covers any relevant page; 'covered' is the union of
    relevant page-keys across the results (so recall is page coverage)."""
    flags: List[int] = []
    covered: Set[str] = set()
    for r in results:
        if unit == "section":
            labels = json.loads(r.get("page_labels") or "[]")
            keys = {"%s#%s" % (r["stem"], lb) for lb in labels}
        else:
            keys = {"%s#%s" % (r["stem"], r["label"])}
        hit = keys & rk
        flags.append(1 if hit else 0)
        covered |= hit
    return flags, covered


def run_eval(settings: Settings, queries_path: Path, k: int = 10, unit: str = "section") -> Dict:
    queries = json.loads(queries_path.read_text(encoding="utf-8"))
    con = sqlite3.connect(str(settings.db_path))
    search_fn = search_sections if unit == "section" else search_pages
    total = len(queries)
    doc_hits = 0
    graded: List[Dict] = []
    details: List[Dict] = []

    for item in queries:
        q = item["query"]
        results = search_fn(con, q, k)
        exp_stems = _expected_stems(item)

        doc_hit = bool(exp_stems) and any(r["stem"] in exp_stems for r in results)
        doc_hits += 1 if doc_hit else 0

        rk = _relevant_keys(item)
        metrics: Optional[Dict] = None
        if rk:
            flags, covered = _result_flags(unit, results, rk)
            topk = flags[:k]
            hits = sum(topk)
            mrr = next((1.0 / i for i, f in enumerate(flags, start=1) if f), 0.0)
            ideal = [1] * min(len(rk), k)
            metrics = {
                "precision_at_k": round(hits / k, 4),
                "recall_at_k": round(len(covered) / len(rk), 4),
                "mrr": round(mrr, 4),
                "ndcg_at_k": round(_dcg(topk) / _dcg(ideal), 4) if ideal else 0.0,
            }
            graded.append(metrics)

        suffix = ""
        if metrics:
            suffix = " P@%d=%.2f R@%d=%.2f nDCG=%.2f MRR=%.2f" % (
                k, metrics["precision_at_k"], k, metrics["recall_at_k"],
                metrics["ndcg_at_k"], metrics["mrr"],
            )
        log.info("[%s] %-36s doc_hit=%s%s", "ok" if doc_hit else "MISS", q[:36], doc_hit, suffix)
        details.append({"query": q, "doc_hit": doc_hit, "metrics": metrics})

    con.close()

    def _mean(key: str) -> Optional[float]:
        return round(sum(g[key] for g in graded) / len(graded), 4) if graded else None

    recall_at_k = round(doc_hits / total, 4) if total else 0.0
    summary = {
        "total": total,
        "k": k,
        "unit": unit,
        "recall_at_k": recall_at_k,            # doc-hit rate; the CI gate metric
        "labeled": len(graded),
        "precision_at_k": _mean("precision_at_k"),
        "page_recall_at_k": _mean("recall_at_k"),
        "ndcg_at_k": _mean("ndcg_at_k"),
        "mrr": _mean("mrr"),
        "details": details,
    }
    log.info(
        "Eval[%s]: doc-hit recall@%d=%.2f (%d/%d) | labeled=%d  P@%d=%s  nDCG@%d=%s  MRR=%s",
        unit, k, recall_at_k, doc_hits, total, len(graded),
        k, summary["precision_at_k"], k, summary["ndcg_at_k"], summary["mrr"],
    )
    return summary
