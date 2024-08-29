from __future__ import annotations

from .Openai import Openai
from ...typing import AsyncResult, Messages

class Groq(Openai):
    label = "Groq"
    url = "https://console.groq.com/playground"
    working = True
    default_model = "mixtral-8x7b-32768"
    models = ["mixtral-8x7b-32768", "gemma-7b-it","distil-whisper-large-v3-en","gemma2-9b-it","gemma-7b-it","llama3-groq-70b-8192-tool-use-preview","llama3-groq-8b-8192-tool-use-preview","llama-3.1-70b-versatile","llama-3.1-8b-instant","llama-guard-3-8b","llama3-70b-8192","llama3-8b-8192","whisper-large-v3"]
    model_aliases = {"mixtral-8x7b": "mixtral-8x7b-32768"}

    @classmethod
    def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        api_base: str = "https://api.groq.com/openai/v1",
        **kwargs
    ) -> AsyncResult:
        return super().create_async_generator(
            model, messages, api_base=api_base, **kwargs
        )