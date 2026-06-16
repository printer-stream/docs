"""Configuration: loaded from a .env file, overridable by environment variables.

All config flows through the single `settings` object (pydantic-settings); no
module reads os.environ directly. Precedence is: environment variable > .env file
> default. The .env file is read from the process working directory (in the image
that is /app); in production, values come from the environment.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

APP_NAME = "printer-stream-docs"

# Repo-relative prefix stripped from stored asset paths when building URLs.
ASSET_PREFIX = "data-extraction/"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

    db_path: Path = Field(default=Path("/app/index/specs.db"), alias="DOCS_DB_PATH")
    static_dir: str = Field(default="/app/static", alias="DOCS_STATIC_DIR")
    # Public base URL of this server; used to build absolute asset URLs.
    base_url: str = Field(default="", alias="DOCS_BASE_URL")
    # Where static assets are served from; defaults to base_url (a CDN overrides it).
    static_base_url: Optional[str] = Field(default=None, alias="DOCS_STATIC_BASE_URL")

    host: str = Field(default="0.0.0.0", alias="HOST")
    port: int = Field(default=10000, alias="PORT")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    search_k: int = Field(default=8, alias="DOCS_SEARCH_K")
    search_max_k: int = Field(default=50, alias="DOCS_SEARCH_MAX_K")

    @property
    def resolved_static_base_url(self) -> str:
        """Static base URL, defaulting to base_url; trailing slash stripped."""
        value = self.static_base_url if self.static_base_url else self.base_url
        return (value or "").rstrip("/")

    def static_directory(self) -> Optional[Path]:
        """The directory to self-serve static assets from, or None (CDN/lean)."""
        p = Path(self.static_dir)
        return p if p.is_dir() else None


settings = Settings()


def setup_logging() -> logging.Logger:
    numeric = getattr(logging, settings.log_level.upper(), logging.INFO)
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
    return logging.getLogger(APP_NAME)
