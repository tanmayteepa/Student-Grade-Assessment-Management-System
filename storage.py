"""
storage.py
Saves the records to a JSON file and loads them back on the next run,
so data isn't lost when the program closes.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "students_data.json"


def load_students(path=DATA_FILE):
    """Read records from disk. A missing or broken file gives an empty database."""
    if not Path(path).exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("unexpected file layout")
        return data
    except (OSError, ValueError) as e:  # JSONDecodeError is a ValueError
        print(f"Warning: could not load saved data ({e}). Starting with an empty database.")
        return {}


def save_students(students_db, path=DATA_FILE):
    """Write records to disk. Returns True on success."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(students_db, f, indent=2)
        return True
    except OSError as e:
        print(f"Warning: could not save data ({e}).")
        return False
