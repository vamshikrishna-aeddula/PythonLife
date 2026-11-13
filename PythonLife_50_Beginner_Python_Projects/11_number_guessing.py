# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 11 - Number Guessing Game + Smart Bot (PythonLife)

What it does : you guess a secret number; a bot shows the fastest strategy.
Concepts     : random, while loops, binary search (why it needs <= 7 guesses for 1-100).
Run          : python 11_number_guessing.py   (add --demo for a sample run)
"""
import random
from pythonlife import run, ask_int


def evaluate_guess(secret, guess):
    return "low" if guess < secret else "high" if guess > secret else "correct"


def bot_play(secret, low=1, high=100):
    """Binary search: always guess the middle. Returns the list of guesses."""
    guesses = []
    while True:
        guess = (low + high) // 2
        guesses.append(guess)
        result = evaluate_guess(secret, guess)
        if result == "correct":
            return guesses
        low, high = (guess + 1, high) if result == "low" else (low, guess - 1)


def main():
    secret, tries = random.randint(1, 100), 0
    print("I am thinking of a number from 1 to 100. You have 7 tries.")
    while tries < 7:
        guess = ask_int(f"Guess #{tries + 1}: ")
        tries += 1
        result = evaluate_guess(secret, guess)
        if result == "correct":
            print(f"Correct! You needed {tries} tries.")
            return
        print("Too low!" if result == "low" else "Too high!")
    print(f"Out of tries. The number was {secret}. Bot would solve it in {len(bot_play(secret))}.")


def demo():
    secret = random.Random(42).randint(1, 100)
    path = bot_play(secret)
    print(f"Secret = {secret}. Bot guesses: {path}  ({len(path)} tries)")


if __name__ == "__main__":
    run(11, "Number Guessing Game + Smart Bot", main, demo)
