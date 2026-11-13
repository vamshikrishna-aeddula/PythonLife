# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 07 - Loan EMI Calculator with Payment Schedule (PythonLife)

What it does : monthly EMI, total interest and a month-by-month schedule.
Concepts     : financial formula, loops, tuple rows, formatted tables.
Formula      : EMI = P*r*(1+r)^n / ((1+r)^n - 1)   (r = yearly rate / 12 / 100)
Run          : python 07_emi_calculator.py    (add --demo for a sample run)
"""
from pythonlife import run, ask_float, ask_int


def emi(principal, annual_rate, months):
    if principal <= 0 or months < 1 or annual_rate < 0:
        raise ValueError("principal > 0, months >= 1 and rate >= 0 are required")
    r = annual_rate / 12 / 100
    if r == 0:
        return round(principal / months, 2)
    f = (1 + r) ** months
    return round(principal * r * f / (f - 1), 2)


def schedule(principal, annual_rate, months):
    """Rows of (month, payment, interest, principal_paid, balance)."""
    r = annual_rate / 12 / 100
    payment = emi(principal, annual_rate, months)
    balance, rows = principal, []
    for m in range(1, months + 1):
        interest = balance * r
        paid = payment - interest
        balance -= paid
        rows.append((m, payment, round(interest, 2), round(paid, 2), round(max(balance, 0), 2)))
    return rows


def show(principal, rate, months, rows_to_show=6):
    payment = emi(principal, rate, months)
    total = payment * months
    print(f"EMI: {payment:,.2f} | Total paid: {total:,.2f} | Total interest: {total - principal:,.2f}")
    print(f"{'Month':>5} {'Payment':>10} {'Interest':>10} {'Principal':>10} {'Balance':>12}")
    for m, pay, interest, paid, bal in schedule(principal, rate, months)[:rows_to_show]:
        print(f"{m:>5} {pay:>10,.2f} {interest:>10,.2f} {paid:>10,.2f} {bal:>12,.2f}")


def main():
    show(ask_float("Loan amount: ", 1), ask_float("Yearly interest %: ", 0), ask_int("Months: ", 1))


def demo():
    show(500000, 9.5, 36)


if __name__ == "__main__":
    run(7, "Loan EMI Calculator", main, demo)
