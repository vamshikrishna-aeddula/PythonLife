# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 06 - BMI & Healthy Weight Calculator (PythonLife)

What it does : computes BMI, category and the healthy weight range for a height.
Concepts     : formulas, if/elif chains, returning multiple values.
Note         : educational tool only - not medical advice.
Run          : python 06_bmi_calculator.py    (add --demo for a sample run)
"""
from pythonlife import run, ask_float


def bmi(weight_kg, height_cm):
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("weight and height must be positive")
    h = height_cm / 100
    return round(weight_kg / (h * h), 1)


def category(value):
    """WHO adult categories."""
    if value < 18.5:
        return "Underweight"
    if value < 25:
        return "Normal"
    if value < 30:
        return "Overweight"
    return "Obese"


def healthy_range(height_cm):
    """Weight range (kg) that gives a BMI of 18.5 - 24.9."""
    h = height_cm / 100
    return round(18.5 * h * h, 1), round(24.9 * h * h, 1)


def report(weight, height):
    value = bmi(weight, height)
    low, high = healthy_range(height)
    print(f"BMI: {value} ({category(value)})")
    print(f"Healthy weight for {height:g} cm: {low} - {high} kg")


def main():
    report(ask_float("Weight (kg): ", 1), ask_float("Height (cm): ", 1))
    print("(Educational only - talk to a doctor for health advice.)")


def demo():
    report(70, 172)
    report(95, 170)


if __name__ == "__main__":
    run(6, "BMI & Healthy Weight Calculator", main, demo)
