# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 14 - Hangman: Python Vocabulary Edition (PythonLife)

What it does : guess the hidden Python term letter by letter.
Concepts     : classes, properties, sets, game loops.
Run          : python 14_hangman.py           (add --demo for a sample run)
"""
import random
from pythonlife import run, ask

WORDS = ["variable", "function", "tuple", "dictionary", "iterator", "decorator", "module",
         "package", "loop", "string", "integer", "boolean", "exception", "lambda", "class"]


class Hangman:
    def __init__(self, word, max_wrong=6):
        self.word, self.max_wrong = word.lower(), max_wrong
        self.correct, self.wrong = set(), set()

    def guess(self, letter):
        """Return 'hit', 'miss' or 'repeat'."""
        letter = letter.lower()
        if letter in self.correct or letter in self.wrong:
            return "repeat"
        if letter in self.word:
            self.correct.add(letter)
            return "hit"
        self.wrong.add(letter)
        return "miss"

    @property
    def masked(self):
        return " ".join(c if c in self.correct else "_" for c in self.word)

    @property
    def won(self):
        return all(c in self.correct for c in self.word)

    @property
    def lost(self):
        return len(self.wrong) >= self.max_wrong

    def status(self):
        return f"{self.masked}   wrong ({len(self.wrong)}/{self.max_wrong}): {' '.join(sorted(self.wrong))}"


def main():
    game = Hangman(random.choice(WORDS))
    while not (game.won or game.lost):
        print(game.status())
        letter = ask("Guess a letter: ")
        if len(letter) == 1 and letter.isalpha():
            if game.guess(letter) == "repeat":
                print("  Already tried that one.")
        else:
            print("  One letter please.")
    print("You win!" if game.won else f"You lost. The word was '{game.word}'.", game.masked)


def demo():
    game = Hangman("decorator")
    for letter in "etaoinsrdcpq":
        if game.won or game.lost:
            break
        print(f"guess '{letter}' -> {game.guess(letter):<6} {game.status()}")
    print("Result:", "WON" if game.won else "LOST")


if __name__ == "__main__":
    run(14, "Hangman - Python Vocabulary", main, demo)
