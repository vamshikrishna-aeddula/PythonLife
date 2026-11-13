# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 04 - Password Strength Checker (PythonLife)

What it does : scores a password 0-100 and tells you how to improve it.
Concepts     : regular expressions (re), sets, scoring logic, getpass.
Run          : python 04_password_checker.py  (add --demo for a sample run)
"""
import re
from getpass import getpass
from pythonlife import run

COMMON = {"password", "123456", "qwerty", "abc123", "iloveyou", "admin",
          "welcome", "letmein", "pythonlife", "python123", "india123"}


def check_password(pw):
    """Return (score, label, tips)."""
    score, tips = 0, []
    if len(pw) >= 8:
        score += 25
    else:
        tips.append("Use at least 8 characters")
    if len(pw) >= 12:
        score += 15
    for pattern, tip in ((r"[a-z]", "Add lowercase letters"), (r"[A-Z]", "Add UPPERCASE letters"),
                         (r"\d", "Add digits"), (r"[^A-Za-z0-9]", "Add a symbol like @ # $")):
        if re.search(pattern, pw):
            score += 15
        else:
            tips.append(tip)
    if re.search(r"(.)\1{2,}", pw):
        score -= 10
        tips.append("Avoid repeating a character 3+ times")
    if re.search(r"(0123|1234|2345|3456|4567|5678|6789|abcd|bcde|qwer)", pw.lower()):
        score -= 10
        tips.append("Avoid easy sequences like 1234 or abcd")
    if any(word in pw.lower() for word in COMMON):
        score = min(score, 20)
        tips.append("Avoid common words")
    score = max(0, min(100, score))
    label = "Weak" if score < 40 else "Medium" if score < 70 else "Strong"
    return score, label, tips


def show(pw):
    score, label, tips = check_password(pw)
    print(f"Score: {score}/100 -> {label}")
    for tip in tips:
        print("  -", tip)


def main():
    show(getpass("Type a password (hidden): "))


def demo():
    for pw in ["password", "Python123", "Tr!cky#Life2026", "aaaa1111"]:
        print(f"\nTesting: {pw}")
        show(pw)


if __name__ == "__main__":
    run(4, "Password Strength Checker", main, demo)
