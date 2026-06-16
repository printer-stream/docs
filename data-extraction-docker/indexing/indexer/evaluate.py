"""Search-quality eval harness.

Runs a fixed query set against the built index and reports, per query, whether
the expected document (and any expected page labels) appear in the top-k results
of the ranked full-text index, plus whether the trigram net finds them. Produces
a recall@k number so index variants can be compared objectively over time.
"""

from __future__ import annotations

import json
import logging
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional

from .config import LOGGER_NAME, Settings
from .search import search_fulltext, search_trigram

log = logging.getLogger(LOGGER_NAME)


def default_queries_path() -> Path:
    return Path(__file__).resolve().parent.parent / "eval" / "queries.json"


def _stem_rank(results: List[dict], stem: str) -> Optional[int]:
    for i, r in enumerate(results, start=1):
        if r["stem"] == stem:
            return i
    return None


def run_eval(settings: Settings, queries_path: Path, k: int = 10) -> Dict:
    queries = json.loads(queries_path.read_text(encoding="utf-8"))
    con = sqlite3.connect(str(settings.db_path))
    total = len(queries)
    passed = 0
    details: List[Dict] = []

    for item in queries:
        q = item["query"]
        expect_stem = item.get("expect_stem")
        expect_labels = item.get("expect_labels", [])

        ft = search_fulltext(con, q, k)
        tg = search_trigram(con, q, k)

        ft_rank = _stem_rank(ft, expect_stem) if expect_stem else None
        tg_hit = any(r["stem"] == expect_stem for r in tg) if expect_stem else None
        ft_labels = {r["label"] for r in ft if r["stem"] == expect_stem}
        labels_found = [lb for lb in expect_labels if lb in ft_labels]

        ok = True
        if expect_stem and ft_rank is None and not tg_hit:
            ok = False
        if expect_labels and not labels_found:
            ok = False
        passed += 1 if ok else 0

        log.info(
            "[%s] %-22s ft_rank=%s trgm=%s labels=%s/%s",
            "PASS" if ok else "FAIL", q, ft_rank, tg_hit,
            len(labels_found), len(expect_labels),
        )
        details.append(
            {
                "query": q, "expect_stem": expect_stem, "ok": ok,
                "ft_rank": ft_rank, "trigram_hit": tg_hit,
                "labels_found": labels_found, "labels_expected": expect_labels,
            }
        )

    con.close()
    recall = passed / total if total else 0.0
    log.info("Eval: %d/%d passed (recall@%d = %.2f)", passed, total, k, recall)
    return {"total": total, "passed": passed, "recall_at_k": recall, "k": k, "details": details}
