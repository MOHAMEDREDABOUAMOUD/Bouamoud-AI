from app.core.assistant import Assistant
from app.services.memory_service import MemoryService


def main() -> None:
    assistant = Assistant()

    service = MemoryService()

    for memory in service.load():
        print(memory)
    assistant.run()


if __name__ == "__main__":
    main()