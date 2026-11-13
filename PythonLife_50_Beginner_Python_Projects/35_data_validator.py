# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 35 - Indian Data Validator: Email, Mobile, PIN, PAN, IFSC (PythonLife)

What it does : checks if user-entered data has the right FORMAT - handy for
               forms and sign-up pages. (Format only - it cannot prove the
               number/ID really exists.)
Concepts     : regular expressions, dictionaries of functions.
Run          : python 35_data_validator.py    (add --demo for a sample run)
"""
import re
from pythonlife import run, ask

PATTERNS = {
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}",
    "mobile": r"(\+91[\s-]?|0)?[6-9]\d{9}",
    "pincode": r"[1-9]\d{5}",
    "pan": r"[A-Z]{5}\d{4}[A-Z]",
    "ifsc": r"[A-Z]{4}0[A-Z0-9]{6}",
}


def validate(kind, value):
    """True if `value` matches the format of `kind`."""
    return re.fullmatch(PATTERNS[kind], value.strip()) is not None


def validate_all(record):
    """record = {'email': ..., 'mobile': ...} -> {'email': True/False, ...}"""
    return {kind: validate(kind, value) for kind, value in record.items()}


def main():
    print("Kinds:", ", ".join(PATTERNS))
    while True:
        kind = ask("Kind (blank to quit): ").lower()
        if not kind:
            break
        if kind not in PATTERNS:
            print("  Unknown kind.")
            continue
        print("  Valid format!" if validate(kind, ask("Value: ")) else "  Invalid format.")


def demo():
    samples = {"email": "student@pythonlife.example", "mobile": "+91 98765 43210",
               "pincode": "500081", "pan": "ABCDE1234F", "ifsc": "SBIN0001234"}
    bad = {"email": "student@@mail", "mobile": "12345", "pincode": "050001",
           "pan": "abcde1234f", "ifsc": "SBIN1001234"}
    print("Good samples:", validate_all(samples))
    print("Bad samples :", validate_all(bad))


if __name__ == "__main__":
    run(35, "Data Format Validator", main, demo)
