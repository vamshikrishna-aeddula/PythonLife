# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 38 - Number System Converter (Binary / Octal / Hex / any base) (PythonLife)

What it does : converts between bases 2-36 WITHOUT using bin()/hex() so you
               can see how the algorithm really works.
Concepts     : divmod, while loops, string indexing, reversing.
Run          : python 38_number_systems.py    (add --demo for a sample run)
"""
from pythonlife import run, ask, ask_int

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, base):
    """Integer -> text in `base` (2-36)."""
    if not 2 <= base <= 36:
        raise ValueError("base must be between 2 and 36")
    if n == 0:
        return "0"
    sign, n, out = ("-" if n < 0 else ""), abs(n), []
    while n:
        n, remainder = divmod(n, base)
        out.append(DIGITS[remainder])
    return sign + "".join(reversed(out))


def from_base(text, base):
    """Text in `base` -> integer."""
    if not 2 <= base <= 36:
        raise ValueError("base must be between 2 and 36")
    text = text.strip().upper()
    sign = -1 if text.startswith("-") else 1
    value = 0
    for ch in text.lstrip("-"):
        digit = DIGITS.find(ch)
        if digit == -1 or digit >= base:
            raise ValueError(f"'{ch}' is not a valid digit in base {base}")
        value = value * base + digit
    return sign * value


def main():
    text = ask("Number: ")
    base = ask_int("It is written in base (2-36): ", 2)
    try:
        n = from_base(text, base)
        print(f"Decimal: {n} | Binary: {to_base(n, 2)} | Octal: {to_base(n, 8)} | Hex: {to_base(n, 16)}")
    except ValueError as err:
        print("  Oops:", err)


def demo():
    for n in (10, 255, 2026):
        print(f"{n:>5} -> binary {to_base(n, 2):>12} | octal {to_base(n, 8):>5} | hex {to_base(n, 16):>4}")
    print("FF in base 16 =", from_base("FF", 16))
    print("1011 in base 2 =", from_base("1011", 2))
    print("ZZ in base 36 =", from_base("ZZ", 36))


if __name__ == "__main__":
    run(38, "Number System Converter", main, demo)
