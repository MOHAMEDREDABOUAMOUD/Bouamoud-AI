from ollama import Client

from app.config.settings import OLLAMA_HOST


class OllamaClient:

    def __init__(self):
        self.client = Client(host=OLLAMA_HOST)

    def chat(self, model: str, message: str, stream: bool = False):

        return self.client.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            stream=stream
        )
    
    def stream_chat(self, model: str, message: str):
        return self.client.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            stream=True
        )