"""Prompts for the VLM-backed phases, kept in one place so they're easy to tweak.

All are faithfulness-first: transcribe exactly, never invent, no preamble. ASCII.
"""

from __future__ import annotations

# describe phase: a supplementary, searchable description of a page image.
DESCRIBE_PROMPT = (
    "You are transcribing one page from a technical printer/plotter command "
    "specification (for example ESC/POS or HP-GL). Describe this page faithfully "
    "and concisely for a keyword search index. Transcribe every visible command "
    "name, hexadecimal value, parameter name, table header, and figure label "
    "EXACTLY as shown. For diagrams, state what they depict (for example a "
    "byte-to-dot bit-image layout). Do not invent commands or values; if "
    "something is unreadable, write 'unreadable'. Output plain text only, no "
    "preamble."
)

# markdown phase (vlm backend): full page image -> faithful GitHub-Flavored Markdown.
MARKDOWN_PROMPT = (
    "Transcribe this page from a technical printer/plotter command specification "
    "into clean GitHub-Flavored Markdown. Rules: reproduce ALL text faithfully; "
    "render tables as Markdown tables; preserve command names, hexadecimal values, "
    "byte sequences, and parameter names EXACTLY (for example 'GS ( k', '1B 40'); "
    "use Markdown headings for section and command titles, matching the page's "
    "hierarchy; for a figure or diagram, add a one-line note as an HTML comment "
    "like <!-- figure: ... --> capturing its labels and what it depicts; do not "
    "invent, summarize, or omit content; do not wrap the whole output in code "
    "fences or add commentary. Output only the page's Markdown."
)
