"""Profiles: a TOML file mapping each phase to a backend + model + params.

A profile is the single place that says "which model does each step use", so
swapping models (or downgrading to cheaper hardware) is editing/selecting a
profile, not changing code. Parsed with stdlib tomllib (no dependency).

Built-in profiles live in ../profiles/*.toml; --profile also accepts a path.
"""

from __future__ import annotations

import logging
import tomllib
from pathlib import Path
from typing import Any, Dict

from .config import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

_BUILTIN_DIR = Path(__file__).resolve().parent.parent / "profiles"

# Applied when a profile omits a section/key, so every profile is complete.
DEFAULTS: Dict[str, Dict[str, Any]] = {
    "render": {"small_width": 1024, "big_dpi": 200, "jpeg_quality": 85},
    "markdown": {"backend": "docling", "do_ocr": True},
    "quality": {"backend": "heuristic", "threshold": 0.5},
    "describe": {"enabled": False, "gate": "illustrated", "image": "big"},
    "sections": {"backend": "headings"},
}


class Profile:
    def __init__(self, name: str, data: Dict[str, Any]) -> None:
        self.name = name
        self._data = data

    def phase(self, name: str) -> Dict[str, Any]:
        merged = dict(DEFAULTS.get(name, {}))
        merged.update(self._data.get(name, {}))
        return merged

    @property
    def render(self) -> Dict[str, Any]:
        return self.phase("render")

    @property
    def markdown(self) -> Dict[str, Any]:
        return self.phase("markdown")

    @property
    def quality(self) -> Dict[str, Any]:
        return self.phase("quality")

    @property
    def describe(self) -> Dict[str, Any]:
        return self.phase("describe")

    @property
    def sections(self) -> Dict[str, Any]:
        return self.phase("sections")


def load_profile(name_or_path: str) -> Profile:
    p = Path(name_or_path)
    if not p.suffix:
        candidate = _BUILTIN_DIR / (name_or_path + ".toml")
        if candidate.exists():
            p = candidate
    if not p.exists():
        builtins = ", ".join(sorted(f.stem for f in _BUILTIN_DIR.glob("*.toml")))
        raise SystemExit("profile not found: %s (built-ins: %s)" % (name_or_path, builtins))
    data = tomllib.loads(p.read_text(encoding="utf-8"))
    log.info("Loaded profile '%s' from %s", name_or_path, p)
    return Profile(name_or_path, data)
