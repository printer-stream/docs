"""Build the full-text search index from the Markdown corpus.

Output: a single SQLite file (default index/specs.db) containing
  - meta:        index metadata (schema version, build time)
  - documents:   one row per doc, with an extractive summary
  - pages:       full page Markdown (source of truth for get_page)
  - chunks:      retrieval units — one body chunk per page, plus heading and
                 per-document summary chunks
  - fts_chunks:  FTS5 full-text index (keyword search + exact command-token /
                 hex lookups via the `tokens` column)

FTS5 has no context-window limit, so whole pages are indexed directly — there is
no embedding model and no token windowing. Run from anywhere:

    python mcp-server/indexer.py

The index is committed to the repo and loaded read-only by the MCP server.
"""
from __future__ import annotations

import os
import re
import sqlite3
import time

from config import cfg
from corpus import discover_documents, headings
from summarizer import summarize

# Bump when the table layout changes so the server can detect incompatibility.
SCHEMA_VERSION = 3

# Command-style tokens worth indexing for exact lookup: ESC/GS mnemonics and hex.
_TOKEN_RE = re.compile(r"\b(?:ESC|GS|FS|DLE|[0-9A-Fa-f]{2}h?|0x[0-9A-Fa-f]{2})\b")


def command_tokens(text: str) -> str:
    seen = dict.fromkeys(t.upper() for t in _TOKEN_RE.findall(text))
    return " ".join(seen)


def build() -> None:
    docs = discover_documents()
    print(f"Discovered {len(docs)} document(s).")

    cfg.index_path.parent.mkdir(parents=True, exist_ok=True)

    # Write to a temp file and atomically rename on success so the live index
    # is never left in a partial state if the process is interrupted mid-build.
    tmp_path = cfg.index_path.with_name(cfg.index_path.name + ".tmp")
    if tmp_path.exists():
        tmp_path.unlink()

    db = sqlite3.connect(tmp_path)
    db.executescript(
        """
        CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY,
            stem TEXT UNIQUE, vendor TEXT, title TEXT,
            summary TEXT, page_count INTEGER
        );
        CREATE TABLE pages (
            doc_id INTEGER, stem TEXT, vendor TEXT, page_no INTEGER,
            text TEXT, image_small TEXT, image_big TEXT,
            PRIMARY KEY (stem, page_no)
        );
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            doc_id INTEGER, stem TEXT, vendor TEXT,
            page_no INTEGER, kind TEXT, text TEXT,
            image_small TEXT, image_big TEXT
        );
        CREATE VIRTUAL TABLE fts_chunks USING fts5(
            text, tokens, content=''
        );
        """
    )

    db.executemany(
        "INSERT INTO meta(key, value) VALUES (?,?)",
        [
            ("schema_version", str(SCHEMA_VERSION)),
            ("search", "fts5"),
            ("built_at", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())),
        ],
    )

    # (doc_id, stem, vendor, page_no, kind, text, small, big)
    chunk_rows: list[tuple] = []
    for doc_id, doc in enumerate(docs, start=1):
        summary = summarize(doc)
        db.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?,?)",
            (doc_id, doc.stem, doc.vendor, doc.title, summary, len(doc.pages)),
        )
        # Per-doc summary chunk (great for conceptual / 'what covers X' queries).
        chunk_rows.append((doc_id, doc.stem, doc.vendor, 0, "summary", summary, "", ""))
        for page in doc.pages:
            # Full page is the source of truth for get_page ...
            db.execute(
                "INSERT INTO pages VALUES (?,?,?,?,?,?,?)",
                (doc_id, doc.stem, doc.vendor, page.page_no,
                 page.text, page.image_small, page.image_big),
            )
            # ... and is indexed whole as a single body chunk (FTS5 has no
            # context limit, so no windowing is needed).
            if page.text.strip():
                chunk_rows.append(
                    (doc_id, doc.stem, doc.vendor, page.page_no, "body",
                     page.text, page.image_small, page.image_big)
                )
            for h in headings(page.text):
                chunk_rows.append(
                    (doc_id, doc.stem, doc.vendor, page.page_no, "title",
                     h, page.image_small, page.image_big)
                )
        print(f"  [{doc_id}/{len(docs)}] {doc.stem}: {len(doc.pages)} page(s)")

    print(f"Indexing {len(chunk_rows)} chunk(s)...")
    for chunk_id, row in enumerate(chunk_rows, start=1):
        doc_id, stem, vendor, page_no, kind, text, small, big = row
        db.execute(
            "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?)",
            (chunk_id, doc_id, stem, vendor, page_no, kind, text, small, big),
        )
        db.execute(
            "INSERT INTO fts_chunks(rowid, text, tokens) VALUES (?,?,?)",
            (chunk_id, text, command_tokens(text)),
        )

    db.commit()
    db.close()

    # Atomic promotion — only replaces the live index once the new one is complete.
    os.replace(tmp_path, cfg.index_path)
    size_kb = cfg.index_path.stat().st_size // 1024
    print(f"Wrote {cfg.index_path} ({size_kb} KB, {len(chunk_rows)} chunks).")


if __name__ == "__main__":
    build()
