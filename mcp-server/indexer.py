"""Build the search index from the Markdown corpus.

Output: a single SQLite file (default index/specs.db) containing
  - meta:        index metadata (embed model + dim, schema version, build time)
  - documents:   one row per doc, with a local-LLM/extractive summary
  - pages:       full page Markdown (source of truth for get_page)
  - chunks:      retrieval units — windowed page bodies + headings + summaries
  - fts_chunks:  FTS5 full-text index (exact command-token / hex lookups)
  - vec_chunks:  sqlite-vec embeddings (semantic / conceptual search)

Pages are stored whole, but embedded in token-sized windows so no content is
lost to the embedding model's context limit. Run from anywhere:

    python mcp-server/indexer.py

The index is committed to the repo and loaded read-only by the MCP server.
"""
from __future__ import annotations

import os
import re
import sqlite3
import time

import sqlite_vec
from sentence_transformers import SentenceTransformer

from chunking import token_windows
from config import cfg
from corpus import discover_documents, headings
from summarizer import summarize
from utils import serialize

# Bump when the table layout changes so the server can detect incompatibility.
SCHEMA_VERSION = 2

# Command-style tokens worth indexing for exact lookup: ESC/GS mnemonics and hex.
_TOKEN_RE = re.compile(r"\b(?:ESC|GS|FS|DLE|[0-9A-Fa-f]{2}h?|0x[0-9A-Fa-f]{2})\b")


def command_tokens(text: str) -> str:
    seen = dict.fromkeys(t.upper() for t in _TOKEN_RE.findall(text))
    return " ".join(seen)


def build() -> None:
    docs = discover_documents()
    print(f"Discovered {len(docs)} document(s).")

    # Load the embedding model first: we need its real output dimension to size
    # the vec table, and its tokenizer to window long pages exactly.
    print(f"Loading embedding model: {cfg.embed_model}")
    embed_model = SentenceTransformer(cfg.embed_model)
    try:
        embed_dim = embed_model.get_embedding_dimension()
    except AttributeError:  # older sentence-transformers
        embed_dim = embed_model.get_sentence_embedding_dimension()
    tokenizer = embed_model.tokenizer
    print(f"Embedding dimension: {embed_dim}")

    cfg.index_path.parent.mkdir(parents=True, exist_ok=True)

    # Write to a temp file and atomically rename on success so the live index
    # is never left in a partial state if the process is interrupted mid-build.
    tmp_path = cfg.index_path.with_name(cfg.index_path.name + ".tmp")
    if tmp_path.exists():
        tmp_path.unlink()

    db = sqlite3.connect(tmp_path)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)

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
    db.execute(
        f"CREATE VIRTUAL TABLE vec_chunks USING vec0(embedding float[{embed_dim}])"
    )

    db.executemany(
        "INSERT INTO meta(key, value) VALUES (?,?)",
        [
            ("schema_version", str(SCHEMA_VERSION)),
            ("embed_model", cfg.embed_model),
            ("embed_dim", str(embed_dim)),
            ("summary_backend", cfg.summary_backend),
            ("summary_model", cfg.summary_model if cfg.summary_backend == "local" else ""),
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
            # Full page is stored whole for get_page ...
            db.execute(
                "INSERT INTO pages VALUES (?,?,?,?,?,?,?)",
                (doc_id, doc.stem, doc.vendor, page.page_no,
                 page.text, page.image_small, page.image_big),
            )
            # ... but embedded in token windows so long pages aren't truncated.
            for window in token_windows(
                page.text, tokenizer, cfg.chunk_tokens, cfg.chunk_overlap
            ):
                if not window:
                    continue
                chunk_rows.append(
                    (doc_id, doc.stem, doc.vendor, page.page_no, "body",
                     window, page.image_small, page.image_big)
                )
            for h in headings(page.text):
                chunk_rows.append(
                    (doc_id, doc.stem, doc.vendor, page.page_no, "title",
                     h, page.image_small, page.image_big)
                )
        print(f"  [{doc_id}/{len(docs)}] {doc.stem}: {len(doc.pages)} page(s)")

    texts = [r[5] for r in chunk_rows]
    print(f"Embedding {len(texts)} chunk(s)...")
    embeddings = embed_model.encode(
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

    # Atomic promotion — only replaces the live index once the new one is complete.
    os.replace(tmp_path, cfg.index_path)
    size_kb = cfg.index_path.stat().st_size // 1024
    print(f"Wrote {cfg.index_path} ({size_kb} KB, {len(chunk_rows)} chunks).")


if __name__ == "__main__":
    build()
