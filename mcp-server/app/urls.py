"""Asset URL building: CDN/base-url when configured, else self-served /static."""

from __future__ import annotations

from typing import Optional

from .config import ASSET_PREFIX, settings


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
    core = rel_path[len(ASSET_PREFIX):] if rel_path.startswith(ASSET_PREFIX) else rel_path
    base = settings.resolved_static_base_url
    if base:
        return "%s/static/%s" % (base, core)
    return "/static/%s" % core
