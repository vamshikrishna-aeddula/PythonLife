# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 44 - Shop Inventory Manager with Low-Stock Alerts (PythonLife)

What it does : track products, restock, sell, and get alerts when stock is low.
Concepts     : dict of dicts, JSON persistence, business rules, formatted tables.
Run          : python 44_inventory_manager.py (add --demo for a sample run)
"""
import json
from pathlib import Path
from pythonlife import run, ask, ask_float, ask_int, choose, data_file


class Inventory:
    def __init__(self, path):
        self.path = Path(path)
        self.items = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {}

    def _save(self):
        self.path.write_text(json.dumps(self.items, indent=2), encoding="utf-8")

    def add_item(self, sku, name, qty, price, reorder_level=5):
        if sku in self.items:
            raise ValueError("SKU already exists")
        self.items[sku] = {"name": name, "qty": qty, "price": price, "reorder_level": reorder_level}
        self._save()

    def restock(self, sku, qty):
        self.items[sku]["qty"] += qty
        self._save()

    def sell(self, sku, qty):
        """Reduce stock; returns the sale value."""
        item = self.items[sku]
        if qty > item["qty"]:
            raise ValueError(f"only {item['qty']} of {item['name']} in stock")
        item["qty"] -= qty
        self._save()
        return round(qty * item["price"], 2)

    def low_stock(self):
        return [i["name"] for i in self.items.values() if i["qty"] <= i["reorder_level"]]

    def total_value(self):
        return round(sum(i["qty"] * i["price"] for i in self.items.values()), 2)


def show(inv):
    print(f"  {'SKU':<8}{'Product':<18}{'Qty':>5}{'Price':>9}")
    for sku, i in inv.items.items():
        print(f"  {sku:<8}{i['name']:<18}{i['qty']:>5}{i['price']:>9.2f}")
    print(f"  Stock value: {inv.total_value():,.2f} | Low stock: {inv.low_stock() or 'none'}")


def main():
    inv = Inventory(data_file("inventory.json"))
    while True:
        pick = choose(["Add item", "Restock", "Sell", "Show stock"])
        if pick == 0:
            break
        try:
            if pick == 1:
                inv.add_item(ask("SKU: "), ask("Name: "), ask_int("Qty: ", 0), ask_float("Price: ", 0))
            elif pick == 2:
                inv.restock(ask("SKU: "), ask_int("Add qty: ", 1))
            elif pick == 3:
                print("  Sale value:", inv.sell(ask("SKU: "), ask_int("Qty: ", 1)))
            else:
                show(inv)
        except (ValueError, KeyError) as err:
            print("  Oops:", repr(err))


def demo():
    inv = Inventory(data_file("inventory.json"))
    inv.add_item("N01", "Notebook", 40, 45.0)
    inv.add_item("P01", "Gel Pen", 12, 10.0, reorder_level=10)
    print("Sold:", inv.sell("P01", 4), "-> sale value")
    inv.restock("N01", 10)
    show(inv)


if __name__ == "__main__":
    run(44, "Inventory Manager", main, demo)
