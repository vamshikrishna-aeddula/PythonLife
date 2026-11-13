# PythonLife - 50 Beginner Python Projects

Learn Python by building 50 small, useful, well-documented programs.
Every project is **one file**, uses only Python's **standard library** (nothing to install),
and has been tested: all 50 run in demo mode and all 50 have unit tests.

**Requires:** Python 3.8+ (tested on 3.12)

## Quick start
```bash
cd projects
python 01_tip_splitter.py          # interactive mode - type your own values
python 01_tip_splitter.py --demo   # automatic sample run, no typing needed
```

## Check that everything works
```bash
python run_all_demos.py            # runs all 50 projects in demo mode -> PASS/FAIL
python -m unittest test_projects -v   # 50 logic tests (correct answers, edge cases, errors)
```

## How each project file is organised
1. A **docstring** at the top: what it does, which concepts it teaches, how to run it.
2. **Pure functions / classes** holding the logic (easy to read and test).
3. `main()` - the interactive version.   4. `demo()` - sample data version.
5. `run(...)` from `pythonlife.py` - shows the PythonLife banner and handles `--demo`.

Your data (to-do lists, expenses, contacts...) is saved in a `.pythonlife` folder in your home directory.
In `--demo` mode a temporary folder is used, so demos never touch your real data.

## Suggested learning path
Do the projects in order. After each one, try the **challenge**: add one feature yourself
(for example: a new unit in project 02, a new question in project 16, a new category in project 30).

## Project index


### Level 1 - Calculators & Everyday Tools

| # | Project | Concepts you practise |
|---|---|---|
| 01 | `01_tip_splitter.py` - Tip & Bill Splitter | functions, dictionaries, input validation, round(). |
| 02 | `02_unit_converter.py` - Unit Converter | dictionaries as lookup tables, string methods, error handling. |
| 03 | `03_age_calculator.py` - Age & Birthday Countdown | datetime.date, calendar, leap years, tuples comparison. |
| 04 | `04_password_checker.py` - Password Strength Checker | regular expressions (re), sets, scoring logic, getpass. |
| 05 | `05_password_generator.py` - Secure Password & Passphrase Generator | the `secrets` module (safer than `random`), string constants, lists. |
| 06 | `06_bmi_calculator.py` - BMI & Healthy Weight Calculator | formulas, if/elif chains, returning multiple values. |
| 07 | `07_emi_calculator.py` - Loan EMI Calculator with Payment Schedule | financial formula, loops, tuple rows, formatted tables. |
| 08 | `08_sip_calculator.py` - SIP & Compound Interest Calculator | compounding, functions with default arguments, formatted output. |
| 09 | `09_currency_converter.py` - Offline Currency Converter with Editable Rates | JSON files, dictionaries, KeyError handling, persistence. |
| 10 | `10_gst_calculator.py` - GST Calculator | percentages, dictionaries, rounding money. |

### Level 2 - Games, Puzzles & Text

| # | Project | Concepts you practise |
|---|---|---|
| 11 | `11_number_guessing.py` - Number Guessing Game + Smart Bot | random, while loops, binary search (why it needs <= 7 guesses for 1-100). |
| 12 | `12_rock_paper_scissors.py` - Rock Paper Scissors with Scoreboard | dictionaries for rules, random.choice, collections.Counter. |
| 13 | `13_dice_simulator.py` - Dice Roller with Tabletop Notation & Histogram | regular expressions, random, Counter, string multiplication for bars. |
| 14 | `14_hangman.py` - Hangman: Python Vocabulary Edition | classes, properties, sets, game loops. |
| 15 | `15_tic_tac_toe.py` - Unbeatable Tic-Tac-Toe | lists, recursion, minimax decision making. |
| 16 | `16_python_quiz.py` - Python Basics Quiz | list of dictionaries, enumerate, grading logic, data-driven design. |
| 17 | `17_flashcards.py` - Spaced-Repetition Flashcards (Leitner Box) | classes, dictionaries, modulo, simulation. |
| 18 | `18_text_statistics.py` - Text Statistics & Reading-Time Analyzer | re, Counter, file reading, sets for stop-words. |
| 19 | `19_palindrome_anagram.py` - Palindrome & Anagram Toolkit | string cleaning, sorted(), dictionaries of lists (defaultdict). |
| 20 | `20_caesar_cipher.py` - Caesar Cipher: Encrypt, Decrypt & Crack | ord()/chr(), modulo arithmetic, dictionaries, basic cryptography. |
| 21 | `21_morse_code.py` - Morse Code Translator | dictionary, reversing a dictionary, split/join. |

### Level 3 - Productivity Apps with Saved Data

