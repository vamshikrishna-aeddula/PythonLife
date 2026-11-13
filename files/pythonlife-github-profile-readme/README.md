<h1 align="center">🐍 PythonLife GitHub Profile README Templates</h1>

<p align="center">
  Four ready-to-use profile templates and an auto-updating "latest posts" script.<br>
  Practical, beginner-friendly, built in public.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-FFD43B?style=for-the-badge&labelColor=3776AB" alt="MIT License">
</p>

## Quick start

1. Create a **public** repo named exactly your GitHub username (e.g. `janedoe/janedoe`) with a `README.md`.
2. Pick a template from [`templates/`](templates) and paste it into your `README.md`.
3. Replace every `{{PLACEHOLDER}}` (search for `{{`).
4. Commit. Your profile updates immediately.

## Templates

| # | Template | Best for |
|---|---|---|
| 1 | [The Clean Classic](templates/01-clean-classic.md) | Beginners, fast and tidy |
| 2 | [about_me.py](templates/02-about-me-py.md) | A memorable, Pythonic profile |
| 3 | [Learning in Public](templates/03-learning-in-public.md) | Learners tracking a 30-day journey |
| 4 | [Project Showcase](templates/04-project-showcase.md) | Developers with 3+ real projects |

## Auto-update latest posts (optional)

1. Copy [`scripts/update_posts.py`](scripts/update_posts.py) into `scripts/` in your profile repo.
2. Copy [`examples/update-readme.yml`](examples/update-readme.yml) to `.github/workflows/update-readme.yml` and set your RSS feed URL.
3. Make sure your README contains the markers `<!-- BLOG-POST-LIST:START -->` and `<!-- BLOG-POST-LIST:END -->` (Template 4 already does).
4. Run the workflow once from the **Actions** tab.

The workflow lives in `examples/` on purpose, so it does not run inside this templates repo.

## Full guide

Placeholder reference, brand palette, quality checklist and do's and don'ts are in [`docs/GUIDE.md`](docs/GUIDE.md).

## Repository layout

```text
.
├── README.md
├── LICENSE
├── templates/
│   ├── 01-clean-classic.md
│   ├── 02-about-me-py.md
│   ├── 03-learning-in-public.md
│   └── 04-project-showcase.md
├── scripts/
│   └── update_posts.py
├── examples/
│   └── update-readme.yml
└── docs/
    └── GUIDE.md
```

## License

MIT. See [LICENSE](LICENSE).

<sub>🐍 PythonLife — learn it, build it, share it.</sub>
