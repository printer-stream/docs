"""Static HTML review reports for flagged pages.

Per-doc reports show the source JPEG beside the extracted Markdown for flagged
pages only, so manual review stays bounded. A corpus report aggregates them.
All output is ASCII-only.
"""

from __future__ import annotations

import html
import json
import logging
import os
from pathlib import Path
from typing import Dict, List

from .config import LOGGER_NAME, Settings

log = logging.getLogger(LOGGER_NAME)

_PAGE_STYLE = (
    "body{font-family:monospace;margin:1.5rem;}"
    "h1{font-size:1.2rem;}"
    ".pg{display:flex;gap:1rem;border-top:1px solid #ccc;padding:1rem 0;}"
    ".pg img{max-width:480px;border:1px solid #999;}"
    ".pg pre{white-space:pre-wrap;background:#f6f6f6;padding:0.5rem;flex:1;overflow:auto;}"
    ".reasons{color:#a00;}"
)


def write_doc_report(settings: Settings, stem: str, flagged_pages: List[Dict]) -> None:
    """flagged_pages: list of {label, page, score, reasons, md_abs, jpeg_abs}."""
    out = settings.quality_html_path(stem)
    out.parent.mkdir(parents=True, exist_ok=True)
    base = out.parent

    parts = [
        "<!doctype html><html><head><meta charset='ascii'>",
        "<title>QA review: %s</title><style>%s</style></head><body>" % (html.escape(stem), _PAGE_STYLE),
        "<h1>QA review: %s</h1>" % html.escape(stem),
        "<p>%d flagged page(s). Confirm the markdown matches the render.</p>" % len(flagged_pages),
    ]
    if not flagged_pages:
        parts.append("<p>No pages flagged.</p>")
    for fp in flagged_pages:
        img_rel = os.path.relpath(fp["jpeg_abs"], base)
        md_text = ""
        try:
            md_text = Path(fp["md_abs"]).read_text(encoding="utf-8")
        except OSError:
            md_text = "(markdown file missing)"
        reasons = "; ".join(fp.get("reasons") or []) or "below threshold"
        parts.append(
            "<div class='pg'><div><b>%s</b> (page %d, score %.2f)"
            "<div class='reasons'>%s</div><img src='%s'></div><pre>%s</pre></div>"
            % (
                html.escape(fp["label"]),
                fp["page"],
                fp["score"],
                html.escape(reasons),
                html.escape(img_rel),
                html.escape(md_text),
            )
        )
    parts.append("</body></html>")
    out.write_text("".join(parts), encoding="utf-8")
    log.info("Wrote doc QA report %s (%d flagged)", out, len(flagged_pages))


def write_corpus_report(settings: Settings) -> None:
    """Aggregate every quality/<vendor>/<doc>.json into quality/report.html."""
    rows = []
    total_pages = 0
    total_flagged = 0
    for qpath in sorted(settings.quality_dir.rglob("*.json")):
        try:
            data = json.loads(qpath.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            log.warning("Skipping unreadable quality file %s", qpath)
            continue
        stem = data.get("stem", qpath.stem)
        pages = data.get("page_count", len(data.get("pages", {})))
        flagged = data.get("flagged_count", 0)
        total_pages += pages
        total_flagged += flagged
        html_rel = os.path.relpath(settings.quality_html_path(stem), settings.quality_dir)
        rows.append((stem, pages, flagged, html_rel))

    parts = [
        "<!doctype html><html><head><meta charset='ascii'><title>QA report</title>",
        "<style>body{font-family:monospace;margin:1.5rem;}"
        "table{border-collapse:collapse;}td,th{border:1px solid #ccc;padding:0.3rem 0.6rem;}"
        ".f{color:#a00;}</style></head><body>",
        "<h1>Extraction QA report</h1>",
        "<p>%d docs, %d pages, <span class='f'>%d flagged</span>.</p>"
        % (len(rows), total_pages, total_flagged),
        "<table><tr><th>doc</th><th>pages</th><th>flagged</th><th>review</th></tr>",
    ]
    for stem, pages, flagged, html_rel in rows:
        cls = " class='f'" if flagged else ""
        parts.append(
            "<tr><td>%s</td><td>%d</td><td%s>%d</td><td><a href='%s'>open</a></td></tr>"
            % (html.escape(stem), pages, cls, flagged, html.escape(html_rel))
        )
    parts.append("</table></body></html>")

    out = settings.corpus_report_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(parts), encoding="utf-8")
    log.info("Wrote corpus QA report %s (%d docs, %d flagged pages)", out, len(rows), total_flagged)
