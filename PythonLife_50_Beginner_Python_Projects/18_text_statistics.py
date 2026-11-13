# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 18 - Text Statistics & Reading-Time Analyzer (PythonLife)

What it does : counts words/sentences, finds the longest and most common words,
               and estimates reading time for any text or .txt file.
Concepts     : re, Counter, file reading, sets for stop-words.
Run          : python 18_text_statistics.py   (add --demo for a sample run)
"""
import re
from collections import Counter
from pathlib import Path
from pythonlife import run, ask

STOP = {"the", "a", "an", "and", "or", "of", "to", "in", "is", "it", "that", "for",
        "on", "with", "as", "was", "are", "be", "this", "by", "at", "from"}


def analyze(text):
    words = re.findall(r"[A-Za-z']+", text.lower())
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "avg_word_length": round(sum(map(len, words)) / len(words), 2) if words else 0,
        "longest_word": max(words, key=len, default=""),
        "top_words": Counter(w for w in words if w not in STOP).most_common(5),
        "reading_minutes": round(len(words) / 200, 1),       # ~200 words per minute
    }


def show(stats):
    for key, value in stats.items():
        print(f"  {key:<16}: {value}")


def main():
    source = ask("Path to a .txt file (or press Enter to type text): ")
    text = Path(source).read_text(encoding="utf-8") if source else ask("Type your text: ")
    show(analyze(text))


SAMPLE = ("Python is a friendly language. Python is used for web apps, data science and automation! "
          "Learning Python step by step with projects makes the language easy to remember.")


def demo():
    show(analyze(SAMPLE))


if __name__ == "__main__":
    run(18, "Text Statistics Analyzer", main, demo)
