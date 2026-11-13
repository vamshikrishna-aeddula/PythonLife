# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 21 - Morse Code Translator (PythonLife)

What it does : text -> Morse and Morse -> text (letters and digits).
Concepts     : dictionary, reversing a dictionary, split/join.
Format       : letters separated by a space, words by ' / '.
Run          : python 21_morse_code.py        (add --demo for a sample run)
"""
from pythonlife import run, ask, choose

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}
REVERSE = {code: ch for ch, code in MORSE.items()}


def to_morse(text):
    words = []
    for word in text.upper().split():
        words.append(" ".join(MORSE[ch] for ch in word if ch in MORSE))
    return " / ".join(w for w in words if w)


def from_morse(code):
    words = []
    for word in code.strip().split(" / "):
        words.append("".join(REVERSE.get(sym, "?") for sym in word.split()))
    return " ".join(words)


def main():
    while True:
        pick = choose(["Text to Morse", "Morse to text"])
        if pick == 0:
            break
        text = ask("Input: ")
        print(to_morse(text) if pick == 1 else from_morse(text))


def demo():
    code = to_morse("Python Life 2026")
    print(code)
    print(from_morse(code))


if __name__ == "__main__":
    run(21, "Morse Code Translator", main, demo)
