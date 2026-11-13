# 🐍 PythonLife — GitHub Profile README Templates

Four ready-to-use profile templates plus an auto-updating "latest posts" section, all in the **PythonLife** voice: practical, beginner-friendly, and built in public.

## How to use any template

1. On GitHub, create a **public** repository named **exactly your username** (e.g. `janedoe/janedoe`).
2. Tick **"Add a README.md"**. GitHub shows a "this is a special repo" banner.
3. Copy a template below into `README.md`.
4. Replace every `{{PLACEHOLDER}}` (search for `{{`).
5. Commit. Your profile updates instantly.

### Placeholder reference

| Placeholder | Meaning | Example |
|---|---|---|
| `{{NAME}}` | Your display name | Jane Doe |
| `{{USERNAME}}` | GitHub username | janedoe |
| `{{TAGLINE}}` | One line about what you do | Building tiny tools in Python |
| `{{ROLE}}` | Your current role or focus | Backend developer |
| `{{CURRENT_PROJECT}}` | What you're building now | A CLI habit tracker |
| `{{LEARNING}}` | What you're studying | FastAPI, async Python |
| `{{BLOG_URL}}` | Your blog or site | https://pythonlife.dev |
| `{{LINKEDIN}}` | LinkedIn handle | janedoe |
| `{{EMAIL}}` | Contact email | jane@example.com |

### Brand palette (swap in your official PythonLife colors if different)

| Use | Hex |
|---|---|
| Python blue | `3776AB` |
| Python yellow | `FFD43B` |
| Dark background | `0D1117` |

