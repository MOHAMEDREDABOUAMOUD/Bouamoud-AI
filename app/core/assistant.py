from app.brain.ollama_client import OllamaClient
from app.config.settings import MODEL_NAME
from app.conversation.conversation import Conversation
from app.ui.console import Console
from app.services.memory_service import MemoryService


class Assistant:

    def __init__(self) -> None:
        self.console = Console()
        self.conversation = Conversation()
        self.brain = OllamaClient()
        self.memory_service = MemoryService()
        self.memory_service.initialize()
        memories = self.memory_service.load()

        if memories:
            content = "Informations connues sur l'utilisateur :\n\n"

            for memory in memories:
                content += f"- {memory.content}\n"

            self.conversation.add_system_message(content)

    def run(self) -> None:
        self.console.display_welcome()
        self.console.display_connection_status()

        while True:

            question = self.console.get_user_input()

            if question.lower() in ["exit", "quit"]:
                break

            self.conversation.add_user_message(question)

            self.memory_service.remember(question)

            messages = self.conversation.get_messages_as_dict()

            self.console.display_assistant_prefix()

            response = ""

            for chunk in self.brain.stream_chat(MODEL_NAME, messages):
                response += chunk
                self.console.display_stream_chunk(chunk)

            self.conversation.add_assistant_message(response)

            self.console.display_newline()