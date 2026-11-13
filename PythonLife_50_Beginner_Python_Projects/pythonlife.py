# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""PythonLife shared helpers - used by every project in the series.

Keeps each project file short and focused on the idea being taught:
  * banner()/run()  - consistent PythonLife header + a --demo switch
  * ask*/choose()   - safe keyboard input (no crashes on bad typing)
  * data_file()     - where projects store their data (temp folder in --demo)
"""
import sys
import tempfile
from pathlib import Path

BRAND = "PythonLife"


def banner(number, title):
    """Print the PythonLife header for a project."""
    line = "=" * 62
    print(line)
    print(f"  {BRAND} | Beginner Python Projects | #{number:02d}")
    print(f"  {title}")
    print(line)


def run(number, title, main, demo):
    """Entry point used by every project.

    python project.py          -> interactive mode (main)
    python project.py --demo   -> automatic sample run (demo)
    """
    banner(number, title)
    if "--demo" in sys.argv:
        print("[demo mode - sample data, no typing needed]\n")
        demo()
        print("\nDemo finished OK.")
        return
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\nBye! Keep learning with {BRAND}.")


def ask(prompt):
    """Read one line of text."""
    return input(prompt).strip()


def ask_float(prompt, minimum=None):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  Please enter a valid number.")
            continue
        if minimum is not None and value < minimum:
            print(f"  Please enter a number >= {minimum}.")
            continue
        return value


def ask_int(prompt, minimum=None):
    """Keep asking until the user types a valid whole number."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"  Please enter a number >= {minimum}.")
            continue
        return value


def choose(options):
    """Show a numbered menu; return 1..N, or 0 to exit."""
    print()
    for i, text in enumerate(options, 1):
        print(f"  {i}) {text}")
    print("  0) Exit")
    while True:
        raw = input("Choose: ").strip()
        if raw.isdigit() and 0 <= int(raw) <= len(options):
            return int(raw)
        print("  Invalid choice, try again.")


def data_file(name):
    """Path for saving project data. Uses a throw-away folder in --demo mode."""
    if "--demo" in sys.argv:
        folder = Path(tempfile.mkdtemp(prefix="pythonlife_"))
    else:
        folder = Path.home() / ".pythonlife"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / name
