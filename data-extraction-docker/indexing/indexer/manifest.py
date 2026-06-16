"""Write the index manifest (builder version, params, counts, checksum)."""

from __future__ import annotations

import hashlib
import json
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

from .config import FTS_TOKENIZE, LOGGER_NAME, Settings, TOKENCHARS, TRIGRAM_TOKENIZE
from .version import __version__

log = logging.getLogger(LOGGER_NAME)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_manifest(settings: Settings, stats: Dict) -> Dict:
    db = settings.db_path
    payload = {
        "builder": {"name": "indexer", "version": __version__},
        "sqlite_version": sqlite3.sqlite_version,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "params": {
            "fts_tokenize": FTS_TOKENIZE,
            "trigram_tokenize": TRIGRAM_TOKENIZE,
            "tokenchars": TOKENCHARS,
        },
        "indexes": {
            settings.index_type: {
                "path": db.relative_to(settings.root).as_posix(),
                "engine": "sqlite-fts5",
                "tables": ["pages_fts (unicode61)", "pages_trgm (trigram)", "documents_fts"],
                "doc_count": stats.get("doc_count", 0),
                "page_count": stats.get("page_count", 0),
                "bytes": db.stat().st_size if db.exists() else 0,
                "sha256": _sha256(db) if db.exists() else None,
            }
        },
    }
    out = settings.manifest_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    log.info("Wrote index manifest %s", out)
    return payload
