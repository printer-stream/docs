"""Low-level shared utilities for the MCP server and indexer."""
from __future__ import annotations

import numpy as np


def serialize(vec) -> bytes:
    """Serialise a vector to raw float32 bytes expected by sqlite-vec.

    Accepts any array-like (numpy array, list, torch tensor) and always
    outputs little-endian float32, which is what sqlite-vec's vec0 expects.
    Using tobytes() instead of struct.pack(*vec) avoids unpacking all elements
    into Python objects — roughly 50-100x faster for typical embedding dims.
    """
    return np.asarray(vec, dtype=np.float32).tobytes()
