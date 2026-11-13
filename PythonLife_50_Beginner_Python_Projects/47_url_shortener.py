# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 47 - Local URL Shortener with Click Counter (PythonLife)

What it does : turns long URLs into short codes (like 'g8') and counts clicks.
               Runs offline - it teaches how real shorteners work.
Concepts     : base-62 encoding, urllib.parse validation, dictionaries, JSON.
Run          : python 47_url_shortener.py     (add --demo for a sample run)
"""
import json
from pathlib import Path
from urllib.parse import urlparse
from pythonlife import run, ask, choose, data_file

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE_URL = "short.local/"


def encode62(number):
    if number == 0:
        return ALPHABET[0]
    out = []
    while number:
        number, rem = divmod(number, 62)
        out.append(ALPHABET[rem])
    return "".join(reversed(out))


def decode62(code):
    value = 0
    for ch in code:
        value = value * 62 + ALPHABET.index(ch)
    return value


class Shortener:
    def __init__(self, path):
        self.path = Path(path)
        self.data = (json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists()
                     else {"counter": 1000, "links": {}})

    def _save(self):
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")

    def shorten(self, url):
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise ValueError("URL must start with http:// or https:// and include a domain")
        for code, info in self.data["links"].items():
            if info["url"] == url:                     # same URL -> same code
                return code
        self.data["counter"] += 1
        code = encode62(self.data["counter"])
        self.data["links"][code] = {"url": url, "clicks": 0}
        self._save()
        return code

    def resolve(self, code):
        info = self.data["links"][code]
        info["clicks"] += 1
        self._save()
        return info["url"]


def main():
    s = Shortener(data_file("links.json"))
    while True:
        pick = choose(["Shorten a URL", "Open a short code", "Show stats"])
        if pick == 0:
            break
        try:
            if pick == 1:
                print("  ", BASE_URL + s.shorten(ask("Long URL: ")))
            elif pick == 2:
                print("  ->", s.resolve(ask("Code: ")))
            else:
                for code, info in s.data["links"].items():
                    print(f"  {BASE_URL}{code}  clicks={info['clicks']}  {info['url']}")
        except (ValueError, KeyError) as err:
            print("  Oops:", repr(err))


def demo():
    s = Shortener(data_file("links.json"))
    a = s.shorten("https://docs.python.org/3/tutorial/index.html")
    b = s.shorten("https://www.python.org/dev/peps/pep-0008/")
    print(BASE_URL + a, BASE_URL + b, "| same URL again ->", s.shorten("https://docs.python.org/3/tutorial/index.html") == a)
    s.resolve(a)
    s.resolve(a)
    print("Clicks on first link:", s.data["links"][a]["clicks"])
    try:
        s.shorten("not a url")
    except ValueError as err:
        print("Blocked:", err)
    assert decode62(a) == 1001


if __name__ == "__main__":
    run(47, "Local URL Shortener", main, demo)
