"""
validator.py
All the input checking lives here so the other modules never have to
worry about bad input. Every function keeps asking until it gets
something usable.
"""


def get_non_empty_string(prompt):
    """Keep asking until the user types something that isn't blank."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")


def get_valid_student_id(prompt):
    """
    Student ID must be letters/digits only, up to 10 characters.
    Returned in upper case so 'abc1' and 'ABC1' are the same student.
    """
    while True:
        value = input(prompt).strip().upper()
        if not value:
            print("Error: ID cannot be empty.")
        elif not value.isalnum():
            print("Error: ID can only contain letters and digits (no spaces or symbols).")
        elif len(value) > 10:
            print("Error: ID can be at most 10 characters long.")
        else:
            return value


def get_valid_name(prompt):
    """Name must have at least one letter and only letters, spaces, . - ' in it."""
    while True:
        value = " ".join(input(prompt).split())  # also cleans up extra spaces
        if not value:
            print("Error: Name cannot be empty.")
        elif len(value) > 20:
            print("Error: Name is too long (max 20 characters).")
        elif not any(ch.isalpha() for ch in value) or \
                not all(ch.isalpha() or ch in " .-'" for ch in value):
            print("Error: Name should only contain letters, spaces, '.', '-' or an apostrophe.")
        else:
            return value


def get_valid_score(prompt):
    """Ask for a number between 0 and 100 (inclusive)."""
    while True:
        try:
            score = float(input(prompt).strip())
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue
        # float("nan") passes float() but fails this comparison, so it is caught too
        if 0 <= score <= 100:
            return score
        print("Error: Score must be between 0 and 100.")


def get_valid_choice(prompt, valid_choices):
    """Keep asking until the answer is one of valid_choices."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Error: Invalid selection. Please choose from {', '.join(valid_choices)}.")
