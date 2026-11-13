# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 09 - Offline Currency Converter with Editable Rates (PythonLife)

What it does : converts money using a rates table you can edit and save.
Concepts     : JSON files, dictionaries, KeyError handling, persistence.
Note         : the bundled rates are SAMPLE values - update them to today's rates.
Run          : python 09_currency_converter.py (add --demo for a sample run)
"""
import json
from pathlib import Path
from pythonlife import run, ask, ask_float, choose, data_file

# value of 1 USD in each currency (sample numbers for learning)
DEFAULT_RATES = {"USD": 1.0, "INR": 83.0, "EUR": 0.92, "GBP": 0.79, "JPY": 150.0, "AED": 3.67}


def load_rates(path):
    path = Path(path)
    if not path.exists():
        save_rates(path, DEFAULT_RATES)
    return json.loads(path.read_text(encoding="utf-8"))


def save_rates(path, rates):
    Path(path).write_text(json.dumps(rates, indent=2), encoding="utf-8")


def convert(amount, frm, to, rates):
    frm, to = frm.upper(), to.upper()
    if frm not in rates or to not in rates:
        raise KeyError(f"unknown currency: {frm if frm not in rates else to}")
    return round(amount / rates[frm] * rates[to], 2)


def main():
    path = data_file("rates.json")
    rates = load_rates(path)
    while True:
        pick = choose(["Convert money", "Show rates", "Update a rate"])
        if pick == 0:
            break
        if pick == 1:
            try:
                amount = ask_float("Amount: ", 0)
                frm, to = ask("From (e.g. USD): "), ask("To (e.g. INR): ")
                print(f"{amount:,.2f} {frm.upper()} = {convert(amount, frm, to, rates):,.2f} {to.upper()}")
            except KeyError as err:
                print("  ", err)
        elif pick == 2:
            for code, value in rates.items():
                print(f"  1 USD = {value} {code}")
        else:
            code = ask("Currency code: ").upper()
            rates[code] = ask_float(f"New value of 1 USD in {code}: ", 0.000001)
            save_rates(path, rates)
            print("  Saved.")


def demo():
    path = data_file("rates.json")
    rates = load_rates(path)
    print("100 USD ->", convert(100, "usd", "inr", rates), "INR")
    print("5000 INR ->", convert(5000, "INR", "EUR", rates), "EUR")
    rates["INR"] = 84.5
    save_rates(path, rates)
    print("After updating the rate, 100 USD ->", convert(100, "USD", "INR", load_rates(path)), "INR")


if __name__ == "__main__":
    run(9, "Offline Currency Converter", main, demo)
