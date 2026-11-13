# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 17 - Spaced-Repetition Flashcards (Leitner Box) (PythonLife)

What it does : cards you know move to higher boxes and appear less often;
               cards you miss return to box 1 - the science of remembering.
Concepts     : classes, dictionaries, modulo, simulation.
Run          : python 17_flashcards.py        (add --demo for a sample run)
"""
from pythonlife import run, ask

CARDS = {
    "What does len() return?": "The number of items",
    "Which keyword starts a function?": "def",
    "What is a list comprehension?": "A short way to build a list from a loop",
    "What does 'import' do?": "Loads a module so you can use it",
    "What is the result of 7 // 2?": "3 (floor division)",
    "What is a dictionary?": "Key-value pairs",
    "What does 'pip install' do?": "Installs a package",
    "What is PEP 8?": "The Python style guide",
}
INTERVAL = {1: 1, 2: 2, 3: 4}          # box -> review every N days


class Deck:
    def __init__(self, cards):
        self.cards = dict(cards)
        self.box = {q: 1 for q in self.cards}

    def due(self, day):
        """Cards to review on this day (day 1, 2, 3...)."""
        return [q for q, b in self.box.items() if (day - 1) % INTERVAL[b] == 0]

    def review(self, question, knew_it):
        self.box[question] = min(self.box[question] + 1, 3) if knew_it else 1

    def summary(self):
        return {b: sum(1 for v in self.box.values() if v == b) for b in (1, 2, 3)}


def main():
    deck, day = Deck(CARDS), 1
    while True:
        due = deck.due(day)
        print(f"\n--- Day {day}: {len(due)} cards due ---")
        for q in due:
            print("Q:", q)
            ask("   (press Enter to reveal) ")
            print("A:", deck.cards[q])
            deck.review(q, ask("   Did you know it? (y/n): ").lower().startswith("y"))
        print("Boxes:", deck.summary())
        if ask("Next day? (y/n): ").lower() != "y":
            break
        day += 1


def demo():
    deck = Deck(CARDS)
    questions = list(CARDS)
    for day in range(1, 5):
        due = deck.due(day)
        for i, q in enumerate(due):
            deck.review(q, knew_it=(i % 3 != 0))      # pretend we miss every 3rd card
        print(f"Day {day}: reviewed {len(due)} cards -> boxes {deck.summary()}")
    assert len(questions) == sum(deck.summary().values())


if __name__ == "__main__":
    run(17, "Spaced-Repetition Flashcards", main, demo)
