import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"CREATED: {path}")

def main():
    project_name = "aether_v4_baseline"
    print(f"--- Initializing {project_name} ---")

    # 1. CORE CONFIGURATION
    create_file(f"{project_name}/requirements.txt", """
pytest==8.0.0
black==24.1.1
""")

    create_file(f"{project_name}/main.py", """
from app.cli import main
if __name__ == "__main__":
    main()
""")

    # 2. FRAMEWORK ENGINE (.ai/)
    create_file(f"{project_name}/.ai/system_state/current_iteration.json", """
{
  "project_name": "Flash-AI",
  "framework_version": "4.0.0",
  "current_phase": "Baseline Established",
  "status": "MISSION ACCOMPLISHED"
}
""")

    create_file(f"{project_name}/.ai/rules_v5.md", """
# AETHER Meta-Framework Rules (v5.0.0)

## Section 1: SDLC Integrity
- Mandatory Gates: Requirements -> Analysis -> Design -> TDD -> Implementation.
- Halt & Verify: Stop and wait for "APPROVED" before moving to the next gate.

## Section 2: Cognitive Protocols
- Triad Review: Perspectives from [Architect], [Security/QA], and [Implementer].
- Scoping Logic: Justify scope based on DDD and YAGNI.

## Section 3: Resilience & Evolution
- Diagnosis First: Provide a "Diagnostic Report" before fixing failed tests.
- Self-Evolution: Perform a "Framework Audit" to mutate rules for efficiency.
""")

    create_file(f"{project_name}/.ai/PORTABLE_SYSTEM_PROMPT.md", """
# AETHER Ignition Prompt
Acknowledge ADMF protocols. Guide through Requirements -> Design -> TDD.
Enforce Triad Review and Diagnosis-First.
""")

    # 3. APP IMPLEMENTATION
    create_file(f"{project_name}/app/__init__.py", "")
    
    create_file(f"{project_name}/app/models.py", """
from dataclasses import dataclass

@dataclass
class Flashcard:
    question: str
    answer: str

    def __post_init__(self):
        if not self.question or not self.answer:
            raise ValueError("Question and Answer cannot be empty.")
""")

    create_file(f"{project_name}/app/repository.py", """
import json
import os
from app.models import Flashcard

class FlashcardRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_all(self, cards):
        data = [{"question": c.question, "answer": c.answer} for c in cards]
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_all(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return [Flashcard(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            print("Warning: Data file corrupt. Starting fresh.")
            return []
""")

    create_file(f"{project_name}/app/cli.py", """
import argparse
import random
from app.models import Flashcard
from app.repository import FlashcardRepository

def main():
    repo = FlashcardRepository("flashcards.json")
    parser = argparse.ArgumentParser(description="AETHER Flash-AI")
    subparsers = parser.add_subparsers(dest="command")

    add_p = subparsers.add_parser("add")
    add_p.add_argument("--q", required=True)
    add_p.add_argument("--a", required=True)

    subparsers.add_parser("review")

    args = parser.parse_args()

    if args.command == "add":
        cards = repo.load_all()
        cards.append(Flashcard(args.q, args.a))
        repo.save_all(cards)
        print(f"Added: {args.q}")
    elif args.command == "review":
        cards = repo.load_all()
        if not cards: return print("No cards!")
        card = random.choice(cards)
        print(f"Q: {card.question}")
        input("Reveal?")
        print(f"A: {card.answer}")
""")

    # 4. TESTS
    create_file(f"{project_name}/tests/__init__.py", "")
    create_file(f"{project_name}/tests/test_domain.py", """
import pytest
from app.models import Flashcard

def test_flashcard_creation():
    card = Flashcard("Q", "A")
    assert card.question == "Q"

def test_flashcard_validation():
    with pytest.raises(ValueError):
        Flashcard("", "A")
""")

    # 5. DOCUMENTATION
    create_file(f"{project_name}/docs/tutorial/MASTER_LOG.md", """
# AETHER MASTER LOG
## Phase 1-4: Framework Initialization Complete.
- Smoke Test 'Flash-AI' successfully verified.
- AETHER v4.0.0 Baseline established.
""")

    create_file(f"{project_name}/USER_GUIDE.md", """
# Flash-AI Guide
Usage: `python3 main.py add --q "Question" --a "Answer"`
Review: `python3 main.py review`
""")

    print(f"--- SUCCESS: AETHER v4.0.0 is ready in ./{project_name} ---")

if __name__ == "__main__":
    main()
