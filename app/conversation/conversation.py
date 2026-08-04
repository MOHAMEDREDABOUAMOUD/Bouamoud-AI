from typing import List

from app.models.message import Message

from app.config.prompts import SYSTEM_PROMPT

class Conversation:
    """
    Représente une conversation entre l'utilisateur et Bouamoud IA.
    """

    def __init__(self) -> None:
        self._messages = [
            Message(
                role="system",
                content=SYSTEM_PROMPT
            )
        ]

    def add_message(self, role: str, content: str) -> None:
        self._messages.append(
            Message(
                role=role,
                content=content
            )
        )

    def add_user_message(self, content: str) -> None:
        """
        Ajoute un message utilisateur.
        """
        self.add_message("user", content)

    def add_assistant_message(self, content: str) -> None:
        """
        Ajoute un message de l'assistant.
        """
        self.add_message("assistant", content)

    def get_messages(self) -> List[Message]:
        """
        Retourne tous les messages.
        """
        return self._messages.copy()

    def get_messages_as_dict(self) -> List[dict]:
        """
        Retourne les messages au format attendu par Ollama.
        """
        return [message.to_dict() for message in self._messages]

    def clear(self) -> None:
        """
        Vide la conversation.
        """
        self._messages.clear()

    def is_empty(self) -> bool:
        """
        Indique si la conversation est vide.
        """
        return len(self._messages) == 0

    def size(self) -> int:
        """
        Retourne le nombre de messages.
        """
        return len(self._messages)