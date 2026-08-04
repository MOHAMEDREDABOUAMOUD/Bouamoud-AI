from app.brain.ollama_client import OllamaClient
from app.config.settings import MODEL_NAME


def main():

    print("=" * 40)
    print("        Bouamoud IA")
    print("=" * 40)

    client = OllamaClient()

    print("Connexion à Ollama : OK ✅")

    while True:

        question = input("\nToi : ")

        if question.lower() in ["exit", "quit"]:
            break

        print("\nBouamoud IA : ", end="", flush=True)

        for chunk in client.stream_chat(MODEL_NAME, question):
            print(chunk["message"]["content"], end="", flush=True)

        print()


if __name__ == "__main__":
    main()