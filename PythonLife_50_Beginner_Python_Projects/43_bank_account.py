# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 43 - Bank Account Simulator (PythonLife)

What it does : deposits, withdrawals, transfers, minimum-balance rule and a
               printable statement.
Concepts     : OOP (classes, methods, encapsulation), custom exceptions, lists.
Run          : python 43_bank_account.py      (add --demo for a sample run)
"""
from pythonlife import run, ask, ask_float, choose


class InsufficientFunds(Exception):
    pass


class Account:
    MIN_BALANCE = 500

    def __init__(self, owner, opening=1000):
        if opening < self.MIN_BALANCE:
            raise ValueError(f"opening balance must be at least {self.MIN_BALANCE}")
        self.owner, self._balance, self.history = owner, float(opening), []
        self.history.append(("Opening", opening, self._balance))

    @property
    def balance(self):
        return round(self._balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount
        self.history.append(("Deposit", amount, self._balance))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if self._balance - amount < self.MIN_BALANCE:
            raise InsufficientFunds(f"must keep a minimum balance of {self.MIN_BALANCE}")
        self._balance -= amount
        self.history.append(("Withdraw", -amount, self._balance))

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def statement(self):
        lines = [f"Statement for {self.owner}", f"{'Type':<10}{'Amount':>10}{'Balance':>12}"]
        lines += [f"{t:<10}{a:>10,.2f}{b:>12,.2f}" for t, a, b in self.history]
        return "\n".join(lines)


def main():
    acct = Account(ask("Account holder: "), ask_float("Opening balance (min 500): ", 500))
    while True:
        pick = choose(["Deposit", "Withdraw", "Show statement"])
        if pick == 0:
            break
        try:
            if pick == 1:
                acct.deposit(ask_float("Amount: ", 0))
            elif pick == 2:
                acct.withdraw(ask_float("Amount: ", 0))
            else:
                print(acct.statement())
        except (ValueError, InsufficientFunds) as err:
            print("  Oops:", err)


def demo():
    a, b = Account("Anu", 5000), Account("Bala", 1000)
    a.deposit(1500)
    a.transfer(b, 2000)
    try:
        a.withdraw(10000)
    except InsufficientFunds as err:
        print("Blocked:", err)
    print(a.statement())
    print(f"Bala's balance: {b.balance:,.2f}")


if __name__ == "__main__":
    run(43, "Bank Account Simulator", main, demo)
