"""Per-phase timing and metadata.

Every phase records how long it took (overall and per page) plus the tool,
version, and params it used, and writes it to meta/<stem>/<phase>.json. The
assemble phase folds these into the pagemap so the lineage and timing of each
phase live alongside the results, for quality monitoring and troubleshooting.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from typing import Dict, Optional

from .config import LOGGER_NAME, Settings
from .version import __version__

log = logging.getLogger(LOGGER_NAME)


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class _PageTimer:
    def __init__(self, recorder: "PhaseRecorder", label: str) -> None:
        self._recorder = recorder
        self._label = label
        self._t0 = 0.0

    def __enter__(self) -> "_PageTimer":
        self._t0 = time.perf_counter()
        return self

    def __exit__(self, *exc) -> bool:
        self._recorder.page_seconds[self._label] = time.perf_counter() - self._t0
        return False


class PhaseRecorder:
    """Times a phase and builds its meta payload."""

    def __init__(self, phase: str, tool: str, version: str, params: Optional[Dict] = None) -> None:
        self.phase = phase
        self.tool = tool
        self.tool_version = version
        self.params = params or {}
        self.started_at = utcnow()
        self._t0 = time.perf_counter()
        self.page_seconds: Dict[str, float] = {}

    def time_page(self, label: str) -> _PageTimer:
        return _PageTimer(self, label)

    def to_dict(
        self, stem: str, page_count: int, status: str = "ok", extra: Optional[Dict] = None
    ) -> Dict:
        duration = time.perf_counter() - self._t0
        payload: Dict = {
            "stem": stem,
            "phase": self.phase,
            "tool": self.tool,
            "tool_version": self.tool_version,
            "pipeline_version": __version__,
            "params": self.params,
            "page_count": page_count,
            "started_at": self.started_at,
            "ended_at": utcnow(),
            "duration_seconds": round(duration, 3),
            "per_page_seconds_avg": round(duration / page_count, 3) if page_count else None,
            "status": status,
        }
        if self.page_seconds:
            payload["page_seconds"] = {k: round(v, 3) for k, v in self.page_seconds.items()}
        if extra:
            payload.update(extra)
        return payload


def write_meta(settings: Settings, stem: str, phase: str, payload: Dict) -> None:
    path = settings.meta_path(stem, phase)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    log.info(
        "Phase %s on %s: %.1fs (%s pages)",
        phase, stem, payload.get("duration_seconds", 0.0), payload.get("page_count", "?"),
    )


def read_meta(settings: Settings, stem: str, phase: str) -> Optional[Dict]:
    path = settings.meta_path(stem, phase)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        log.warning("Unreadable meta %s", path)
        return None
