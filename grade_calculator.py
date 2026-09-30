"""
grade_calculator.py
Pure calculation code: averages, letter grades, pass/fail and class stats.
Nothing in here prints or asks for input, which makes it easy to test.
"""

PASSING_MARKS = 50.0


def calculate_average(scores):
    """Mean of a list of scores. Returns 0.0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def assign_letter_grade(average):
    """Turn an average into a letter grade (S, A, B, C, D or F)."""
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def determine_status(average, passing_marks=PASSING_MARKS):
    """Return 'Pass' if the average reaches the passing mark, else 'Fail'."""
    return "Pass" if average >= passing_marks else "Fail"


def class_statistics(averages):
    """
    Takes a list of student averages and returns a dict with the class
    average, highest, lowest and pass count/percentage.
    Returns None if the list is empty.
    """
    if not averages:
        return None
    passed = sum(1 for a in averages if determine_status(a) == "Pass")
    return {
        "count": len(averages),
        "class_average": calculate_average(averages),
        "highest": max(averages),
        "lowest": min(averages),
        "passed": passed,
        "failed": len(averages) - passed,
        "pass_rate": passed / len(averages) * 100,
    }
