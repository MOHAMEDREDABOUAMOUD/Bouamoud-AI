from dataclasses import dataclass


@dataclass(slots=True)
class Message:
    """
    Représente un message d'une conversation.
    """

    role: str
    content: str

    def to_dict(self) -> dict:
        """
        Convertit le message au format attendu par Ollama.
        """
        return {
            "role": self.role,
            "content": self.content,
        }