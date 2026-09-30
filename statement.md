# Project Statement

## Project Title
**Student Grade & Assessment Management System**

## Problem Statement
In a lot of small classes, coaching centres and even college labs, marks are still kept in a notebook or a messy Excel sheet. When a teacher wants to know who is failing, who scored highest, or what the class average is, they end up adding and comparing numbers by hand. That takes time and it is easy to make a mistake, especially at the end of a term when everything is needed at once. Typing a wrong mark, giving the same ID to two students, or losing the file are also very common problems.

This project is a small program that takes care of that work. The teacher enters each student's marks once, and the program does the averages, grades, pass/fail decision, searching and report writing. It also refuses obviously wrong input (like a score of 250 or a blank name) so that the data stays clean.

## Objectives
1. Keep every student's record in one place, identified by a unique Student ID.
2. Calculate the average, letter grade and pass/fail status automatically instead of by hand.
3. Let the user find a student, filter by pass/fail and see the top scorers quickly.
4. Show simple class-level numbers (class average, highest, lowest, pass percentage).
5. Export a readable text report that can be printed or shared.
6. Stop bad input from crashing the program or corrupting the records.
7. Keep the code split into small modules so each part can be understood and tested on its own.

## Target Users
- **Teachers and tutors** who handle marks for one class or batch and need quick results.
- **Lab or department staff** who prepare simple result sheets.
- **Students learning Python**, since the code is written in plain Python with no external libraries and can be read from top to bottom.

The program is not meant for a whole university. It is built for a class-sized amount of data (tens or a few hundred students).

## Scope of the Project

### What is included
1. **Record management.** Add, update and delete students. Records are held in a Python dictionary with the Student ID as the key, and are saved to a JSON file so they are still there next time the program is opened.
2. **Grade calculation.** Each student has marks in three subjects (Math, Science, English). The average is worked out and mapped to a letter grade using the scale below. A student passes if the average is 50 or more.
3. **Searching and filtering.** Search by Student ID, list only passed or only failed students, and rank the top three students.
4. **Class statistics.** Number of students, class average, highest and lowest average, and how many passed/failed.
5. **File output.** A formatted `.txt` report with the student table and class statistics.
6. **Input validation.** Menu choices, IDs, names and scores are all checked before use.

### Grade scale used

| Average | Grade |
|---------|-------|
| 90 and above | S |
| 80 to 89.99 | A |
| 70 to 79.99 | B |
| 60 to 69.99 | C |
| 50 to 59.99 | D |
| Below 50 | F (Fail) |

### What is not included
- No login or user accounts (one person uses the program at a time).
- No graphical interface or website. It runs in the terminal.
- No database server. A single JSON file is enough for this size of data.
- Subjects are fixed to three. Changing them means editing one list in `student_manager.py`.

## High-Level Features
- Menu driven terminal interface with 10 options
- Add, update and delete student records
- Automatic average, letter grade and pass/fail status
- Search by Student ID (not case sensitive)
- Filter students by Pass or Fail
- Top 3 performers list
- Class statistics summary
- Export report to `grade_report.txt` (falls back to Desktop/Home if the folder is write-protected)
- Data saved automatically in `students_data.json`
- Unit tests for the calculation, search, validation and storage code

## Functional Requirements
| ID | Requirement |
|----|-------------|
| FR1 | The user can add a student with a unique ID, a name and three subject marks. |
| FR2 | The user can change the marks of an existing student. |
| FR3 | The user can delete a student record. |
| FR4 | The system shows all students with average, grade and status. |
| FR5 | The user can search for a student by ID. |
| FR6 | The user can filter students by Pass or Fail. |
| FR7 | The system shows the top three students by average. |
| FR8 | The system shows class statistics. |
| FR9 | The system exports a text report of all students. |
| FR10 | Records are saved after every change and loaded on start-up. |

## Non-Functional Requirements
1. **Usability.** Everything is done through a numbered menu, and error messages say what was wrong and what to type instead.
2. **Reliability / error handling.** Wrong input never crashes the program. Every input function loops until it gets something valid. A missing or damaged data file results in an empty database with a warning, not a crash. Pressing Ctrl+C saves the data before exiting.
3. **Maintainability.** The code is split into 7 modules with one job each, and the calculation code does not print or read input. Comments and docstrings explain each function.
4. **Data integrity.** Scores must be between 0 and 100, IDs must be unique and only letters/digits, names cannot contain digits.
5. **Portability.** It only needs Python 3.8+ and the standard library, so it runs on Windows, Linux and macOS with nothing to install.
6. **Performance.** All operations run in memory and finish instantly for class-sized data. Sorting for the top performers is O(n log n).
7. **Testability.** The logic is separated from input/output so it can be checked with unit tests.

## Assumptions
- Each student has exactly three subjects with equal weight.
- The pass mark is 50 for the average and is set in one constant in `grade_calculator.py`.
- Student IDs are not case sensitive (`24bce101` and `24BCE101` are the same student).
