"""
student_manager.py
Add, update and delete student records. The records live in a dict:
    { "24BCE101": {"name": "Riya", "scores": [80.0, 75.0, 90.0]}, ... }
"""

from validator import get_valid_student_id, get_valid_name, get_valid_score

SUBJECTS = ["Math", "Science", "English"]


def _read_scores(label):
    """Ask for one score per subject and return them as a list."""
    scores = []
    for subject in SUBJECTS:
        scores.append(get_valid_score(f"Enter {label}score for {subject} (0-100): "))
    return scores


def add_student(students_db):
    """Ask for details and add a new student. Duplicate IDs are rejected."""
    print("\n--- Add New Student ---")
    student_id = get_valid_student_id("Enter Student ID (e.g. 24BCE101): ")

    if student_id in students_db:
        print(f"Error: Student ID '{student_id}' already exists.")
        return

    name = get_valid_name("Enter Student Name: ")
    print(f"\nEnter marks for {len(SUBJECTS)} subjects:")
    scores = _read_scores("")

    students_db[student_id] = {"name": name, "scores": scores}
    print(f"Success: Student '{name}' (ID: {student_id}) added.")


def update_student_scores(students_db):
    """Replace the scores of an existing student."""
    print("\n--- Update Student Scores ---")
    student_id = get_valid_student_id("Enter Student ID to update: ")

    if student_id not in students_db:
        print(f"Error: Student ID '{student_id}' not found.")
        return

    print(f"Updating scores for: {students_db[student_id]['name']}")
    students_db[student_id]["scores"] = _read_scores("new ")
    print(f"Success: Scores updated for Student ID {student_id}.")


def delete_student(students_db):
    """Remove a student from the database."""
    print("\n--- Delete Student Record ---")
    student_id = get_valid_student_id("Enter Student ID to delete: ")

    if student_id in students_db:
        removed = students_db.pop(student_id)
        print(f"Success: Record for '{removed['name']}' (ID: {student_id}) removed.")
    else:
        print(f"Error: Student ID '{student_id}' not found.")
