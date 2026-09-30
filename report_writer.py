"""
report_writer.py
Prints the tables on screen and writes the text report to a file.
If the current folder can't be written to, it tries Desktop, then Home.
"""

from pathlib import Path
from grade_calculator import (calculate_average, assign_letter_grade,
                              determine_status, class_statistics)

WIDTH = 60
HEADER = f"{'ID':<10} {'Name':<20} {'Average':<10} {'Grade':<8} {'Status':<8}"


def _row(student_id, data):
    """One formatted table row for a student."""
    avg = calculate_average(data["scores"])
    return (f"{student_id:<10} {data['name']:<20} {avg:<10.2f} "
            f"{assign_letter_grade(avg):<8} {determine_status(avg):<8}")


def _stats_lines(students_db):
    """Lines describing class statistics (empty list if no students)."""
    stats = class_statistics([calculate_average(d["scores"]) for d in students_db.values()])
    if stats is None:
        return []
    return [
        f"Students          : {stats['count']}",
        f"Class average     : {stats['class_average']:.2f}",
        f"Highest average   : {stats['highest']:.2f}",
        f"Lowest average    : {stats['lowest']:.2f}",
        f"Passed / Failed   : {stats['passed']} / {stats['failed']}",
        f"Pass percentage   : {stats['pass_rate']:.1f}%",
    ]


def display_all_students(students_db):
    """Print all students as a table."""
    if not students_db:
        print("\nNo student records found.")
        return

    print("\n" + "=" * WIDTH)
    print(HEADER)
    print("=" * WIDTH)
    for student_id, data in students_db.items():
        print(_row(student_id, data))
    print("=" * WIDTH)


def display_class_statistics(students_db):
    """Print class average, highest/lowest and pass rate."""
    lines = _stats_lines(students_db)
    if not lines:
        print("\nNo student records available.")
        return
    print("\n--- CLASS STATISTICS ---")
    print("\n".join(lines))


def _write_file_data(file_path, students_db):
    """Write the full report to file_path."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("=" * WIDTH + "\n")
        f.write("STUDENT GRADE MANAGEMENT REPORT".center(WIDTH) + "\n")
        f.write("=" * WIDTH + "\n\n")
        f.write(HEADER + "\n")
        f.write("-" * WIDTH + "\n")
        for student_id, data in students_db.items():
            f.write(_row(student_id, data) + "\n")
        f.write("-" * WIDTH + "\n\n")
        f.write("\n".join(_stats_lines(students_db)) + "\n")
        f.write("=" * WIDTH + "\n")


def export_report_to_file(students_db, filename="grade_report.txt"):
    """Save the report. Falls back to Desktop/Home if the folder is protected."""
    if not students_db:
        print("\nCannot export: no student records available.")
        return

    local_path = Path(filename).resolve()
    try:
        _write_file_data(local_path, students_db)
        print(f"\nSuccess: report saved to:\n{local_path}")
        return
    except PermissionError:
        print("\nNotice: this folder is write-protected, trying another location...")
    except OSError as e:
        print(f"\nError writing report: {e}")
        return

    fallback_dir = Path.home() / "Desktop"
    if not fallback_dir.exists():
        fallback_dir = Path.home()
    fallback_path = fallback_dir / filename
    try:
        _write_file_data(fallback_path, students_db)
        print(f"\nSuccess: report saved to:\n{fallback_path}")
    except OSError as e:
        print(f"\nError writing report to file: {e}")
