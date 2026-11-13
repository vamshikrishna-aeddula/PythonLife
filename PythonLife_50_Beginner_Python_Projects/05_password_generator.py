# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 05 - Secure Password & Passphrase Generator (PythonLife)

What it does : creates strong random passwords and easy-to-remember passphrases.
Concepts     : the `secrets` module (safer than `random`), string constants, lists.
Run          : python 05_password_generator.py (add --demo for a sample run)
"""
import random
import secrets
import string
from pythonlife import run, ask_int

SYMBOLS = "!@#$%^&*()-_=+"
WORDS = ["python", "coffee", "river", "mango", "rocket", "tiger", "cloud", "lotus",
         "pixel", "forest", "silver", "planet", "monsoon", "spice", "guitar", "temple",
         "orange", "anchor", "bridge", "falcon", "garden", "harbor", "island", "jungle"]


def generate_password(length=14, symbols=True):
    """Random password with at least one lower, upper, digit (and symbol)."""
    if length < 4:
        raise ValueError("length must be at least 4")
    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if symbols:
        pools.append(SYMBOLS)
    chars = [secrets.choice(pool) for pool in pools]          # one from each pool
    everything = "".join(pools)
    chars += [secrets.choice(everything) for _ in range(length - len(chars))]
    random.SystemRandom().shuffle(chars)
    return "".join(chars)


def generate_passphrase(words=4, separator="-"):
    """Example: Mango-tiger-cloud-river-42"""
    picked = [secrets.choice(WORDS) for _ in range(words)]
    picked[0] = picked[0].capitalize()
    return separator.join(picked) + separator + str(secrets.randbelow(90) + 10)


def main():
    length = ask_int("Password length (min 4): ", 4)
    for _ in range(3):
        print("Password  :", generate_password(length))
    print("Passphrase:", generate_passphrase())


def demo():
    print("Password  :", generate_password(16))
    print("No symbols:", generate_password(10, symbols=False))
    print("Passphrase:", generate_passphrase())


if __name__ == "__main__":
    run(5, "Password & Passphrase Generator", main, demo)
