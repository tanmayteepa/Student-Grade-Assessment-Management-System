# Student Grade & Assessment Management System

A command-line Python program for keeping student marks, working out grades, and making simple reports. I built it as my "Build Your Own Project" submission for the Python course on VITyarthi.

---

## Overview

Teachers often have to calculate averages and check who passed by hand. This program does that for you. You type in the marks for each student, and it works out the average, the letter grade and whether the student passed. You can also search for a student, see who is at the top, look at class statistics and save everything to a text report.

The whole thing runs in the terminal and uses only the Python standard library. The code is split into several small files so that each one has one job (input checking, calculations, searching, reports, saving). More detail on the problem and scope is in [`statement.md`](statement.md).

## Features

- Menu-driven interface (10 options)
- Add, update and delete student records
- Automatic average, letter grade (S/A/B/C/D/F) and Pass/Fail
- Search by Student ID (works with lower or upper case)
- Filter students by Pass or Fail
- Top 3 performers
- Class statistics: class average, highest, lowest, pass percentage
- Export a report to `grade_report.txt`
- Data is saved to `students_data.json` and loaded again next time
- Input checking for menu choices, IDs, names and scores
- Unit tests

## Technologies Used

- Python 3.8 or newer
- Standard library only: `json`, `pathlib`, `unittest`
- Git and GitHub for version control

No `pip install` is needed.

## Project Structure

```text
student_grade_system/
│
├── main.py                # Menu and main loop
├── validator.py           # Input checking (menu, ID, name, score)
├── student_manager.py     # Add / update / delete records
├── grade_calculator.py    # Average, letter grade, pass/fail, class stats
├── search_filter.py       # Search by ID, filter, top performers
├── report_writer.py       # Console tables and text report export
├── storage.py             # Save / load records as JSON
│
├── tests/
│   └── test_system.py     # Unit tests
│
├── statement.md           # Problem statement and scope
├── README.md              # This file
└── .gitignore
```

### How the modules connect

```text
                           main.py
        ______________________|______________________
       |          |           |            |         |
  validator  student_manager  search_filter  report_writer  storage
                  |               |             |
                  |               +------+------+
                  v                      v
            validator            grade_calculator
```

`grade_calculator.py` doesn't import any other project file, so it can be tested without any of the rest.

## How to Install and Run

1. Make sure Python 3.8+ is installed:
   ```bash
   python --version
   ```
2. Get the code:
   ```bash
   git clone <your-repository-link>
   cd student_grade_system
   ```
   (or just download the ZIP from GitHub and extract it)
3. Start the program:
   ```bash
   python main.py
   ```
   On some systems the command is `python3 main.py`.

## How to Use It

1. Choose **1** to add a student. Enter an ID (letters and digits only, up to 10 characters, e.g. `24BCE101`), the name, and the marks for Math, Science and English.
2. Choose **4** to see everyone in a table.
3. Use **5** to look up one student, **6** to see only the passed or failed ones, **7** for the top 3, and **8** for class statistics.
4. Choose **9** to save a report file, then **10** to exit.

Your records are saved automatically whenever you add, update or delete someone, so you won't lose them if you close the window.

### Grade scale

| Average | Grade |
|---------|-------|
| 90+ | S |
| 80 – 89.99 | A |
| 70 – 79.99 | B |
| 60 – 69.99 | C |
| 50 – 59.99 | D |
| below 50 | F |

A student passes with an average of 50 or more.

## Sample Output

Viewing all students (option 4):

```text
============================================================
ID         Name                 Average    Grade    Status
============================================================
A1         Asha                 95.00      S        Pass
B2         Bilal                38.33      F        Fail
C3         Chitra               65.00      C        Pass
============================================================
```

Class statistics (option 8):

```text
--- CLASS STATISTICS ---
Students          : 3
Class average     : 66.11
Highest average   : 95.00
Lowest average    : 38.33
Passed / Failed   : 2 / 1
Pass percentage   : 66.7%
```

Add your own screenshots of the running program in a `screenshots/` folder and link them here.

## Testing

The tests use Python's built-in `unittest`. From the project folder run:

```bash
python -m unittest discover tests -v
```

They cover:
- averages (including an empty list) and every grade boundary (49.99, 50, 89.99, 90 and so on)
- pass/fail decision and class statistics
- searching (upper/lower case, missing ID), filtering and top performer order
- input validation with fake keyboard input (bad numbers, out-of-range scores, blank or invalid IDs and names)
- add, update and delete, and rejecting duplicate IDs
- saving and loading, including a missing file and a corrupted file

I also tried the menu by hand, including typing letters where numbers were expected, and pressing Ctrl+C.

## Error Handling

- Non-numeric or out-of-range scores are rejected and asked again.
- Blank IDs, IDs with symbols, and names with digits are rejected.
- Duplicate IDs are not allowed.
- If the report can't be written in the current folder (permission error), it tries Desktop and then the Home folder.
- If the data file is missing or broken, the program starts with an empty list and prints a warning.

## Limitations

- Only three fixed subjects with equal weight.
- One user at a time, no login.
- Data is stored in one JSON file, which is fine for a class but not for thousands of records.

## Future Enhancements

- Let the user choose the subjects and their weightage
- Import and export CSV files
- A simple GUI (Tkinter) or web version
- Charts of the grade distribution
- Password protection for the records

## Author

Add your name, register number and course here.
