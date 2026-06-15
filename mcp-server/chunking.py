"""Token-aware text windowing.

Splits long text into overlapping windows sized to the embedding model's
context limit, so embeddings never silently truncate a chunk's tail. Windows
are measured with the embedding model's own tokenizer so the token budget is
exact rather than estimated from characters.
"""
from __future__ import annotations

from typing import Iterator


def token_windows(
    text: str,
    tokenizer,
    size: int,
    overlap: int,
) -> Iterator[str]:
    """Yield overlapping token windows of `text`, each at most `size` tokens.

    Short text (<= size tokens) is yielded once, unchanged, preserving its
    exact formatting. Longer text is decoded back from token windows.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    if not 0 <= overlap < size:
        raise ValueError("overlap must satisfy 0 <= overlap < size")

    # verbose=False silences the tokenizer's "sequence longer than 512" notice:
    # producing >512 tokens here is expected — windowing below is what fixes it.
    ids = tokenizer.encode(text, add_special_tokens=False, verbose=False)
    if len(ids) <= size:
        yield text
        return

    step = size - overlap
    for start in range(0, len(ids), step):
        window_ids = ids[start:start + size]
        if not window_ids:
            break
        yield tokenizer.decode(window_ids, skip_special_tokens=True).strip()
        if start + size >= len(ids):
            break
