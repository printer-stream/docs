"""Asset URL building + byte loading: CDN/base-url when configured, else local."""

from __future__ import annotations

import logging
import urllib.request
from typing import Optional

from .config import APP_NAME, ASSET_PREFIX, settings

log = logging.getLogger(APP_NAME)


def _core(rel_path: str) -> str:
    return rel_path[len(ASSET_PREFIX):] if rel_path.startswith(ASSET_PREFIX) else rel_path


def asset_url(rel_path: Optional[str]) -> Optional[str]:
    """Map a stored repo-relative asset path to a servable URL.

    'data-extraction/jpeg/star/x/small/page-01.jpg' ->
      base set:   '<static_base_url>/static/jpeg/star/x/small/page-01.jpg'
      base unset: '/static/jpeg/star/x/small/page-01.jpg' (relative)

    static_base_url defaults to base_url, so when the server's public base URL is
    configured the URLs are absolute (which remote MCP clients need to fetch them).
    """
    if not rel_path:
        return None
    core = _core(rel_path)
    base = settings.resolved_static_base_url
    if base:
        return "%s/static/%s" % (base, core)
    return "/static/%s" % core


def load_asset_bytes(rel_path: str, timeout: int = 30) -> bytes:
    """Read a static asset's bytes from the local static dir if present, else
    fetch from the configured base/CDN URL. Raises if neither is available
    (lean image without DOCS_STATIC_BASE_URL and without a mounted volume)."""
    core = _core(rel_path)
    static_dir = settings.static_directory()
    if static_dir is not None:
        path = static_dir / core
        if path.is_file():
            log.debug("asset from disk: %s", path)
            return path.read_bytes()
    base = settings.resolved_static_base_url
    if base:
        url = "%s/static/%s" % (base, core)
        log.debug("asset from url: %s", url)
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return resp.read()
    raise FileNotFoundError(
        "asset not available locally and no DOCS_STATIC_BASE_URL set: %s" % rel_path
    )
