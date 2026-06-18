"""Build the SQLite FTS5 search index from pagemaps + markdown + sections.

Retrieval is section-first (a command/topic spans pages), with pages kept as a
fallback search path and as the displayable artifact. Reads each pagemap (the
authoritative page<->artifact map) plus sections/<stem>.json, and populates:
  - documents      : per-doc title, languages, extractive summary
  - sections       : logical chunk + body + the page range/labels it covers
  - sections_fts   : ranked section full-text (unicode61 + command-symbol tokenchars)
  - sections_trgm  : section substring/symbol recall (trigram)
  - pages          : page metadata + body (self-contained, fallback + display)
  - pages_fts      : ranked page full-text
  - pages_trgm     : page substring/symbol recall (trigram)
  - documents_fts  : title/summary search
"""

from __future__ import annotations

import json
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

from . import summary as summary_mod
from .config import FTS_TOKENIZE, LOGGER_NAME, Settings, TRIGRAM_TOKENIZE
from .version import __version__

log = logging.getLogger(LOGGER_NAME)


def _schema_sql() -> str:
    return """
DROP TABLE IF EXISTS documents_fts;
DROP TABLE IF EXISTS sections_trgm;
DROP TABLE IF EXISTS sections_fts;
DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS pages_trgm;
DROP TABLE IF EXISTS pages_fts;
DROP TABLE IF EXISTS pages;
DROP TABLE IF EXISTS documents;
DROP TABLE IF EXISTS index_meta;

-- Key/value metadata about this index build (created_at, indexer_version, ...).
CREATE TABLE index_meta (key TEXT PRIMARY KEY, value TEXT);

CREATE TABLE documents (
  id INTEGER PRIMARY KEY,
  stem TEXT UNIQUE, vendor TEXT, doc TEXT, title TEXT,
  page_count INTEGER, languages TEXT, summary TEXT, source_pdf TEXT,
  -- Extraction lineage copied from the pagemap (for /version and /documents).
  extracted_at TEXT, pipeline_version TEXT, phases TEXT
);

-- Sections are the primary retrieval unit: a logical chunk that may span pages,
-- carrying the page range/labels it covers (page_labels is a JSON array).
CREATE TABLE sections (
  id INTEGER PRIMARY KEY,
  stem TEXT, vendor TEXT, doc TEXT, section_no INTEGER,
  title TEXT, heading_path TEXT, level INTEGER, body TEXT,
  page_start INTEGER, page_end INTEGER, page_labels TEXT, char_count INTEGER
);
CREATE INDEX idx_sections_stem ON sections(stem);
CREATE INDEX idx_sections_vendor ON sections(vendor);

CREATE TABLE pages (
  id INTEGER PRIMARY KEY,
  stem TEXT, vendor TEXT, doc TEXT, page INTEGER, label TEXT,
  heading_path TEXT, body TEXT, description TEXT,
  jpeg_small TEXT, jpeg_big TEXT, markdown TEXT,
  source TEXT, flagged INTEGER
);
CREATE INDEX idx_pages_stem ON pages(stem);
CREATE INDEX idx_pages_vendor ON pages(vendor);

CREATE VIRTUAL TABLE sections_fts USING fts5(
  title, heading_path, body,
  content='sections', content_rowid='id',
  tokenize="%s"
);
CREATE VIRTUAL TABLE sections_trgm USING fts5(
  body,
  content='sections', content_rowid='id',
  tokenize="%s"
);
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
""" % (FTS_TOKENIZE, TRIGRAM_TOKENIZE, FTS_TOKENIZE, TRIGRAM_TOKENIZE)


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
        "INSERT INTO documents(stem,vendor,doc,title,page_count,languages,summary,source_pdf,"
        "extracted_at,pipeline_version,phases)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (stem, vendor, doc, title, pagemap.get("page_count", len(pages)),
         languages, summary, pagemap.get("source_pdf"),
         pagemap.get("generated_at"), pagemap.get("pipeline_version"),
         json.dumps(pagemap.get("phases", {}), ensure_ascii=True)),
    )
    log.info("Indexed %s: %d pages, languages=[%s]", stem, len(rows), languages)
    return len(rows)


def _index_sections(con, settings: Settings, stem: str) -> int:
    """Insert a document's logical sections from sections/<stem>.json. Missing or
    unreadable -> warn and skip (the doc's pages are still indexed)."""
    path = settings.sections_json_path(stem)
    if not path.exists():
        log.warning("No sections.json for %s; section search unavailable for this doc", stem)
        return 0
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        log.exception("Skipping unreadable sections.json %s", path)
        return 0
    vendor = data.get("vendor", "")
    doc = data.get("doc", "")
    rows: List[Tuple] = []
    for s in data.get("sections", []):
        body = s.get("text", "")
        rows.append(
            (
                stem, vendor, doc, s.get("id"),
                s.get("title", ""), s.get("heading_path", ""), s.get("level"), body,
                s.get("page_start"), s.get("page_end"),
                json.dumps(s.get("page_labels", []), ensure_ascii=True),
                s.get("char_count", len(body)),
            )
        )
    con.executemany(
        "INSERT INTO sections(stem,vendor,doc,section_no,title,heading_path,level,body,"
        "page_start,page_end,page_labels,char_count) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        rows,
    )
    log.info("Indexed %s: %d sections", stem, len(rows))
    return len(rows)


def _populate_fts(con) -> None:
    con.execute(
        "INSERT INTO sections_fts(rowid, title, heading_path, body) "
        "SELECT id, title, heading_path, body FROM sections"
    )
    con.execute("INSERT INTO sections_trgm(rowid, body) SELECT id, body FROM sections")
    con.execute(
        "INSERT INTO pages_fts(rowid, body, description, heading_path) "
        "SELECT id, body, description, heading_path FROM pages"
    )
    con.execute("INSERT INTO pages_trgm(rowid, body) SELECT id, body FROM pages")
    con.execute(
        "INSERT INTO documents_fts(rowid, title, summary, languages) "
        "SELECT id, title, summary, languages FROM documents"
    )
    for tbl in ("sections_fts", "sections_trgm", "pages_fts", "pages_trgm"):
        con.execute("INSERT INTO %s(%s) VALUES('optimize')" % (tbl, tbl))
    log.info("Populated and optimized FTS indexes")


def _write_index_meta(con, doc_count: int, page_count: int, section_count: int) -> None:
    con.executemany(
        "INSERT INTO index_meta(key, value) VALUES (?, ?)",
        [
            ("created_at", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
            ("indexer_version", __version__),
            ("sqlite_version", sqlite3.sqlite_version),
            ("doc_count", str(doc_count)),
            ("page_count", str(page_count)),
            ("section_count", str(section_count)),
        ],
    )


def build_index(con, settings: Settings) -> Dict:
    """Build the whole index into an open connection. Returns build stats."""
    con.executescript(_schema_sql())
    pagemaps = _iter_pagemaps(settings)
    if not pagemaps:
        log.warning("No pagemaps found under %s", settings.pagemap_dir)
    doc_count = 0
    page_count = 0
    section_count = 0
    for pm_path in pagemaps:
        try:
            pagemap = json.loads(pm_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.exception("Skipping unreadable pagemap %s", pm_path)
            continue
        page_count += _index_document(con, settings, pagemap)
        section_count += _index_sections(con, settings, pagemap["stem"])
        doc_count += 1
    _populate_fts(con)
    _write_index_meta(con, doc_count, page_count, section_count)
    con.commit()
    log.info("Build complete: %d docs, %d pages, %d sections", doc_count, page_count, section_count)
    return {"doc_count": doc_count, "page_count": page_count, "section_count": section_count}
