# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 39 - Matrix Calculator (PythonLife)

What it does : add, multiply, transpose, determinant and inverse of matrices
               (inverse uses exact fractions, so no rounding surprises).
Concepts     : nested lists, zip, recursion, Gauss-Jordan elimination, fractions.
Run          : python 39_matrix_calculator.py (add --demo for a sample run)
"""
from fractions import Fraction
from pythonlife import run, ask


def add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrices must have the same size")
    return [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)]


def multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("columns of A must equal rows of B")
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(m):
    return [list(col) for col in zip(*m)]


def determinant(m):
    n = len(m)
    if any(len(row) != n for row in m):
        raise ValueError("determinant needs a square matrix")
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return sum(((-1) ** c) * m[0][c] * determinant([row[:c] + row[c + 1:] for row in m[1:]])
               for c in range(n))


def inverse(m):
    n = len(m)
    if determinant(m) == 0:
        raise ValueError("matrix is singular (determinant is 0), no inverse")
    a = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(m)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if a[r][col] != 0)
        a[col], a[pivot] = a[pivot], a[col]
        pv = a[col][col]
        a[col] = [x / pv for x in a[col]]
        for r in range(n):
            if r != col:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a]


def show(m, name=""):
    if name:
        print(name)
    for row in m:
        print("  [" + "  ".join(f"{str(x):>6}" for x in row) + " ]")


def parse(text):
    """'1 2; 3 4' -> [[1, 2], [3, 4]]"""
    return [[float(x) if "." in x else int(x) for x in row.split()] for row in text.split(";")]


def main():
    print("Type matrices like:  1 2; 3 4")
    a = parse(ask("Matrix A: "))
    try:
        show(transpose(a), "Transpose:")
        show([[determinant(a)]], "Determinant:")
        show(inverse(a), "Inverse:")
    except ValueError as err:
        print("  Oops:", err)


def demo():
    a, b = [[1, 2], [3, 4]], [[0, 1], [1, 0]]
    show(add(a, b), "A + B")
    show(multiply(a, b), "A x B")
    show(transpose(a), "Transpose of A")
    print("det(A) =", determinant(a), "| det of 3x3 =", determinant([[2, 0, 1], [1, 3, 2], [1, 1, 1]]))
    show(inverse(a), "Inverse of A")


if __name__ == "__main__":
    run(39, "Matrix Calculator", main, demo)
