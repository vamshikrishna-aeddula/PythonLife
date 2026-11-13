# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 02 - Unit Converter (PythonLife)

What it does : converts length, weight and temperature units.
Concepts     : dictionaries as lookup tables, string methods, error handling.
Run          : python 02_unit_converter.py    (add --demo for a sample run)
Example      : type  10 km mile
"""
from pythonlife import run

# every unit is stored as "how many base units it contains"
LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
          "inch": 0.0254, "ft": 0.3048, "mile": 1609.344}          # base: metre
WEIGHT = {"mg": 1e-6, "g": 0.001, "kg": 1, "lb": 0.45359237,
          "oz": 0.028349523125}                                      # base: kilogram
TEMPS = ("c", "f", "k")


def _to_celsius(v, unit):
    return v if unit == "c" else (v - 32) * 5 / 9 if unit == "f" else v - 273.15


def _from_celsius(v, unit):
    return v if unit == "c" else v * 9 / 5 + 32 if unit == "f" else v + 273.15


def convert(value, frm, to):
    """Convert value from one unit to another (same family only)."""
    frm, to = frm.lower().strip(), to.lower().strip()
    for table in (LENGTH, WEIGHT):
        if frm in table and to in table:
            return value * table[frm] / table[to]
    if frm in TEMPS and to in TEMPS:
        return _from_celsius(_to_celsius(value, frm), to)
    raise ValueError(f"cannot convert '{frm}' to '{to}'")


def main():
    print("Units: " + ", ".join(list(LENGTH) + list(WEIGHT) + list(TEMPS)))
    print("Type like:  10 km mile   (or 'q' to quit)")
    while True:
        text = input("> ").strip()
        if text.lower() in ("q", "quit", ""):
            break
        try:
            value, frm, to = text.split()
            print(f"{value} {frm} = {convert(float(value), frm, to):.4f} {to}")
        except ValueError as err:
            print("  Oops:", err)


def demo():
    for value, frm, to in [(10, "km", "mile"), (5, "kg", "lb"), (100, "c", "f"), (72, "f", "c")]:
        print(f"{value} {frm} = {convert(value, frm, to):.2f} {to}")


if __name__ == "__main__":
    run(2, "Unit Converter", main, demo)
