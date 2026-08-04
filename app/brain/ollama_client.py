from ollama import Client

from app.config.settings import OLLAMA_HOST

from collections.abc import Iterator

from typing import Any

class OllamaClient:

    def __init__(self):
        self.client = Client(host=OLLAMA_HOST)

    def chat(self, model: str, messages: list[dict], stream: bool = False) -> Any:
        return self.client.chat(
            model=model,
            messages=messages,
            stream=stream
        )

    def stream_chat(self, model: str, messages: list[dict]) -> Iterator[str]:
        stream = self.client.chat(
            model=model,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            content = chunk.message.content

            if content is not None:
                yield content