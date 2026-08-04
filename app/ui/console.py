class Console:
    """
    Gère les interactions console de l'application.
    """

    def display_welcome(self) -> None:
        """
        Affiche l'en-tête de démarrage.
        """
        print("=" * 40)
        print("        Bouamoud IA")
        print("=" * 40)

    def display_connection_status(self) -> None:
        """
        Affiche l'état de la connexion au fournisseur IA.
        """
        print("Connexion à Ollama : OK ✅")

    def get_user_input(self) -> str:
        """
        Lit la saisie utilisateur depuis la console.
        """
        return input("\nToi : ")

    def display_assistant_prefix(self) -> None:
        """
        Affiche le préfixe de réponse de l'assistant.
        """
        print("\nBouamoud IA : ", end="", flush=True)

    def display_stream_chunk(self, content: str) -> None:
        """
        Affiche un fragment de réponse sans retour à la ligne.
        """
        print(content, end="", flush=True)

    def display_newline(self) -> None:
        """
        Termine l'affichage de la réponse courante.
        """
        print()
