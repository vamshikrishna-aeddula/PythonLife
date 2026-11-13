"""
check_letter.py: lint a cover letter before you send it.

Checks for leftover {{PLACEHOLDERS}}, length, generic phrases,
repetitive "I" openings, missing numbers and (optionally) the company name.
Standard library only.

Usage:
    python scripts/check_letter.py my_letter.txt --company "Acme"
    python scripts/check_letter.py outreach.txt --short
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CLICHES = [
    "to whom it may concern",
    "i am writing to apply",
    "i am writing to express",
    "hard worker",
    "team player",
    "passionate about",
    "fast learner",
    "think outside the box",
    "results-driven",
    "go-getter",
]


def analyze(text: str, company: str | None, short: bool) -> tuple[list[str], list[str]]:
    """Return (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    left = sorted(set(re.findall(r"\{\{\w+\}\}", text)))
    if left:
        errors.append("Unfilled placeholders: " + ", ".join(left))

    words = len(re.findall(r"\b[\w'-]+\b", text))
    low, high = (80, 220) if short else (150, 400)
    if words < low:
        warnings.append(f"Short ({words} words). Aim for {low} to {high}.")
    elif words > high:
        warnings.append(f"Long ({words} words). Aim for {low} to {high}.")

    lowered = text.lower()
    for phrase in CLICHES:
        if phrase in lowered:
            warnings.append(f'Generic phrase: "{phrase}". Replace it with something specific.')

    if company and company.lower() not in lowered:
        warnings.append(f"The company name '{company}' never appears.")

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    if sentences:
        share = sum(s.startswith("I ") for s in sentences) / len(sentences)
        if share > 0.5:
            warnings.append(f"{share:.0%} of sentences start with 'I'. Vary the openings.")

    if not re.search(r"\d", text):
        warnings.append("No numbers found. Add at least one measurable result.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a cover letter.")
    parser.add_argument("file", type=Path, help="Plain text or Markdown letter")
    parser.add_argument("--company", help="Company name that should appear")
    parser.add_argument("--short", action="store_true", help="Use limits for short outreach messages")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    errors, warnings = analyze(text, args.company, args.short)

    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"WARNING {w}")
    if not errors and not warnings:
        print("OK: no issues found.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
