# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 16 - Python Basics Quiz (PythonLife)

What it does : 10-question multiple-choice quiz with explanations and a score.
Concepts     : list of dictionaries, enumerate, grading logic, data-driven design.
Tip          : add your own questions to QUESTIONS - no other code changes needed!
Run          : python 16_python_quiz.py       (add --demo for a sample run)
"""
from pythonlife import run, ask

QUESTIONS = [
    {"q": "What is the type of 3 / 2 in Python 3?", "options": ["int", "float", "str", "bool"],
     "answer": 1, "why": "The / operator always returns a float (1.5)."},
    {"q": "What does len('PythonLife') return?", "options": ["8", "9", "10", "11"],
     "answer": 2, "why": "Python has 6 letters, Life has 4 -> 10."},
    {"q": "Which of these is mutable?", "options": ["tuple", "str", "list", "int"],
     "answer": 2, "why": "Lists can be changed in place; tuples/strings/ints cannot."},
    {"q": "What is 2 ** 3?", "options": ["6", "8", "9", "5"],
     "answer": 1, "why": "** is the power operator: 2*2*2 = 8."},
    {"q": "Which keyword defines a function?", "options": ["func", "define", "def", "fun"],
     "answer": 2, "why": "Functions start with def."},
    {"q": "What is [1, 2, 3][-1]?", "options": ["1", "2", "3", "Error"],
     "answer": 2, "why": "Index -1 means the last item."},
    {"q": "Which dict method returns a default if the key is missing?",
     "options": ["fetch()", "get()", "find()", "pop_default()"],
     "answer": 1, "why": "d.get(key, default) never raises KeyError."},
    {"q": "What is 'py' * 2?", "options": ["'py2'", "'pypy'", "Error", "'py py'"],
     "answer": 1, "why": "Multiplying a string repeats it."},
    {"q": "list(range(3)) gives:", "options": ["[1, 2, 3]", "[0, 1, 2]", "[0, 1, 2, 3]", "[1, 2]"],
     "answer": 1, "why": "range(3) starts at 0 and stops before 3."},
    {"q": "Which loop runs while a condition is True?", "options": ["for", "while", "repeat", "loop"],
     "answer": 1, "why": "while repeats as long as its condition is True."},
]


def grade(answers, questions=QUESTIONS):
    """answers = list of chosen option indexes. Returns the score."""
    return sum(1 for a, q in zip(answers, questions) if a == q["answer"])


def verdict(score, total):
    pct = score / total * 100
    if pct >= 80:
        return "Excellent! You are ready for projects."
    return "Good start - revise the explanations above." if pct >= 50 else "Keep practising - you will get there!"


def main():
    answers = []
    for n, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{n}. {q['q']}")
        for letter, opt in zip("abcd", q["options"]):
            print(f"   {letter}) {opt}")
        pick = ask("Your answer (a-d): ").lower()
        chosen = "abcd".find(pick) if len(pick) == 1 else -1
        answers.append(chosen)
        print("  Correct!" if chosen == q["answer"] else f"  Not quite. {q['why']}")
    score = grade(answers)
    print(f"\nScore: {score}/{len(QUESTIONS)} - {verdict(score, len(QUESTIONS))}")


def demo():
    answers = [q["answer"] for q in QUESTIONS]
    answers[0], answers[3] = 0, 0                      # two deliberate mistakes
    score = grade(answers)
    for n, (a, q) in enumerate(zip(answers, QUESTIONS), 1):
        mark = "OK " if a == q["answer"] else "XX "
        print(f"{mark}Q{n}: {q['q']}")
    print(f"\nScore: {score}/{len(QUESTIONS)} - {verdict(score, len(QUESTIONS))}")


if __name__ == "__main__":
    run(16, "Python Basics Quiz", main, demo)
