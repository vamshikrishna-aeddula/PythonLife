# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 20 - Caesar Cipher: Encrypt, Decrypt & Crack (PythonLife)

What it does : shifts letters to hide a message, and cracks it by brute force.
Concepts     : ord()/chr(), modulo arithmetic, dictionaries, basic cryptography.
Warning      : a toy cipher for learning - never use it to protect real secrets.
Run          : python 20_caesar_cipher.py     (add --demo for a sample run)
"""
from pythonlife import run, ask, ask_int, choose


def shift_text(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)


def encrypt(text, shift):
    return shift_text(text, shift)


def decrypt(text, shift):
    return shift_text(text, -shift)


def brute_force(text):
    """Try all 25 shifts. Returns {shift: candidate}."""
    return {s: decrypt(text, s) for s in range(1, 26)}


def main():
    while True:
        pick = choose(["Encrypt", "Decrypt", "Brute-force crack"])
        if pick == 0:
            break
        text = ask("Text: ")
        if pick == 3:
            for s, cand in brute_force(text).items():
                print(f"  shift {s:>2}: {cand}")
        else:
            n = ask_int("Shift (1-25): ", 1)
            print(encrypt(text, n) if pick == 1 else decrypt(text, n))


def demo():
    secret = encrypt("Learn Python with PythonLife!", 3)
    print("Encrypted:", secret)
    print("Decrypted:", decrypt(secret, 3))
    print("Brute force shift 3 ->", brute_force(secret)[3])


if __name__ == "__main__":
    run(20, "Caesar Cipher", main, demo)
