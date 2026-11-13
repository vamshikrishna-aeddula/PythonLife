# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 01 - Tip & Bill Splitter (PythonLife)

What it does : splits a restaurant bill (with tip) between friends.
Concepts     : functions, dictionaries, input validation, round().
Run          : python 01_tip_splitter.py      (add --demo for a sample run)
"""
from pythonlife import run, ask_float, ask_int


def split_bill(amount, tip_percent, people):
    """Return the tip, total and each person's share (2 decimals)."""
    if amount < 0 or tip_percent < 0 or people < 1:
        raise ValueError("amount/tip cannot be negative and people must be >= 1")
    tip = round(amount * tip_percent / 100, 2)
    total = round(amount + tip, 2)
    return {"bill": amount, "tip": tip, "total": total,
            "per_person": round(total / people, 2)}


def show(result, people):
    print(f"Bill: {result['bill']:.2f} | Tip: {result['tip']:.2f} | Total: {result['total']:.2f}")
    print(f"Each of {people} people pays: {result['per_person']:.2f}")


def main():
    amount = ask_float("Bill amount: ", 0)
    tip = ask_float("Tip % (e.g. 10): ", 0)
    people = ask_int("Number of people: ", 1)
    show(split_bill(amount, tip, people), people)


def demo():
    show(split_bill(1250, 10, 4), 4)


if __name__ == "__main__":
    run(1, "Tip & Bill Splitter", main, demo)
