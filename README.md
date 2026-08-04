# AGENTS.md

# Bouamoud IA

## Vision

Bouamoud IA est un assistant IA personnel fonctionnant entièrement en local.

L'objectif n'est pas seulement de construire un chatbot, mais une plateforme modulaire capable de :

- discuter naturellement avec l'utilisateur ;
- mémoriser les conversations ;
- apprendre progressivement les préférences de l'utilisateur ;
- contrôler le poste de travail ;
- exécuter des actions ;
- rester indépendant du modèle de langage utilisé.

Le projet doit pouvoir évoluer pendant plusieurs années sans nécessiter de refonte complète.

---

# Philosophie

Le projet est développé comme un logiciel professionnel.

Nous privilégions :

- la lisibilité ;
- la simplicité ;
- la modularité ;
- les responsabilités uniques ;
- l'évolutivité.

Chaque décision d'architecture doit être prise dans l'objectif de faciliter les futures évolutions.

---

# Architecture

Le projet suit une architecture modulaire.

```
main.py
        │
        ▼
Assistant
        │
 ┌──────┼────────┐
 ▼      ▼        ▼
UI   Conversation Brain
                 │
                 ▼
            Ollama/OpenAI/...
```

Les composants doivent être faiblement couplés.

Une classe ne doit jamais dépendre directement d'une technologie lorsqu'une abstraction est possible.

---

# Structure du projet

```
Bouamoud-AI/

main.py

app/

    brain/
    config/
    conversation/
    core/
    models/
    services/
    ui/

tests/

README.md
requirements.txt
.env
.gitignore
AGENTS.md
```

---

# Responsabilités

## main.py

Point d'entrée de l'application.

Il ne contient aucune logique métier.

Il démarre uniquement Assistant.

---

## Assistant

Chef d'orchestre de l'application.

Responsabilités :

- démarrer l'application
- gérer la boucle principale
- coordonner les composants

Il ne contient aucun code spécifique à Ollama, Whisper, SQLite ou à la console.

---

## Brain

Responsable de la communication avec le modèle de langage.

Il doit être possible de remplacer facilement :

- Ollama
- LM Studio
- OpenAI
- tout autre fournisseur

sans modifier Assistant.

---

## Conversation

Responsable de la conversation courante.

Elle gère :

- les messages
- le contexte
- l'historique

Plus tard :

- résumé automatique
- mémoire
- récupération de contexte

---

## UI

Responsable des interactions avec l'utilisateur.

Exemples :

- console
- interface graphique
- interface web

La logique métier ne doit jamais être placée ici.

---

## Services

Contient les services métier.

Exemples futurs :

- SpeechService
- MemoryService
- PluginService
- DesktopService

---

## Models

Contient uniquement les objets métier.

Exemples :

- Message
- ConversationContext
- MemoryEntry

Les modèles ne contiennent aucune logique métier complexe.

---

# Principes de développement

Toujours respecter :

- SOLID
- DRY
- KISS

Une classe = une responsabilité.

Une méthode = une responsabilité.

---

# Taille des classes

Objectif :

- < 150 lignes

Maximum recommandé :

- 200 lignes

Si une classe devient trop grande :

→ la découper.

---

# Dépendances

Les dépendances doivent toujours pointer vers l'intérieur du projet.

Jamais l'inverse.

Éviter les dépendances circulaires.

---

# Git

Le développement est organisé en Sprints.

Chaque Sprint est découpé en plusieurs Tasks.

Une Task = un commit.

Exemples :

```
feat(core): initialize assistant

feat(conversation): add conversation manager

feat(memory): add SQLite persistence

refactor(core): simplify assistant workflow

fix(brain): handle Ollama timeout
```

Les commits "update", "test", "fix" sans contexte sont interdits.

---

# Workflow

Pour chaque fonctionnalité :

1. Analyse
2. Conception
3. Validation
4. Développement
5. Tests
6. Commit

Ne jamais coder directement sans conception.

---

# Tests

Toute fonctionnalité importante doit être testée avant son commit.

Les tests seront placés dans :

```
tests/
```

Utiliser :

- pytest

---

# Style Python

Respecter PEP8.

Utiliser :

- type hints
- dataclasses lorsque pertinent
- docstrings sur les classes publiques

Éviter les fonctions de plus de 40 lignes.

---

# Linting

Le projet utilisera :

- Ruff
- Black

Le code doit être formaté avant chaque commit.

---

# Intelligence Artificielle

Le modèle IA n'est qu'un fournisseur.

Le projet ne doit jamais être dépendant d'un modèle spécifique.

Aujourd'hui :

- Gemma

Demain :

- Qwen
- Llama
- OpenAI
- LM Studio

Le changement de modèle doit nécessiter un minimum de modifications.

---

# Roadmap

Sprint 1

- Ollama
- Premier échange

Sprint 2

- Architecture

Sprint 3

- Conversation persistante

Sprint 4

- Mémoire SQLite

Sprint 5

- Voix

Sprint 6

- Contrôle du poste

Sprint 7

- Plugins

Sprint 8

- Interface graphique

---

# Objectif final

Bouamoud IA doit devenir un véritable assistant personnel capable de :

- discuter naturellement
- mémoriser les informations importantes
- apprendre les habitudes de l'utilisateur
- exécuter des actions
- fonctionner entièrement en local
- rester modulaire et évolutif

La priorité est toujours donnée à la qualité de l'architecture plutôt qu'à la rapidité de développement.

Le projet est conçu pour être maintenable sur le long terme.
