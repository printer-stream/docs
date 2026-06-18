"""Tiny name -> factory registries so phase backends and describe gates can be
added, swapped, or removed cleanly (one function per strategy, no switch blocks)."""

from __future__ import annotations

from typing import Callable, Dict, List


class Registry:
    def __init__(self, kind: str) -> None:
        self.kind = kind
        self._items: Dict[str, Callable] = {}

    def register(self, name: str) -> Callable:
        def deco(fn: Callable) -> Callable:
            self._items[name] = fn
            return fn
        return deco

    def get(self, name: str) -> Callable:
        if name not in self._items:
            raise SystemExit(
                "unknown %s: %r (available: %s)" % (self.kind, name, ", ".join(self.names()))
            )
        return self._items[name]

    def names(self) -> List[str]:
        return sorted(self._items)
