# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 10 - GST Calculator (PythonLife)

What it does : adds GST to a price, or extracts GST from a GST-inclusive price,
               and splits it into CGST + SGST.
Concepts     : percentages, dictionaries, rounding money.
Note         : you type the GST rate - rates change, so none are hard-coded.
Run          : python 10_gst_calculator.py    (add --demo for a sample run)
"""
from pythonlife import run, ask_float, choose


def add_gst(price, rate):
    """price is WITHOUT GST."""
    gst = round(price * rate / 100, 2)
    return {"base": round(price, 2), "gst": gst, "cgst": round(gst / 2, 2),
            "sgst": round(gst / 2, 2), "total": round(price + gst, 2)}


def remove_gst(total, rate):
    """total already INCLUDES GST."""
    base = round(total * 100 / (100 + rate), 2)
    gst = round(total - base, 2)
    return {"base": base, "gst": gst, "cgst": round(gst / 2, 2),
            "sgst": round(gst / 2, 2), "total": round(total, 2)}


def show(result):
    for key in ("base", "cgst", "sgst", "gst", "total"):
        print(f"  {key.upper():>6}: {result[key]:>12,.2f}")


def main():
    while True:
        pick = choose(["Add GST to a price", "Remove GST from a total"])
        if pick == 0:
            break
        amount, rate = ask_float("Amount: ", 0), ask_float("GST rate %: ", 0)
        show(add_gst(amount, rate) if pick == 1 else remove_gst(amount, rate))


def demo():
    print("Price 1000 + 18% GST:")
    show(add_gst(1000, 18))
    print("Total 1180 includes 18% GST:")
    show(remove_gst(1180, 18))


if __name__ == "__main__":
    run(10, "GST Calculator", main, demo)