Badges use [shields.io](https://shields.io), which is reliable and needs no setup.

---

## Template 1 — The Clean Classic

**Best for:** beginners and anyone who wants a tidy, fast-loading profile.
**Why it works:** short, scannable, with one clear call to action. No external widgets that can break.

````markdown
<!-- PythonLife · Template 1: The Clean Classic -->

<h1 align="center">Hi, I'm {{NAME}} 👋</h1>

<p align="center">
  <b>{{TAGLINE}}</b><br>
  Part of the <a href="{{BLOG_URL}}">PythonLife</a> community 🐍
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python">
  <img src="https://img.shields.io/github/followers/{{USERNAME}}?style=for-the-badge&color=3776AB" alt="Followers">
  <img src="https://img.shields.io/github/stars/{{USERNAME}}?style=for-the-badge&color=FFD43B&labelColor=0D1117" alt="Stars">
</p>

---

### 🔭 Right now
- 🛠️ Building: **{{CURRENT_PROJECT}}**
- 📚 Learning: **{{LEARNING}}**
- 💬 Ask me about: Python basics, automation, clean code

### 🧰 Toolbox
| Area | Tools |
|---|---|
| Language | Python 3 |
| Web | Flask · FastAPI |
| Data | pandas · SQLite |
| Workflow | Git · pytest · VS Code |

### 📫 Say hello
[Blog]({{BLOG_URL}}) · [LinkedIn](https://linkedin.com/in/{{LINKEDIN}}) · [Email](mailto:{{EMAIL}})

<sub>🐍 Made with PythonLife templates</sub>
````

---

## Template 2 — `about_me.py` (the Pythonic profile)

**Best for:** developers who want something memorable and original.
**Why it works:** your profile *is* valid Python, which shows personality and teaches by example. GitHub syntax-highlights it automatically.

````markdown
<!-- PythonLife · Template 2: about_me.py -->

```python
# about_me.py — the PythonLife way

from dataclasses import dataclass, field


@dataclass
class Developer:
    name: str = "{{NAME}}"
    role: str = "{{ROLE}}"
    github: str = "{{USERNAME}}"
    brand: str = "PythonLife 🐍"
    currently_building: str = "{{CURRENT_PROJECT}}"
    currently_learning: list[str] = field(default_factory=lambda: [
        "{{LEARNING}}",
        "writing better tests",
    ])
    values: tuple[str, ...] = (
        "readability counts",
        "simple is better than complex",
        "learn in public",
    )

    def say_hi(self) -> str:
        return f"Hi, I'm {self.name} — {self.role}. Let's build something."


if __name__ == "__main__":
    me = Developer()
    print(me.say_hi())
```

<p>
  <a href="{{BLOG_URL}}"><img src="https://img.shields.io/badge/Blog-3776AB?style=flat-square&logo=hashnode&logoColor=white" alt="Blog"></a>
  <a href="https://linkedin.com/in/{{LINKEDIN}}"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&logo=linkedin&logoColor=FFD43B" alt="LinkedIn"></a>
  <a href="mailto:{{EMAIL}}"><img src="https://img.shields.io/badge/Email-FFD43B?style=flat-square&logo=gmail&logoColor=0D1117" alt="Email"></a>
</p>

> 💡 *Import this, never `import this` at 2 a.m.*
````

**Customize:** add fields like `favorite_libraries`, `coffee_per_day: int`, or a `hire_me()` method. Keep it runnable.

---

## Template 3 — Learning in Public (30-Day Python Journey)

**Best for:** learners, bootcamp students, career switchers.
**Why it works:** shows consistent progress, which recruiters value as much as polished projects. You update checkboxes and a log; nothing else.

````markdown
<!-- PythonLife · Template 3: Learning in Public -->

# {{NAME}}'s Python Journey 🐍

> Learning Python in public with **PythonLife**. Started: `{{START_DATE}}`

![Progress](https://img.shields.io/badge/Progress-0%25-FFD43B?style=for-the-badge&labelColor=3776AB)
<!-- Update the 0% as you go, e.g. Progress-40%25 (%25 is the percent sign) -->

## 🗺️ Roadmap

**Week 1 — Foundations**
- [ ] Variables, types, input/output
- [ ] Conditionals and loops
- [ ] Functions
- [ ] Mini project: number guessing game

**Week 2 — Data and files**
- [ ] Lists, dicts, sets, tuples
- [ ] Reading and writing files
- [ ] Error handling
- [ ] Mini project: expense tracker (CSV)

**Week 3 — Real-world Python**
- [ ] Modules and packages, `pip`, virtual environments
- [ ] Working with APIs (`requests`)
- [ ] Intro to testing (`pytest`)
- [ ] Mini project: weather CLI

**Week 4 — Ship it**
- [ ] Git and GitHub workflow
- [ ] Write a proper project README
- [ ] Publish one project end to end
- [ ] Write a "what I learned" post

## 📓 Daily log

| Day | Topic | What I built or learned | Link |
|---|---|---|---|
| 1 | Setup | Installed Python, ran `hello.py` | [code](#) |
| 2 | | | |
| 3 | | | |

## 🏗️ Projects so far

| Project | What it does | Status |
|---|---|---|
| [guess-the-number](#) | Terminal game | ✅ Done |
| [expense-tracker](#) | Tracks spending in CSV | 🚧 In progress |

## 💬 Follow along
[Blog]({{BLOG_URL}}) · [LinkedIn](https://linkedin.com/in/{{LINKEDIN}})

<sub>🐍 PythonLife — learn it, build it, share it.</sub>
````

**Tip:** commit once per day with a message like `day-07: file handling notes`. Your contribution graph becomes part of the story.

---

## Template 4 — The Project Showcase (maintainer / portfolio)

**Best for:** developers with 3+ real projects who want to lead with their work.
**Why it works:** every project gets the same four facts (problem, stack, status, link), so a reader can judge your work in seconds.

````markdown
<!-- PythonLife · Template 4: Project Showcase -->

<div align="center">

# {{NAME}}
### {{ROLE}} · Python 🐍

<a href="{{BLOG_URL}}">PythonLife</a> ·
<a href="https://linkedin.com/in/{{LINKEDIN}}">LinkedIn</a> ·
<a href="mailto:{{EMAIL}}">Email</a>

</div>

## 👨‍💻 About
I build {{TAGLINE}}. I care about readable code, good docs, and tools that save people time.

## 🚀 Featured projects

| Project | Problem it solves | Stack | Status |
|---|---|---|---|
| [**project-one**](https://github.com/{{USERNAME}}/project-one) | One sentence on who it helps and how | Python · Click · pytest | ✅ Stable |
| [**project-two**](https://github.com/{{USERNAME}}/project-two) | One sentence | Python · FastAPI | 🚧 Active |
| [**project-three**](https://github.com/{{USERNAME}}/project-three) | One sentence | Python · pandas | 🧪 Experimental |

> Status key: ✅ Stable · 🚧 Active development · 🧪 Experimental · 📦 Archived

## 🧠 How I work
- **Docs first:** every project ships with install, usage, and example sections.
- **Tests:** `pytest` with CI on every push.
- **Style:** `ruff` + `black`, type hints on public functions.

## 🤝 Open to
- [ ] Open-source collaboration
- [ ] Freelance Python work
- [ ] Mentoring beginners
<!-- Tick the ones that apply: change [ ] to [x] -->

## ✍️ Latest from PythonLife
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
````

The "Latest from PythonLife" block fills itself in once you add the automation below.

---

## Bonus — Auto-update "Latest posts" with GitHub Actions

Keeps your profile fresh without manual edits. It uses **only the Python standard library**, so there is nothing to install.

### Step 1: add `scripts/update_posts.py` to your profile repo

```python
"""
update_posts.py — PythonLife profile README updater.

Reads an RSS feed and rewrites the section between the
<!-- BLOG-POST-LIST:START --> and <!-- BLOG-POST-LIST:END --> markers
in README.md. Standard library only.

Usage:
    python scripts/update_posts.py https://example.com/feed.xml 5
"""

from __future__ import annotations

import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

README = Path("README.md")
START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"


def fetch_posts(feed_url: str, limit: int) -> list[tuple[str, str]]:
    """Return up to `limit` (title, link) pairs from an RSS 2.0 feed."""
    req = urllib.request.Request(feed_url, headers={"User-Agent": "pythonlife-readme"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        root = ET.fromstring(resp.read())

    posts = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if title and link:
            posts.append((title, link))
        if len(posts) >= limit:
            break
    return posts


def render(posts: list[tuple[str, str]]) -> str:
    if not posts:
        return "_No posts yet. Check back soon!_"
    return "\n".join(f"- [{title}]({link})" for title, link in posts)


def update_readme(content: str, block: str) -> str:
    pattern = re.compile(f"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)
    if not pattern.search(content):
        raise SystemExit(f"Markers not found in {README}. Add {START} and {END}.")
    # A function replacement avoids backslash issues in post titles.
    return pattern.sub(lambda _: f"{START}\n{block}\n{END}", content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: update_posts.py FEED_URL [LIMIT]")

    feed_url = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    block = render(fetch_posts(feed_url, limit))
    original = README.read_text(encoding="utf-8")
    README.write_text(update_readme(original, block), encoding="utf-8")
    print(f"Updated README with {limit} posts max.")
```

### Step 2: add `.github/workflows/update-readme.yml`

```yaml
name: Update README posts

on:
  schedule:
    - cron: "0 6 * * *"   # daily at 06:00 UTC
  workflow_dispatch:       # lets you run it manually from the Actions tab

permissions:
  contents: write

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Update posts section
        run: python scripts/update_posts.py "https://YOUR-SITE/feed.xml" 5

      - name: Commit changes
        run: |
          git config user.name  "pythonlife-bot"
          git config user.email "bot@users.noreply.github.com"
          git add README.md
          git diff --cached --quiet || git commit -m "chore: update latest posts"
          git push
```

### Step 3: replace `https://YOUR-SITE/feed.xml` with your real RSS URL, then run the workflow once from the **Actions** tab.

---

## Quality checklist (before you publish)

- [ ] No leftover `{{` placeholders (search the file)
- [ ] Every link opens the right page
- [ ] Looks good in both **light and dark** mode (avoid white-only images)
- [ ] Under ~150 lines; the first screen tells people who you are
- [ ] Alt text on every image
- [ ] One clear call to action (blog, email, or project)

## Do's and don'ts

| Do | Don't |
|---|---|
| Lead with what you build and what you're learning | List 40 tech logos you've touched once |
| Keep widgets to 2 or 3 | Stack many third-party stat cards (they go down and leave broken images) |
| Update the "Right now" section monthly | Leave stale projects marked "in progress" |
| Link to real, documented repos | Link to empty repos |

---

<sub>🐍 **PythonLife** · Templates are free to use and adapt. Attribution is appreciated but not required.</sub>
