"""Build the search index from the Markdown corpus.

Output: a single SQLite file (default index/specs.db) containing
  - documents:  one row per doc, with an LLM/extractive summary
  - chunks:     page bodies + heading chunks + per-doc summary chunks
  - fts_chunks: FTS5 full-text index (exact command-token / hex lookups)
  - vec_chunks: sqlite-vec embeddings (semantic / conceptual search)

Run from anywhere:  python mcp-server/indexer.py
The index is committed to the repo and loaded read-only by the MCP server.
"""
from __future__ import annotations

import os
import re
import sqlite3
import struct
from pathlib import Path

import sqlite_vec
from sentence_transformers import SentenceTransformer

from corpus import (
    INDEX_PATH,
    Document,
    discover_documents,
    headings,
)

EMBED_MODEL = os.environ.get("DOCS_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
EMBED_DIM = 384  # bge-small-en-v1.5

# Command-style tokens worth indexing for exact lookup: ESC/GS mnemonics and hex.
_TOKEN_RE = re.compile(r"\b(?:ESC|GS|FS|DLE|[0-9A-Fa-f]{2}h?|0x[0-9A-Fa-f]{2})\b")


def serialize(vec) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def command_tokens(text: str) -> str:
    seen = dict.fromkeys(t.upper() for t in _TOKEN_RE.findall(text))
    return " ".join(seen)


def summarize(doc: Document) -> str:
    """One-paragraph 'what devices/technologies this doc covers' blurb.

    Uses an LLM if OPENAI_API_KEY is set; otherwise an extractive fallback
    (title + leading text of the first content pages).
    """
    head = "\n".join(p.text for p in doc.pages[:3])[:6000]
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=api_key)
            model = os.environ.get("DOCS_SUMMARY_MODEL", "gpt-4o-mini")
            resp = client.chat.completions.create(
                model=model,
                temperature=0.2,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You summarize printer/device technical specs. In 2-4 "
                            "sentences, state which devices, models, protocols, and "
                            "command sets the document covers, and who would use it."
                        ),
                    },
                    {"role": "user", "content": f"Title: {doc.title}\n\n{head}"},
                ],
            )
            return resp.choices[0].message.content.strip()
        except Exception as exc:  # noqa: BLE001 - never fail the build on summaries
            print(f"  summary LLM failed ({exc}); using extractive fallback")

    snippet = " ".join(head.split())[:500]
    return f"{doc.title}. {snippet}"


def build() -> None:
    docs = discover_documents()
    print(f"Discovered {len(docs)} document(s).")

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    if INDEX_PATH.exists():
        INDEX_PATH.unlink()

    db = sqlite3.connect(INDEX_PATH)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)

    db.executescript(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY,
            stem TEXT UNIQUE, vendor TEXT, title TEXT,
            summary TEXT, page_count INTEGER
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
    db.execute(
        f"CREATE VIRTUAL TABLE vec_chunks USING vec0(embedding float[{EMBED_DIM}])"
    )

    print(f"Loading embedding model: {EMBED_MODEL}")
    model = SentenceTransformer(EMBED_MODEL)

    chunk_rows: list[tuple] = []  # (doc_id, stem, vendor, page_no, kind, text, small, big)
    for doc_id, doc in enumerate(docs, start=1):
        summary = summarize(doc)
        db.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?,?)",
            (doc_id, doc.stem, doc.vendor, doc.title, summary, len(doc.pages)),
        )
        # Per-doc summary chunk (great for conceptual / 'what covers X' queries).
        chunk_rows.append((doc_id, doc.stem, doc.vendor, 0, "summary", summary, "", ""))
        for page in doc.pages:
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

    texts = [r[5] for r in chunk_rows]
    print(f"Embedding {len(texts)} chunk(s)...")
    embeddings = model.encode(
        texts, batch_size=32, normalize_embeddings=True, show_progress_bar=False
    )

    for chunk_id, (row, emb) in enumerate(zip(chunk_rows, embeddings), start=1):
        doc_id, stem, vendor, page_no, kind, text, small, big = row
        db.execute(
            "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?)",
            (chunk_id, doc_id, stem, vendor, page_no, kind, text, small, big),
        )
        db.execute(
            "INSERT INTO fts_chunks(rowid, text, tokens) VALUES (?,?,?)",
            (chunk_id, text, command_tokens(text)),
        )
        db.execute(
            "INSERT INTO vec_chunks(rowid, embedding) VALUES (?,?)",
            (chunk_id, serialize(emb)),
        )

    db.commit()
    db.close()
    size_kb = INDEX_PATH.stat().st_size // 1024
    print(f"Wrote {INDEX_PATH} ({size_kb} KB, {len(chunk_rows)} chunks).")


if __name__ == "__main__":
    build()
