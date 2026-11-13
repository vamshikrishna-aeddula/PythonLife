# ServiceNow Now Assist and AI Agents: 250 Practice Questions

![Questions](https://img.shields.io/badge/questions-250-3776ab) ![License: MIT](https://img.shields.io/badge/license-MIT-ffd43b) ![Release](https://img.shields.io/badge/ServiceNow-Australia-3776ab)

A study bank of 250 questions and answers on ServiceNow Now Assist, Otto, AI Agents, AI Agent Studio, Skill Kit, AI Control Tower and AI governance. Use it for interview preparation, certification study, team training and self-assessment.

Questions are grouped into 11 topics and tagged by level (54 Beginner, 149 Intermediate, 47 Advanced). Every answer is short, so you can recall it in an interview.

> Independent community resource. It is not affiliated with or endorsed by ServiceNow. ServiceNow, Now Assist and Otto are trademarks of ServiceNow, Inc.

## Topics

| # | Topic | Questions | Beginner / Intermediate / Advanced |
|---|---|---|---|
| 01 | [Platform AI Fundamentals and Licensing](questions/01-platform-ai-fundamentals-and-licensing.md) | 25 | 13 / 12 / 0 |
| 02 | [Now Assist for ITSM and ITOM](questions/02-now-assist-for-itsm-and-itom.md) | 20 | 6 / 10 / 4 |
| 03 | [Now Assist for CSM, HRSD and Other Workflows](questions/03-now-assist-for-csm-hrsd-and-other-workflows.md) | 20 | 6 / 11 / 3 |
| 04 | [Now Assist Skill Kit and Generative AI Controller](questions/04-now-assist-skill-kit-and-generative-ai-controller.md) | 25 | 4 / 15 / 6 |
| 05 | [Otto Panel, Virtual Agent and AI Search](questions/05-otto-panel-virtual-agent-and-ai-search.md) | 20 | 5 / 13 / 2 |
| 06 | [AI Agents Fundamentals](questions/06-ai-agents-fundamentals.md) | 30 | 9 / 18 / 3 |
| 07 | [AI Agent Studio, Tools and Triggers](questions/07-ai-agent-studio-tools-and-triggers.md) | 30 | 4 / 22 / 4 |
| 08 | [Orchestration, Multi-Agent and Agentic Workflows](questions/08-orchestration-multi-agent-and-agentic-workflows.md) | 25 | 1 / 14 / 10 |
| 09 | [Governance, Security and Responsible AI](questions/09-governance-security-and-responsible-ai.md) | 30 | 3 / 18 / 9 |
| 10 | [Platform Data and Integration](questions/10-platform-data-and-integration.md) | 15 | 3 / 10 / 2 |
| 11 | [Administration, Testing and Troubleshooting](questions/11-administration-testing-and-troubleshooting.md) | 10 | 0 / 6 / 4 |

## Study with the command-line quiz

```bash
python scripts/quiz.py                          # 10 random questions
python scripts/quiz.py -n 25 --level Advanced   # 25 advanced questions
python scripts/quiz.py --category 07            # AI Agent Studio only
python scripts/quiz.py --stats                  # counts by topic and level
```

The quiz uses only the Python standard library. It shows a question, waits for you to answer in your head, reveals the answer, and asks if you got it right.

## Data files

| File | Use |
|---|---|
| `data/questions.json` | All questions as structured data for apps and flashcards |
| `data/questions.csv` | Same data for spreadsheets and Anki-style imports |

Fields: `id`, `number`, `category`, `level`, `question`, `answer`.

## Accuracy and updates

Product names and features change quickly. Facts were checked against ServiceNow documentation, release notes and announcements available in November 2026, mainly for the Australia release. See [docs/SOURCES.md](docs/SOURCES.md). Always confirm details against your own instance, your release family and your entitlements before relying on them.

Notable naming changes: Otto is the new AI experience brand, the Now Assist panel is now the Otto panel, and the Now Assist Admin Console is now AI Admin Hub.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections and new questions with a source are welcome.

## License

Released under the [MIT License](LICENSE).
