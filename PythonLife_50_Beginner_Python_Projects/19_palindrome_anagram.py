# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 19 - Palindrome & Anagram Toolkit (PythonLife)

What it does : checks palindromes ("Never odd or even"), checks if two phrases
               are anagrams, and groups a word list into anagram families.
Concepts     : string cleaning, sorted(), dictionaries of lists (defaultdict).
Run          : python 19_palindrome_anagram.py (add --demo for a sample run)
"""
from collections import defaultdict
from pythonlife import run, ask


def clean(text):
    return "".join(ch.lower() for ch in text if ch.isalnum())


def is_palindrome(text):
    c = clean(text)
    return c != "" and c == c[::-1]


def are_anagrams(a, b):
    return clean(a) != "" and sorted(clean(a)) == sorted(clean(b))


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(clean(w)))].append(w)
    return [g for g in groups.values() if len(g) > 1]


def main():
    while True:
        text = ask("Phrase (blank to quit): ")
        if not text:
            break
        print("  Palindrome!" if is_palindrome(text) else "  Not a palindrome.")
        other = ask("  Second phrase to test as anagram (Enter to skip): ")
        if other:
            print("  Anagrams!" if are_anagrams(text, other) else "  Not anagrams.")


def demo():
    for phrase in ["Never odd or even", "A man, a plan, a canal: Panama", "PythonLife"]:
        print(f"{phrase!r:35} palindrome? {is_palindrome(phrase)}")
    print("listen / silent anagrams?", are_anagrams("listen", "silent"))
    print("Groups:", group_anagrams(["listen", "silent", "enlist", "google", "gogole", "cat", "act", "dog"]))


if __name__ == "__main__":
    run(19, "Palindrome & Anagram Toolkit", main, demo)
