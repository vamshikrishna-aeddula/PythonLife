# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 40 - Roman Numeral Converter with Validation (PythonLife)

What it does : integers 1-3999 <-> Roman numerals; rejects invalid ones like "IIII".
Concepts     : greedy algorithm, lists of tuples, round-trip validation.
Run          : python 40_roman_numerals.py    (add --demo for a sample run)
"""
from pythonlife import run, ask

PAIRS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("number must be between 1 and 3999")
    out = []
    for value, symbol in PAIRS:
        count, number = divmod(number, value)
        out.append(symbol * count)
    return "".join(out)


def from_roman(text):
    text = text.strip().upper()
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not text or any(ch not in values for ch in text):
        raise ValueError("only the letters I V X L C D M are allowed")
    total = 0
    for i, ch in enumerate(text):
        v = values[ch]
        total += -v if i + 1 < len(text) and values[text[i + 1]] > v else v
    if to_roman(total) != text:                    # round-trip proves it is written correctly
        raise ValueError(f"'{text}' is not a correctly written Roman numeral")
    return total


def main():
    while True:
        text = ask("Number or Roman numeral (blank to quit): ")
        if not text:
            break
        try:
            print("  ->", to_roman(int(text)) if text.isdigit() else from_roman(text))
        except ValueError as err:
            print("  Oops:", err)


def demo():
    for n in (4, 9, 14, 49, 1994, 2026, 3999):
        print(f"{n:>4} = {to_roman(n)}")
    print("MCMXCIV =", from_roman("MCMXCIV"))
    try:
        from_roman("IIII")
    except ValueError as err:
        print("IIII ->", err)


if __name__ == "__main__":
    run(40, "Roman Numeral Converter", main, demo)
