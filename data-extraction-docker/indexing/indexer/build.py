"""Build the SQLite FTS5 search index from pagemaps + markdown (+ descriptions).

Reads each pagemap (the authoritative page<->artifact map), pulls each page's
markdown body and optional VLM description, and populates:
  - pages          : page metadata + body (self-contained for retrieval)
  - documents      : per-doc title, languages, extractive summary
  - pages_fts      : ranked full-text (unicode61 + command-symbol tokenchars)
  - pages_trgm     : substring/symbol recall (trigram)
  - documents_fts  : title/summary search
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple

from . import summary as summary_mod
from .config import FTS_TOKENIZE, LOGGER_NAME, Settings, TRIGRAM_TOKENIZE

log = logging.getLogger(LOGGER_NAME)


def _schema_sql() -> str:
    return """
DROP TABLE IF EXISTS documents_fts;
DROP TABLE IF EXISTS pages_trgm;
DROP TABLE IF EXISTS pages_fts;
DROP TABLE IF EXISTS pages;
DROP TABLE IF EXISTS documents;

CREATE TABLE documents (
  id INTEGER PRIMARY KEY,
  stem TEXT UNIQUE, vendor TEXT, doc TEXT, title TEXT,
  page_count INTEGER, languages TEXT, summary TEXT, source_pdf TEXT
);

CREATE TABLE pages (
  id INTEGER PRIMARY KEY,
  stem TEXT, vendor TEXT, doc TEXT, page INTEGER, label TEXT,
  heading_path TEXT, body TEXT, description TEXT,
  jpeg_small TEXT, jpeg_big TEXT, markdown TEXT,
  source TEXT, flagged INTEGER
);
CREATE INDEX idx_pages_stem ON pages(stem);
CREATE INDEX idx_pages_vendor ON pages(vendor);

CREATE VIRTUAL TABLE pages_fts USING fts5(
  body, description, heading_path,
  content='pages', content_rowid='id',
  tokenize="%s"
);
CREATE VIRTUAL TABLE pages_trgm USING fts5(
  body,
  content='pages', content_rowid='id',
  tokenize="%s"
);
CREATE VIRTUAL TABLE documents_fts USING fts5(
  title, summary, languages,
  content='documents', content_rowid='id',
  tokenize="unicode61 remove_diacritics 0"
);
""" % (FTS_TOKENIZE, TRIGRAM_TOKENIZE)


def _iter_pagemaps(settings: Settings) -> List[Path]:
    return [p for p in sorted(settings.pagemap_dir.rglob("*.json")) if p.name != "schema.json"]


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _index_document(con, settings: Settings, pagemap: Dict) -> int:
    stem = pagemap["stem"]
    vendor = pagemap["vendor"]
    doc = pagemap["doc"]
    pages = pagemap.get("pages", [])

    full_text_parts: List[str] = []
    rows: List[Tuple] = []
    for pr in pages:
        label = pr["label"]
        body = _read(settings.abs(pr["markdown"]))
        desc_rel = pr.get("describe")
        description = _read(settings.abs(desc_rel)) if desc_rel else _read(
            settings.describe_path(stem, label)
        )
        headings = summary_mod.extract_headings(body)
        heading_path = " > ".join(headings)
        full_text_parts.append(body)
        rows.append(
            (
                stem, vendor, doc, pr["page"], label, heading_path, body, description,
                pr.get("jpeg_small"), pr.get("jpeg_big"), pr.get("markdown"),
                pr.get("source"), 1 if pr.get("flagged") else 0,
            )
        )

    con.executemany(
        "INSERT INTO pages(stem,vendor,doc,page,label,heading_path,body,description,"
        "jpeg_small,jpeg_big,markdown,source,flagged) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        rows,
    )

    title, languages, summary = summary_mod.make_summary(
        vendor, doc, pagemap.get("page_count", len(pages)), "\n".join(full_text_parts)
    )
    con.execute(
        "INSERT INTO documents(stem,vendor,doc,title,page_count,languages,summary,source_pdf)"
        " VALUES (?,?,?,?,?,?,?,?)",
        (stem, vendor, doc, title, pagemap.get("page_count", len(pages)),
         languages, summary, pagemap.get("source_pdf")),
    )
    log.info("Indexed %s: %d pages, languages=[%s]", stem, len(rows), languages)
    return len(rows)


def _populate_fts(con) -> None:
    con.execute(
        "INSERT INTO pages_fts(rowid, body, description, heading_path) "
        "SELECT id, body, description, heading_path FROM pages"
    )
    con.execute("INSERT INTO pages_trgm(rowid, body) SELECT id, body FROM pages")
    con.execute(
        "INSERT INTO documents_fts(rowid, title, summary, languages) "
        "SELECT id, title, summary, languages FROM documents"
    )
    con.execute("INSERT INTO pages_fts(pages_fts) VALUES('optimize')")
    con.execute("INSERT INTO pages_trgm(pages_trgm) VALUES('optimize')")
    log.info("Populated and optimized FTS indexes")


def build_index(con, settings: Settings) -> Dict:
    """Build the whole index into an open connection. Returns build stats."""
    con.executescript(_schema_sql())
    pagemaps = _iter_pagemaps(settings)
    if not pagemaps:
        log.warning("No pagemaps found under %s", settings.pagemap_dir)
    doc_count = 0
    page_count = 0
    for pm_path in pagemaps:
        try:
            pagemap = json.loads(pm_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.exception("Skipping unreadable pagemap %s", pm_path)
            continue
        page_count += _index_document(con, settings, pagemap)
        doc_count += 1
    _populate_fts(con)
    con.commit()
    log.info("Build complete: %d docs, %d pages", doc_count, page_count)
    return {"doc_count": doc_count, "page_count": page_count}
