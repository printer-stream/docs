"""The describe-phase prompt.

The describe phase gives figure/diagram/low-text pages a searchable text surface
the keyword index can see (improving recall). Descriptions are a clearly separate,
supplementary signal - never merged into the authoritative markdown. The model is
called through providers.LLMClient (any OpenAI-compatible endpoint); this module
just holds the prompt.
"""

from __future__ import annotations

# Faithful, transcription-first prompt. The point is recall, not prose: capture
# exact tokens, never invent. Kept ASCII.
PROMPT = (
    "You are transcribing one page from a technical printer/plotter command "
    "specification (for example ESC/POS or HP-GL). Describe this page faithfully "
    "and concisely for a keyword search index. Transcribe every visible command "
    "name, hexadecimal value, parameter name, table header, and figure label "
    "EXACTLY as shown. For diagrams, state what they depict (for example a "
    "byte-to-dot bit-image layout). Do not invent commands or values; if "
    "something is unreadable, write 'unreadable'. Output plain text only, no "
    "preamble."
)
