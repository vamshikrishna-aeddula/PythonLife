# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 12 - Rock Paper Scissors with Scoreboard (PythonLife)

What it does : play best-of-N against the computer and see the final score.
Concepts     : dictionaries for rules, random.choice, collections.Counter.
Run          : python 12_rock_paper_scissors.py (add --demo for a sample run)
"""
import random
from collections import Counter
from pythonlife import run, ask, ask_int

BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def winner(player, computer):
    """Return 'tie', 'player' or 'computer'."""
    if player == computer:
        return "tie"
    return "player" if BEATS[player] == computer else "computer"


def play_rounds(moves, rng):
    score = Counter()
    for move in moves:
        comp = rng.choice(list(BEATS))
        result = winner(move, comp)
        score[result] += 1
        print(f"You: {move:<8} Computer: {comp:<8} -> {result}")
    return score


def main():
    rounds = ask_int("How many rounds? ", 1)
    moves = []
    while len(moves) < rounds:
        move = ask("rock / paper / scissors: ").lower()
        if move in BEATS:
            moves.append(move)
        else:
            print("  Type rock, paper or scissors.")
    # play live so the user sees results; reuse the same function
    score = play_rounds(moves, random.Random())
    print(f"Final -> You {score['player']}, Computer {score['computer']}, Ties {score['tie']}")


def demo():
    score = play_rounds(["rock", "paper", "scissors", "rock", "paper"], random.Random(7))
    print(f"Final -> You {score['player']}, Computer {score['computer']}, Ties {score['tie']}")


if __name__ == "__main__":
    run(12, "Rock Paper Scissors", main, demo)
