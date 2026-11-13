# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 37 - Prime Number Toolkit (PythonLife)

What it does : prime test, sieve of Eratosthenes, prime factors, next prime,
               twin primes, GCD and LCM.
Concepts     : algorithms, while loops, efficiency (checking only up to sqrt(n)).
Run          : python 37_prime_toolkit.py     (add --demo for a sample run)
"""
import math
from pythonlife import run, ask_int


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, math.isqrt(n) + 1, 2))


def sieve(limit):
    """All primes up to `limit` using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if flags[i]:
            for multiple in range(i * i, limit + 1, i):
                flags[multiple] = False
    return [i for i, ok in enumerate(flags) if ok]


def prime_factors(n):
    """12 -> {2: 2, 3: 1}"""
    if n < 2:
        raise ValueError("n must be 2 or more")
    factors, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def twin_primes(limit):
    p = sieve(limit)
    return [(a, b) for a, b in zip(p, p[1:]) if b - a == 2]


def lcm(a, b):
    return a * b // math.gcd(a, b)


def main():
    n = ask_int("Enter a number (2 or more): ", 2)
    print(f"{n} is {'prime' if is_prime(n) else 'not prime'}; factors {prime_factors(n)}; next prime {next_prime(n)}")
    print("Primes up to", n, ":", sieve(n))


def demo():
    print("Primes up to 50:", sieve(50))
    print("97 prime?", is_prime(97), "| 91 prime?", is_prime(91))
    print("360 factors:", prime_factors(360))
    print("Next prime after 100:", next_prime(100))
    print("Twin primes below 60:", twin_primes(60))
    print("GCD(48, 180) =", math.gcd(48, 180), "| LCM =", lcm(48, 180))


if __name__ == "__main__":
    run(37, "Prime Number Toolkit", main, demo)
