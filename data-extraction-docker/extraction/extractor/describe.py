"""Optional VLM page descriptions (the `describe` phase).

Gives figure/diagram/low-text pages a searchable text surface the keyword index
can see, improving recall. Descriptions are a clearly separate, supplementary
signal - never merged into the authoritative markdown.

Provider-pluggable via any OpenAI-compatible chat/completions endpoint (a local
vLLM serving e.g. Qwen2.5-VL, or a cheap hosted vision model). Stdlib only.
"""

from __future__ import annotations

import base64
import json
import logging
import urllib.error
import urllib.request

from .config import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

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


class DescribeClient:
    """Minimal OpenAI-compatible vision client (chat/completions)."""

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str = "",
        timeout: int = 120,
        max_tokens: int = 320,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.endpoint = self.base_url + "/chat/completions"
        self.model = model
        self.api_key = api_key
        self.timeout = timeout
        self.max_tokens = max_tokens

    def describe_image(self, image_bytes: bytes, mime: str = "image/jpeg") -> str:
        data_url = "data:%s;base64,%s" % (mime, base64.b64encode(image_bytes).decode("ascii"))
        payload = {
            "model": self.model,
            "temperature": 0,
            "max_tokens": self.max_tokens,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": PROMPT},
                        {"type": "image_url", "image_url": {"url": data_url}},
                    ],
                }
            ],
        }
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = "Bearer " + self.api_key
        req = urllib.request.Request(
            self.endpoint, data=json.dumps(payload).encode("utf-8"), headers=headers
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        return (body["choices"][0]["message"]["content"] or "").strip()
