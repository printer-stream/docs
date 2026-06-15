"""Document summarisation.

Default backend is a local instruction-tuned seq2seq model (flan-t5) driven
directly via transformers — no external API, and no dependency on the
`pipeline` task registry (whose task names vary across transformers versions).
If the backend is 'extractive', or the model fails to load, it falls back to a
zero-dependency extractive summary (title + leading text). The summary is
stored per document and embedded as a 'summary' chunk so conceptual
'what covers X' queries retrieve whole documents.
"""
from __future__ import annotations

import logging
from functools import lru_cache

from config import cfg
from corpus import Document

log = logging.getLogger("printer-stream-docs.summarizer")

# flan-t5 follows instructions, so we ask directly for the facets we index on.
_INSTRUCTION = (
    "Summarise in 2-4 sentences which devices, models, protocols and command "
    "sets this printer/device document covers, and who would use it."
)
# flan-t5's input window is 512 tokens; cap the source so truncation is
# predictable (leading pages carry the title/overview that matters here).
_MAX_SOURCE_CHARS = 4000
_MAX_INPUT_TOKENS = 512
_MAX_NEW_TOKENS = 160


@lru_cache(maxsize=1)
def _model_and_tokenizer():
    """Load the seq2seq model + tokenizer once (lazy: only when first needed)."""
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    log.info("Loading local summarisation model '%s'...", cfg.summary_model)
    tokenizer = AutoTokenizer.from_pretrained(cfg.summary_model)
    model = AutoModelForSeq2SeqLM.from_pretrained(cfg.summary_model)
    model.eval()
    return tokenizer, model


def _source_text(doc: Document) -> str:
    return "\n".join(p.text for p in doc.pages[:3])[:_MAX_SOURCE_CHARS]


def _extractive(doc: Document, source: str) -> str:
    snippet = " ".join(source.split())[:500]
    return f"{doc.title}. {snippet}"


def summarize(doc: Document) -> str:
    """Return a one-paragraph 'what this document covers' blurb."""
    source = _source_text(doc)
    if cfg.summary_backend == "extractive":
        return _extractive(doc, source)

    try:
        import torch

        tokenizer, model = _model_and_tokenizer()
        prompt = f"{_INSTRUCTION}\n\nTitle: {doc.title}\n\n{source}"
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=_MAX_INPUT_TOKENS,
        )
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=_MAX_NEW_TOKENS,
                num_beams=4,
                no_repeat_ngram_size=3,
            )
        text = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
        return text or _extractive(doc, source)
    except Exception as exc:  # noqa: BLE001 - never fail the build on summaries
        log.warning("Local summariser failed (%s); using extractive fallback", exc)
        return _extractive(doc, source)
