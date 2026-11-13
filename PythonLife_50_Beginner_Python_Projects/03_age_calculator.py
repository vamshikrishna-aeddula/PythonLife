# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 03 - Age & Birthday Countdown (PythonLife)

What it does : exact age in years/months/days + days until next birthday.
Concepts     : datetime.date, calendar, leap years, tuples comparison.
Run          : python 03_age_calculator.py    (add --demo for a sample run)
"""
import calendar
from datetime import date
from pythonlife import run, ask_int


def age_on(born, today):
    """Return (years, months, days) between born and today."""
    years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    months = (today.month - born.month - (today.day < born.day)) % 12
    total = born.year * 12 + (born.month - 1) + years * 12 + months
    year, month = divmod(total, 12)
    month += 1
    anchor_day = min(born.day, calendar.monthrange(year, month)[1])
    days = (today - date(year, month, anchor_day)).days
    return years, months, days


def next_birthday(born, today):
    """Return (date, days_left). Feb-29 babies celebrate on 1 March in normal years."""
    def birthday_in(year):
        try:
            return date(year, born.month, born.day)
        except ValueError:
            return date(year, 3, 1)
    nxt = birthday_in(today.year)
    if nxt < today:
        nxt = birthday_in(today.year + 1)
    return nxt, (nxt - today).days


def report(born, today):
    y, m, d = age_on(born, today)
    nxt, left = next_birthday(born, today)
    print(f"Age: {y} years, {m} months, {d} days")
    print(f"Next birthday: {nxt:%A, %d %B %Y} (in {left} days)")


def main():
    year = ask_int("Birth year: ", 1900)
    month = ask_int("Birth month (1-12): ", 1)
    day = ask_int("Birth day: ", 1)
    try:
        report(date(year, month, day), date.today())
    except ValueError as err:
        print("Invalid date:", err)


def demo():
    report(date(2000, 2, 29), date(2026, 11, 13))
    report(date(1995, 8, 15), date(2026, 11, 13))


if __name__ == "__main__":
    run(3, "Age & Birthday Countdown", main, demo)
