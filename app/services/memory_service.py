from datetime import datetime
from pathlib import Path
import sqlite3

from app.models.memory import Memory


class MemoryService:

    def __init__(self) -> None:
        self.database_path = Path("bouamoud.db")

    def should_remember(self, text: str) -> bool:
        """
        Détermine si un message mérite d'être mémorisé.
        """
        keywords = [
            "je m'appelle",
            "mon nom est",
            "je suis",
            "j'habite",
            "je travaille",
            "je préfère",
            "mon projet",
        ]

        text = text.lower()

        return any(keyword in text for keyword in keywords)

    def remember(self, text: str) -> None:
        """
        Sauvegarde une mémoire si elle est jugée importante.
        """
        if not self.should_remember(text):
            return

        memory = Memory(
            id=None,
            category="identity",
            content=text,
            created_at=datetime.now(),
        )

        self.save(memory)

    def _connect(self) -> sqlite3.Connection:
        """
        Crée une connexion vers la base de données.
        """
        return sqlite3.connect(self.database_path)

    def initialize(self) -> None:
        """
        Initialise la base de données SQLite.
        """
        with self._connect() as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    category TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)

    def save(self, memory: Memory) -> None:
        """
        Sauvegarde une mémoire.
        """
        with self._connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO memories (
                    content,
                    category,
                    created_at
                )
                VALUES (?, ?, ?)
                """,
                (
                    memory.content,
                    memory.category,
                    memory.created_at.isoformat(),
                ),
            )

    def load(self) -> list[Memory]:
        """
        Charge toutes les mémoires.
        """
        with self._connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    id,
                    content,
                    category,
                    created_at
                FROM memories
                ORDER BY created_at ASC
                """
            )

            rows = cursor.fetchall()

        memories: list[Memory] = []

        for row in rows:
            memories.append(
                Memory(
                    id=row[0],
                    category=row[2],
                    content=row[1],
                    created_at=datetime.fromisoformat(row[3]),
                )
            )

        return memories

    def clear(self) -> None:
        """
        Supprime toutes les mémoires.
        """
        with self._connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM memories
                """
            )