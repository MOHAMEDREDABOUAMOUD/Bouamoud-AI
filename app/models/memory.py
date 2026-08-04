from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Memory:
    """
    Représente une information enregistrée en mémoire.
    """

    id: int | None
    category: str
    content: str
    created_at: datetime