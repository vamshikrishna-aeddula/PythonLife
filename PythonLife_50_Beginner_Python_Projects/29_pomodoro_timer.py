# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 29 - Pomodoro Focus Timer (PythonLife)

What it does : alternates focus sessions and breaks (default 25/5, long break after 4).
Concepts     : time.sleep, divmod, passing functions as arguments (testable code!).
Run          : python 29_pomodoro_timer.py    (add --demo for a sample run)
"""
import time
from pythonlife import run, ask_int


def fmt(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def countdown(seconds, label, sleep=time.sleep):
    for remaining in range(int(seconds), 0, -1):
        print(f"\r  {label}  {fmt(remaining)} ", end="", flush=True)
        sleep(1)
    print(f"\r  {label}  done!      ")


def build_plan(work=25, rest=5, cycles=4, long_rest=15):
    """List of (label, minutes)."""
    plan = []
    for i in range(1, cycles + 1):
        plan.append((f"Focus #{i}", work))
        plan.append(("Long break" if i == cycles else "Short break", long_rest if i == cycles else rest))
    return plan


def run_pomodoro(plan, unit=60, sleep=time.sleep):
    """unit = seconds per 'minute' (use 1 for a quick demo)."""
    for label, minutes in plan:
        countdown(minutes * unit, label, sleep)


def main():
    work = ask_int("Focus minutes (25): ", 1)
    rest = ask_int("Break minutes (5): ", 1)
    cycles = ask_int("Cycles: ", 1)
    print("Press Ctrl+C to stop.")
    run_pomodoro(build_plan(work, rest, cycles))
    print("Great work! Take a real break.")


def demo():
    plan = build_plan(work=2, rest=1, cycles=2, long_rest=2)
    print("Plan:", plan)
    run_pomodoro(plan, unit=1, sleep=lambda s: None)       # no real waiting in the demo


if __name__ == "__main__":
    run(29, "Pomodoro Focus Timer", main, demo)
