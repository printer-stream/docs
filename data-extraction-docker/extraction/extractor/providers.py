"""Shared OpenAI-compatible LLM/VLM client.

Every model-bearing backend (markdown-vlm, describe, quality-judge, sections-llm)
goes through this one client, so providers are swapped by config, not code. Works
against any OpenAI-compatible /chat/completions endpoint - local vLLM/Ollama or a
hosted API. Stdlib only (urllib); no SDK dependency.
"""

from __future__ import annotations

import base64
import json
import logging
import os
import urllib.request
from typing import Dict, List, Optional

from .config import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)


class LLMClient:
    def __init__(
        self, base_url: str, model: str, api_key: str = "",
        timeout: int = 180, max_tokens: int = 1024, temperature: float = 0.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.endpoint = self.base_url + "/chat/completions"
        self.model = model
        self.api_key = api_key or ""
        self.timeout = int(timeout)
        self.max_tokens = int(max_tokens)
        self.temperature = float(temperature)

    def chat(self, messages: List[Dict], max_tokens: Optional[int] = None,
             temperature: Optional[float] = None) -> str:
        payload = {
            "model": self.model,
            "temperature": self.temperature if temperature is None else temperature,
            "max_tokens": self.max_tokens if max_tokens is None else max_tokens,
            "messages": messages,
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

    @staticmethod
    def text_part(text: str) -> Dict:
        return {"type": "text", "text": text}

    @staticmethod
    def image_part(image_bytes: bytes, mime: str = "image/jpeg") -> Dict:
        data = base64.b64encode(image_bytes).decode("ascii")
        return {"type": "image_url", "image_url": {"url": "data:%s;base64,%s" % (mime, data)}}

    def vision(self, prompt: str, image_bytes: bytes, mime: str = "image/jpeg", **kw) -> str:
        return self.chat(
            [{"role": "user", "content": [self.text_part(prompt), self.image_part(image_bytes, mime)]}],
            **kw,
        )

    def text_only(self, prompt: str, **kw) -> str:
        return self.chat([{"role": "user", "content": prompt}], **kw)


def client_from(provider: Optional[Dict]) -> LLMClient:
    """Build a client from a profile [<phase>.provider] block. The API key is
    read from the env var named by `api_key_env` (secrets never live in profiles)."""
    if not provider or not provider.get("base_url") or not provider.get("model"):
        raise SystemExit(
            "this phase needs a [<phase>.provider] block with base_url and model in the profile"
        )
    api_key = ""
    env_name = provider.get("api_key_env")
    if env_name:
        api_key = os.environ.get(env_name, "")
    return LLMClient(
        base_url=provider["base_url"],
        model=provider["model"],
        api_key=api_key,
        timeout=provider.get("timeout", 180),
        max_tokens=provider.get("max_tokens", 1024),
        temperature=provider.get("temperature", 0.0),
    )
