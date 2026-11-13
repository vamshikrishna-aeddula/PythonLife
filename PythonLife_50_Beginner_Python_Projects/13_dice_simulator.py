# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 13 - Dice Roller with Tabletop Notation & Histogram (PythonLife)

What it does : rolls dice written like "2d6+3" and simulates thousands of rolls
               to draw a text histogram.
Concepts     : regular expressions, random, Counter, string multiplication for bars.
Run          : python 13_dice_simulator.py    (add --demo for a sample run)
"""
import random
import re
from collections import Counter
from pythonlife import run, ask, ask_int

PATTERN = re.compile(r"(\d*)d(\d+)([+-]\d+)?")


def parse_dice(expr):
    """'2d6+3' -> (2, 6, 3)"""
    m = PATTERN.fullmatch(expr.strip().lower())
    if not m:
        raise ValueError("use the format NdS+M, e.g. d20, 2d6, 3d8-1")
    count, sides, mod = int(m.group(1) or 1), int(m.group(2)), int(m.group(3) or 0)
    if count < 1 or sides < 2:
        raise ValueError("need at least 1 die with 2+ sides")
    return count, sides, mod


def roll(expr, rng=random):
    count, sides, mod = parse_dice(expr)
    rolls = [rng.randint(1, sides) for _ in range(count)]
    return rolls, sum(rolls) + mod


def simulate(expr, times, rng=random):
    return Counter(roll(expr, rng)[1] for _ in range(times))


def histogram(counter, width=40):
    biggest = max(counter.values())
    return [f"{value:>3} | {'#' * max(1, round(count / biggest * width))} {count}"
            for value, count in sorted(counter.items())]


def main():
    expr = ask("Dice (e.g. 2d6+3): ")
    try:
        rolls, total = roll(expr)
        print(f"Rolled {rolls} -> total {total}")
        print("\n".join(histogram(simulate(expr, ask_int("Simulate how many rolls? ", 1)))))
    except ValueError as err:
        print("  Oops:", err)


def demo():
    rng = random.Random(1)
    print("Roll 2d6+3:", roll("2d6+3", rng))
    print("\nHistogram of 2d6 x 2000 rolls:")
    print("\n".join(histogram(simulate("2d6", 2000, rng))))


if __name__ == "__main__":
    run(13, "Dice Roller & Probability Histogram", main, demo)
