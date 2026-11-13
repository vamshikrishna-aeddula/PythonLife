# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 41 - Number to Words (Indian System: Lakh & Crore) (PythonLife)

What it does : 123456 -> "One Lakh Twenty-Three Thousand Four Hundred Fifty-Six"
               and amounts -> cheque-style "... Rupees and ... Paise Only".
Concepts     : divmod, recursion, lists as lookup tables, Decimal for money.
Run          : python 41_number_to_words.py   (add --demo for a sample run)
"""
from decimal import Decimal, InvalidOperation
from pythonlife import run, ask

ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def _below_100(n):
    if n < 20:
        return ONES[n]
    return TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")


def _below_1000(n):
    hundreds, rest = divmod(n, 100)
    parts = []
    if hundreds:
        parts.append(ONES[hundreds] + " Hundred")
    if rest:
        parts.append(_below_100(rest))
    return " ".join(parts)


def number_to_words(n):
    """Whole number >= 0 in the Indian numbering system."""
    if n < 0:
        raise ValueError("number must be 0 or more")
    if n == 0:
        return "Zero"
    crore, n = divmod(n, 10_000_000)
    lakh, n = divmod(n, 100_000)
    thousand, n = divmod(n, 1000)
    parts = []
    if crore:
        parts.append(number_to_words(crore) + " Crore")
    if lakh:
        parts.append(_below_100(lakh) + " Lakh")
    if thousand:
        parts.append(_below_100(thousand) + " Thousand")
    if n:
        parts.append(_below_1000(n))
    return " ".join(parts)


def amount_in_words(amount):
    """Cheque style: 1234.50 -> 'One Thousand ... Rupees and Fifty Paise Only'."""
    try:
        value = Decimal(str(amount)).quantize(Decimal("0.01"))
    except InvalidOperation:
        raise ValueError("not a valid amount")
    rupees = int(value)
    paise = int((value - rupees) * 100)
    text = number_to_words(rupees) + " Rupees"
    if paise:
        text += " and " + number_to_words(paise) + " Paise"
    return text + " Only"


def main():
    while True:
        text = ask("Amount (blank to quit): ")
        if not text:
            break
        try:
            print("  ", amount_in_words(text))
        except ValueError as err:
            print("  Oops:", err)


def demo():
    for n in (7, 19, 85, 100, 1000, 123456, 10_000_000, 2_50_00_000 + 15):
        print(f"{n:>12,} = {number_to_words(n)}")
    print(amount_in_words("45678.50"))


if __name__ == "__main__":
    run(41, "Number to Words (Lakh/Crore)", main, demo)
