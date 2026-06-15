#!/usr/bin/env python3
"""Deterministic clean-up pass for the extracted Markdown corpus.

The PDF->Markdown extraction (current `pymupdf4llm` pipeline, and the older tool
that produced the committed `md/`) leaves several classes of low-value noise that
hurt full-text search and readability. `clean()` removes them; it is idempotent
(safe to run repeatedly) and tool-agnostic.

Noise classes removed (see TASK-1-SIMPLIFY.md):
  1. Glyph/bitmap tables  -- download-character font tables rendered as walls of
     `|...●<br>○<br>...|` cells; replaced with a short placeholder.
  3. Picture placeholders -- `**==> picture [W x H] intentionally omitted <==**`.
  4. Picture-text blocks  -- `**----- Start of picture text -----**` ... `End`.
  6. Repeated headers/footers -- horizontal-rule artifact lines, bare page
     numbers, and running titles that recur across most of a document's pages.

Collapsed command-spec tables (class 2) are intentionally left alone: the text is
still searchable and re-flowing them heuristically is risky.

CLI:
  python scripts/md_clean.py                 # clean md/ and md-bulk/ in place
  python scripts/md_clean.py path [path ...] # clean specific files/dirs in place
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

# Class 3: bold-wrapped "picture intentionally omitted" placeholder line.
_PICTURE_PLACEHOLDER_RE = re.compile(
    r"^\s*\*\*==>\s*picture\b[^\n]*intentionally omitted[^\n]*<==\*\*\s*$",
    re.MULTILINE,
)

# Class 4: the OCR'd "picture text" block, from the Start marker through the End
# marker (the End marker often trails content on its own line). DOTALL + lazy so
# each block is matched independently.
_PICTURE_TEXT_BLOCK_RE = re.compile(
    r"\*\*-{2,}\s*Start of picture text\s*-{2,}\*\*.*?-{2,}\s*End of picture text\s*-{2,}\*\*(?:<br>)?",
    re.DOTALL,
)
# Any orphan picture-text markers left without a matching pair.
_PICTURE_TEXT_ORPHAN_RE = re.compile(
    r"^\s*\*?\*?-{2,}\s*(?:Start|End) of picture text\s*-{2,}\*?\*?(?:<br>)?\s*$",
    re.MULTILINE,
)

# Class 6 horizontal-rule artifacts. PDF page separators come through as long
# runs of the bar glyphs U+2015 / U+2014 / U+2500 (NOT the ASCII hyphen, so real
# Markdown table separators like `|---|` are never touched).
_RULE_CHARS = "―—─"
# A run of bar glyphs through end of line: a footer caption glued onto content.
_TRAILING_RULE_RE = re.compile(rf"\s*[{_RULE_CHARS}]{{5,}}.*$")
# Characters that may make up a pure separator row (incl. pipe-wrapped ones).
_RULE_ONLY = set(_RULE_CHARS + "=| \t")

# Class 6: a line that is only a (optionally bold) page number.
_PAGE_NUMBER_RE = re.compile(r"^\s*\*{0,2}\d{1,4}\*{0,2}\s*$")

# Class 6: full-page watermark tokens stamped on every page. The OCR often
# space-separates the letters and sometimes glues the token onto a real heading
# (e.g. "## **C O N F I D E N T I A L Program example for GS L**"), so the token
# is removed in place and an emptied heading/emphasis shell is then dropped.
# Extend this list with any other corpus-wide watermarks.
_WATERMARK_RE = re.compile(
    r"C\s*O\s*N\s*F\s*I\s*D\s*E\s*N\s*T\s*I\s*A\s*L",
    re.IGNORECASE,
)
# A line left with nothing but Markdown markup (#, *, _, ~) after token removal.
_MARKUP_SHELL_RE = re.compile(r"^[#*_~\s]+$")


def _is_pure_rule(line: str) -> bool:
    """True for a line that is only a horizontal-rule artifact (incl. `|――|`)."""
    core = line.strip()
    if not core or not any(c in core for c in _RULE_CHARS + "="):
        return False
    rule = sum(c in _RULE_CHARS or c == "=" for c in core)
    return rule >= 4 and all(c in _RULE_ONLY for c in core)

# Glyph-table cell characters: filled/empty dot matrix marks.
_GLYPH_CHARS = "●○▪▫•■□"  # ● ○ ▪ ▫ • ■ □


def _is_glyph_table_block(lines: list[str]) -> bool:
    """True if a run of table lines is a bitmap/font table rather than data.

    Real command tables (e.g. `|Commands|Name|...|`) carry words and no dot-matrix
    marks; glyph tables are dominated by ●/○ cells. Key on glyph density so data
    tables are never touched.
    """
    body = "".join(lines)
    glyphs = sum(body.count(c) for c in _GLYPH_CHARS)
    if glyphs < 8:
        return False
    # Discount the table scaffolding itself: `<br>` and `|` would otherwise
    # contribute hundreds of fake "alnum" letters (b, r) and dwarf the signal.
    content = body.replace("<br>", " ").replace("|", " ")
    alnum = sum(ch.isalnum() for ch in content)
    # Plenty of marks vs real characters -> it's pixel art, not a data table.
    return glyphs >= alnum


def _strip_glyph_tables(text: str) -> str:
    """Replace contiguous bitmap-font table blocks with a short placeholder."""
    out: list[str] = []
    block: list[str] = []

    def flush() -> None:
        if not block:
            return
        if _is_glyph_table_block(block):
            out.append("*(bitmap font table omitted)*")
        else:
            out.extend(block)
        block.clear()

    for line in text.split("\n"):
        if line.lstrip().startswith("|"):
            block.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return "\n".join(out)


def _collapse_blank_lines(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)  # trailing spaces
    text = re.sub(r"\n{3,}", "\n\n", text)                   # >2 blanks -> 1
    return text.strip("\n") + "\n"


def find_running_headers(
    pages: list[str], min_fraction: float = 0.6, max_len: int = 80
) -> set[str]:
    """Lines that recur (stripped) on at least `min_fraction` of a doc's pages.

    Catches near-universal running titles / footers / watermarks like
    'ESC/POS Command Specifications', 'Rev.2.52', or 'C O N F I D E N T I A L'.
    The fraction is deliberately high (0.6): a true footer appears on almost
    every page, whereas a recurring spec value or per-section label (e.g. jvc's
    '**Allowed users** admin, operator', ~51%) is content and must be kept.
    Only applied when a document has enough pages for the signal to be meaningful.
    """
    if len(pages) < 5:
        return set()
    counts: Counter[str] = Counter()
    for page in pages:
        seen = {
            ln.strip()
            for ln in page.split("\n")
            if 0 < len(ln.strip()) <= max_len
        }
        counts.update(seen)
    threshold = max(3, int(len(pages) * min_fraction))
    return {line for line, n in counts.items() if n >= threshold}


def clean(text: str, running_headers: set[str] | None = None) -> str:
    """Return `text` with the noise classes removed. Idempotent.

    `running_headers` are the doc-level repeated header/footer lines to strip
    (computed by find_running_headers from a document's per-page slices). They are
    matched by page *fraction*, which distinguishes a true running footer
    (on ~every page) from a spec value that merely recurs often.
    """
    text = _PICTURE_TEXT_BLOCK_RE.sub("", text)
    text = _PICTURE_TEXT_ORPHAN_RE.sub("", text)
    text = _PICTURE_PLACEHOLDER_RE.sub("", text)
    text = _strip_glyph_tables(text)

    headers = running_headers or set()
    kept: list[str] = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped and stripped in headers:
            continue
        if _is_pure_rule(line):
            continue
        if _PAGE_NUMBER_RE.match(line):
            continue
        if _WATERMARK_RE.search(line):
            line = re.sub(r"[ \t]{2,}", " ", _WATERMARK_RE.sub("", line))
            if _MARKUP_SHELL_RE.match(line):  # heading/emphasis emptied of text
                continue
            # Tidy the space the removed token left after a heading's emphasis
            # opener, e.g. "## ** Program example" -> "## **Program example".
            line = re.sub(r"(^#{1,6}\s+(?:\*{1,3}|_{1,3}))\s+", r"\1", line)
        line = _TRAILING_RULE_RE.sub("", line)  # drop footer glued onto content
        kept.append(line)

    return _collapse_blank_lines("\n".join(kept))


def _iter_doc_dirs(root: Path):
    """Yield (doc_dir, [page-*.md ...]) for every document directory under root."""
    docs: dict[Path, list[Path]] = {}
    for page_file in sorted(root.rglob("page-*.md")):
        docs.setdefault(page_file.parent, []).append(page_file)
    yield from docs.items()


def main(argv: list[str]) -> None:
    here = Path(__file__).resolve().parent.parent
    targets = [Path(a) for a in argv] or [here / "md", here / "md-bulk"]
    dirs = [t for t in targets if t.is_dir()]

    # Pass 1 — learn each document's running headers/footers from its per-page
    # slices (keyed by stem, e.g. "star/escpos_cm_en"), so bulk README.md files
    # in *either* tree can be deduped with the same signal.
    headers_by_stem: dict[str, set[str]] = {}
    for target in dirs:
        for doc_dir, page_files in _iter_doc_dirs(target):
            stem = doc_dir.relative_to(target).as_posix()
            headers_by_stem[stem] = find_running_headers(
                [p.read_text(encoding="utf-8") for p in page_files]
            )

    # Pass 2 — clean every Markdown file, applying its stem's header set.
    total_files = total_changed = 0

    def scrub(path: Path, headers: set[str]) -> None:
        nonlocal total_files, total_changed
        text = path.read_text(encoding="utf-8")
        cleaned = clean(text, headers)
        total_files += 1
        if cleaned != text:
            path.write_text(cleaned, encoding="utf-8")
            total_changed += 1

    for target in targets:
        if target.is_file():
            scrub(target, set())
        elif target.is_dir():
            for md_file in sorted(target.rglob("*.md")):
                stem = md_file.parent.relative_to(target).as_posix()
                scrub(md_file, headers_by_stem.get(stem, set()))
        else:
            print(f"skip (not found): {target}", file=sys.stderr)

    print(f"md_clean: {total_changed}/{total_files} file(s) changed.")


if __name__ == "__main__":
    main(sys.argv[1:])
