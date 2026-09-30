"""
search_filter.py
Lookup, filter and ranking functions for the student records.
"""

from grade_calculator import calculate_average, determine_status


def find_student_by_id(students_db, student_id):
    """Return the record for student_id, or None if it doesn't exist."""
    return students_db.get(student_id.strip().upper())


def filter_by_status(students_db, status):
    """Return a new dict holding only the students whose status matches."""
    filtered = {}
    for student_id, data in students_db.items():
        if determine_status(calculate_average(data["scores"])) == status:
            filtered[student_id] = data
    return filtered


def get_top_performers(students_db, top_n=3):
    """
    Return the top_n students as (id, name, average) tuples, best first.
    Ties are broken by ID so the order is always the same.
    """
    ranked = [
        (sid, data["name"], calculate_average(data["scores"]))
        for sid, data in students_db.items()
    ]
    ranked.sort(key=lambda item: (-item[2], item[0]))
    return ranked[:top_n]
