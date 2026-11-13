# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 08 - SIP & Compound Interest Calculator (PythonLife)

What it does : projects how a monthly investment (SIP) or lump sum can grow.
Concepts     : compounding, functions with default arguments, formatted output.
Note         : an illustration only - real returns are not guaranteed.
Run          : python 08_sip_calculator.py    (add --demo for a sample run)
"""
from pythonlife import run, ask_float


def sip_future_value(monthly, annual_return, years):
    """Future value of a monthly SIP (payments at the start of each month)."""
    n, r = int(years * 12), annual_return / 12 / 100
    fv = monthly * n if r == 0 else monthly * (((1 + r) ** n - 1) / r) * (1 + r)
    invested = monthly * n
    return {"invested": round(invested, 2), "future_value": round(fv, 2),
            "gain": round(fv - invested, 2)}


def lump_sum(amount, annual_return, years, compounds_per_year=1):
    """A = P * (1 + r/n)^(n*t)"""
    r = annual_return / 100
    return round(amount * (1 + r / compounds_per_year) ** (compounds_per_year * years), 2)


def main():
    monthly = ask_float("Monthly SIP amount: ", 1)
    rate = ask_float("Expected yearly return %: ", 0)
    years = ask_float("Years: ", 1)
    result = sip_future_value(monthly, rate, years)
    for key, value in result.items():
        print(f"{key:>13}: {value:,.2f}")
    print("(Illustration only - returns are not guaranteed.)")


def demo():
    r = sip_future_value(5000, 12, 10)
    print(f"SIP 5,000/month @12% for 10 yrs -> invested {r['invested']:,.0f}, "
          f"value {r['future_value']:,.0f}, gain {r['gain']:,.0f}")
    print(f"Lump sum 100,000 @8% for 5 yrs  -> {lump_sum(100000, 8, 5):,.2f}")


if __name__ == "__main__":
    run(8, "SIP & Compound Interest Calculator", main, demo)
