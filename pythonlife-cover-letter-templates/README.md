# PythonLife Cover Letter Templates

![License: MIT](https://img.shields.io/badge/license-MIT-3776ab) ![Dependencies: none](https://img.shields.io/badge/dependencies-none-ffd43b) ![Version](https://img.shields.io/badge/version-1.0.0-3776ab)

Seven cover letter and outreach templates for Python developers, with a guide, a worked example, and a small linter that checks your letter before you send it.

## Templates

| # | Template | Best for |
|---|---|---|
| 01 | [Junior Python Developer](templates/01-junior-python-developer.md) | First Python role |
| 02 | [Career Switcher](templates/02-career-switcher.md) | Moving into Python from another field |
| 03 | [Backend and API Developer](templates/03-backend-api-developer.md) | Experienced engineers with measurable results |
| 04 | [Data Analyst and Data Scientist](templates/04-data-analyst-scientist.md) | Data roles |
| 05 | [Student and Internship](templates/05-student-internship.md) | Internships and placements |
| 06 | [Freelance Proposal](templates/06-freelance-proposal.md) | Pitching clients |
| 07 | [Referral and Cold Outreach](templates/07-referral-or-cold-outreach.md) | No open role, or a referral |

## Quick start

1. Open the template that fits your situation.
2. Copy the letter and replace every `{{PLACEHOLDER}}`. Search for `{{` to find them.
3. Run the linter: `python scripts/check_letter.py my_letter.txt --company "Acme"`
4. Send as a PDF.

## Documentation

- [Guide](docs/GUIDE.md): structure, tailoring, formatting, follow-up and checklist
- [Worked example](docs/EXAMPLE.md): a filled-in letter and why it works

## The linter

`scripts/check_letter.py` flags unfilled placeholders, length problems, generic phrases such as "team player", repetitive "I" openings and missing numbers. Standard library only, Python 3.9 or newer.

## Structure

```text
.
├── README.md
├── LICENSE
├── docs/
│   ├── GUIDE.md
│   └── EXAMPLE.md
├── templates/
│   └── 01 to 07 .md files
└── scripts/check_letter.py
```

## License

Released under the [MIT License](LICENSE).
