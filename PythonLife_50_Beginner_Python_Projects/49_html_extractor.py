# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 49 - HTML Page Inspector: Title, Headings, Links, Images (PythonLife)

What it does : parses an HTML page (file or text) and lists its title, headings,
               links and image alt-texts - the basis of web scraping and SEO checks.
Concepts     : html.parser.HTMLParser (event-driven parsing), inheritance.
Run          : python 49_html_extractor.py    (add --demo for a sample run)
"""
from html.parser import HTMLParser
from pathlib import Path
from pythonlife import run, ask


class PageInfo(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title, self.headings, self.links, self.images = "", [], [], []
        self._tag, self._href, self._text = None, None, ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("title", "h1", "h2", "h3", "a"):
            self._tag, self._text = tag, ""
            if tag == "a":
                self._href = attrs.get("href", "")
        elif tag == "img":
            self.images.append((attrs.get("src", ""), attrs.get("alt", "")))

    def handle_data(self, data):
        if self._tag:
            self._text += data

    def handle_endtag(self, tag):
        if tag != self._tag:
            return
        text = " ".join(self._text.split())
        if tag == "title":
            self.title = text
        elif tag == "a":
            self.links.append((text, self._href))
        else:
            self.headings.append((tag, text))
        self._tag = None


def inspect_html(source):
    parser = PageInfo()
    parser.feed(source)
    return parser


def show(page):
    print("  Title   :", page.title)
    print("  Headings:", page.headings)
    print("  Links   :", page.links)
    print("  Images  :", page.images)
    missing = [src for src, alt in page.images if not alt]
    print("  SEO tip :", f"{len(missing)} image(s) missing alt text" if missing else "all images have alt text")


def main():
    path = Path(ask("HTML file path: ")).expanduser()
    if path.is_file():
        show(inspect_html(path.read_text(encoding="utf-8", errors="replace")))
    else:
        print("  File not found.")


SAMPLE = """<html><head><title>PythonLife Home</title></head><body>
<h1>Welcome to PythonLife</h1><h2>Courses</h2>
<a href="/python">Python Course</a> <a href="https://example.com">Partner</a>
<img src="logo.png" alt="PythonLife logo"><img src="banner.png">
<h3>Contact</h3></body></html>"""


def demo():
    show(inspect_html(SAMPLE))


if __name__ == "__main__":
    run(49, "HTML Page Inspector", main, demo)
