"""Settings, path resolution, and logging for the indexer."""

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass
from pathlib import Path

LOGGER_NAME = "indexer"

# unicode61 tokenizer extended to keep command-significant symbols as token
# characters (so "GS / bit" phrase-matches). Prose terminators (. , ; : ! ? ( ))
# are deliberately NOT included so normal word search is unharmed; the trigram
# index is the substring/symbol recall net for everything else.
TOKENCHARS = "@/*^<>=&|~#+"
FTS_TOKENIZE = "unicode61 remove_diacritics 0 tokenchars '%s'" % TOKENCHARS
TRIGRAM_TOKENIZE = "trigram case_sensitive 0"


@dataclass
class Settings:
    root: Path
    index_type: str = "fulltext"
    out_root: str = "data-extraction"

    def __post_init__(self) -> None:
        self.root = Path(self.root).resolve()

    @property
    def pagemap_dir(self) -> Path:
        return self.root / self.out_root / "pagemap"

    @property
    def sections_dir(self) -> Path:
        return self.root / self.out_root / "sections"

    def sections_json_path(self, stem: str) -> Path:
        return self.sections_dir / (stem + ".json")

    @property
    def index_dir(self) -> Path:
        return self.root / self.out_root / "index"

    @property
    def fulltext_dir(self) -> Path:
        return self.index_dir / self.index_type

    @property
    def db_path(self) -> Path:
        return self.fulltext_dir / "specs.db"

    @property
    def manifest_path(self) -> Path:
        return self.index_dir / "manifest.json"

    def abs(self, rel: str) -> Path:
        return self.root / rel

    def describe_path(self, stem: str, label: str) -> Path:
        return self.root / self.out_root / "describe" / stem / (label + ".txt")

    def document_md(self, stem: str) -> Path:
        return self.root / self.out_root / "markdown" / stem / "document.md"


def setup_logging(level: str = "INFO") -> logging.Logger:
    numeric = getattr(logging, level.upper(), logging.INFO)
    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
    )
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(numeric)
    return logging.getLogger(LOGGER_NAME)
