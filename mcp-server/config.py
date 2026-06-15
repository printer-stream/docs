"""Application configuration via pydantic-settings.

All settings are read from environment variables (DOCS_ prefix unless noted) or
from a `.env` file next to this module. Precedence: env vars > .env > defaults.

Supported variables:
  DOCS_REPO_ROOT       — data root; md/, jpeg/, index/ are expected below it
  DOCS_MD_DIR          — directory of per-page Markdown slices
  DOCS_MD_BULK_DIR     — directory of bulk Markdown exports
  DOCS_JPEG_DIR        — directory of page JPEG thumbnails
  DOCS_INDEX_PATH      — path to the SQLite search index
  DOCS_STATIC_BASE_URL — base URL page images are served from (empty -> the
                         server serves them itself under /static)
  HOST / DOCS_HOST     — server bind address
  PORT / DOCS_PORT     — server bind port
  DOCS_LOG_LEVEL       — log verbosity (DEBUG/INFO/WARNING/ERROR)
  DOCS_VERBOSE_DEPS    — show HTTP chatter from httpx
  DOCS_EVAL_LLM        — evaluate.py: use an LLM to generate eval queries
  DOCS_EVAL_MODEL      — evaluate.py: OpenAI model for eval query generation
  OPENAI_API_KEY       — evaluate.py: API key for LLM eval (no DOCS_ prefix)
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from pydantic import AliasChoices, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_HERE = Path(__file__).resolve().parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DOCS_",
        env_file=str(_HERE / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        # Tolerate unknown DOCS_ vars (e.g. a leftover DOCS_EMBED_MODEL from the
        # embedding era) instead of crashing on startup.
        extra="ignore",
    )

    repo_root: Path = _HERE.parent
    md_dir: Path = _HERE.parent / "md"
    md_bulk_dir: Path = _HERE.parent / "md-bulk"
    jpeg_dir: Path = _HERE.parent / "jpeg"
    index_path: Path = _HERE.parent / "index" / "specs.db"

    # Page images. Search results expose absolute URLs to each page's JPEG.
    # When set, URLs point at this base (e.g. a CDN, "https://cdn.example.com");
    # when empty, the server serves the images itself and builds URLs under
    # /static. A trailing slash is optional.
    static_base_url: str = ""

    # Server runtime. HOST/PORT keep their conventional unprefixed names (a
    # DOCS_-prefixed form is also accepted).
    host: str = Field("0.0.0.0", validation_alias=AliasChoices("DOCS_HOST", "HOST"))
    port: int = Field(8000, validation_alias=AliasChoices("DOCS_PORT", "PORT"))
    log_level: str = "INFO"
    verbose_deps: bool = False

    # Evaluation harness (evaluate.py) — optional, LLM-assisted query generation.
    eval_llm: bool = False
    eval_model: str = "gpt-4o-mini"
    openai_api_key: Optional[str] = Field(
        None, validation_alias=AliasChoices("OPENAI_API_KEY")
    )

    @model_validator(mode="before")
    @classmethod
    def _derive_missing_paths(cls, data: dict) -> dict:
        """Derive any unset path fields from repo_root before type validation.

        Using mode='before' keeps all fields typed as Path (not Optional[Path]),
        so callers never need to guard against None.
        """
        repo = Path(data.get("repo_root") or _HERE.parent)
        for key, relative in [
            ("md_dir", "md"),
            ("md_bulk_dir", "md-bulk"),
            ("jpeg_dir", "jpeg"),
            ("index_path", "index/specs.db"),
        ]:
            if not data.get(key):
                data[key] = repo / relative
        return data


cfg = Settings()
