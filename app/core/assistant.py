from app.brain.ollama_client import OllamaClient
from app.config.settings import MODEL_NAME
from app.conversation.conversation import Conversation
from app.ui.console import Console


class Assistant:

    def __init__(self) -> None:
        self.console = Console()
        self.conversation = Conversation()
        self.brain = OllamaClient()

    def run(self) -> None:
        self.console.display_welcome()
        self.console.display_connection_status()

        while True:

            question = self.console.get_user_input()

            if question.lower() in ["exit", "quit"]:
                break

            self.conversation.add_user_message(question)

            messages = self.conversation.get_messages_as_dict()

            self.console.display_assistant_prefix()

            response = ""

            for chunk in self.brain.stream_chat(MODEL_NAME, messages):
                response += chunk
                self.console.display_stream_chunk(chunk)

            self.conversation.add_assistant_message(response)

            self.console.display_newline()