| # | Project | Concepts you practise |
|---|---|---|
| 22 | `22_todo_manager.py` - To-Do Manager with Priorities & Due Dates | classes, JSON persistence, sorting with key=, dates. |
| 23 | `23_expense_tracker.py` - Expense Tracker with Category & Monthly Reports | csv module, defaultdict, date strings, formatted reports. |
| 24 | `24_contact_book.py` - Contact Book with Search | dict of dicts, JSON, string cleaning, case-insensitive search. |
| 25 | `25_grade_calculator.py` - Student Marks, Grades & Rank List | nested dictionaries, sorted(), list comprehensions, enumerate. |
| 26 | `26_attendance_tracker.py` - Attendance Tracker with Shortage Alerts | classes, JSON, sets, percentage maths. |
| 27 | `27_habit_tracker.py` - Daily Habit Tracker with Streaks | sets, sorting, date arithmetic, JSON. |
| 28 | `28_study_planner.py` - Python Learning Roadmap Study Planner | lists of tuples, timedelta, while loops, weekday(). |
| 29 | `29_pomodoro_timer.py` - Pomodoro Focus Timer | time.sleep, divmod, passing functions as arguments (testable code!). |

### Level 4 - Files, Data & Automation

| # | Project | Concepts you practise |
|---|---|---|
| 30 | `30_file_organizer.py` - Downloads Folder Organizer | pathlib, shutil, dictionaries of sets, avoiding overwrites. |
| 31 | `31_duplicate_finder.py` - Duplicate File Finder | hashing (SHA-256), reading files in chunks, grouping with dicts. |
| 32 | `32_bulk_renamer.py` - Bulk File Renamer | pathlib, sorting, f-string number padding, safe two-step renaming. |
| 33 | `33_csv_analyzer.py` - CSV Data Analyzer | csv.DictReader, statistics module, try/except for type detection. |
| 34 | `34_log_analyzer.py` - Server Log Analyzer | regular expressions with groups, Counter, file processing. |
| 35 | `35_data_validator.py` - Indian Data Validator: Email, Mobile, PIN, PAN, IFSC | regular expressions, dictionaries of functions. |
| 36 | `36_calendar_planner.py` - Monthly Calendar Planner | the calendar module, dictionaries, string formatting. |

### Level 5 - Algorithms & Number Crunching

| # | Project | Concepts you practise |
|---|---|---|
| 37 | `37_prime_toolkit.py` - Prime Number Toolkit | algorithms, while loops, efficiency (checking only up to sqrt(n)). |
| 38 | `38_number_systems.py` - Number System Converter (Binary / Octal / Hex / any base) | divmod, while loops, string indexing, reversing. |
| 39 | `39_matrix_calculator.py` - Matrix Calculator | nested lists, zip, recursion, Gauss-Jordan elimination, fractions. |
| 40 | `40_roman_numerals.py` - Roman Numeral Converter with Validation | greedy algorithm, lists of tuples, round-trip validation. |
| 41 | `41_number_to_words.py` - Number to Words (Indian System: Lakh & Crore) | divmod, recursion, lists as lookup tables, Decimal for money. |

### Level 6 - OOP, Databases & Real-World Tools

| # | Project | Concepts you practise |
|---|---|---|
| 42 | `42_library_system.py` - Library Management System | classes & objects, dataclasses, custom errors, date arithmetic. |
| 43 | `43_bank_account.py` - Bank Account Simulator | OOP (classes, methods, encapsulation), custom exceptions, lists. |
| 44 | `44_inventory_manager.py` - Shop Inventory Manager with Low-Stock Alerts | dict of dicts, JSON persistence, business rules, formatted tables. |
| 45 | `45_student_database.py` - Student Database with SQLite | sqlite3, SQL (CREATE/INSERT/SELECT/UPDATE/DELETE/GROUP BY), |
| 46 | `46_notes_app.py` - Searchable Notes App with Tags (SQLite) | sqlite3, LIKE queries, datetime timestamps, simple data modelling. |
| 47 | `47_url_shortener.py` - Local URL Shortener with Click Counter | base-62 encoding, urllib.parse validation, dictionaries, JSON. |
| 48 | `48_markdown_to_html.py` - Mini Markdown to HTML Converter | regular expressions & substitution, html.escape (security!), |
| 49 | `49_html_extractor.py` - HTML Page Inspector: Title, Headings, Links, Images | html.parser.HTMLParser (event-driven parsing), inheritance. |
| 50 | `50_resume_keyword_matcher.py` - Resume vs Job Description Keyword Matcher (ATS Score) | regular expressions with word boundaries, sets, text files. |


## Notes
* Financial and health calculators (07, 08, 06) are **learning tools**, not professional advice.
  The currency rates in project 09 are sample values - edit them to current rates.
* Projects 04, 20 and 47 teach how things work; do not use the toy cipher (20) to protect real secrets.
* Project 50: only add a skill to your resume if you genuinely have it.

## License
Released under the **MIT License** - see the `LICENSE` file. You may use, modify and share
these projects (including in classes and courses) as long as the copyright notice and
license text are kept.

Happy coding - PythonLife
