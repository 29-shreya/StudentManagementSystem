
import json
import os

from pathlib import Path

# Store students.json in the same folder as this Python file.
FILE_NAME = Path(__file__).parent / "students.json"


def load_students():
    """Load student records from the JSON file."""

    if not FILE_NAME.exists():
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = json.load(file)

        if not isinstance(students, list):
            raise ValueError("Student data must be stored as a list.")

        return students

    except json.JSONDecodeError as error:
        raise ValueError(
            "The students.json file contains invalid JSON. "
            "Please check the file before continuing."
        ) from error

    except OSError as error:
        raise OSError(f"Unable to read student data: {error}") from error


def save_students(students):
    """Save student records safely to the JSON file."""

    if not isinstance(students, list):
        raise ValueError("Student records must be provided as a list.")

    temp_file = FILE_NAME.with_suffix(".tmp")

    try:
        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        # Replace the old file only after writing succeeds.
        os.replace(temp_file, FILE_NAME)

    except OSError as error:
        if temp_file.exists():
            temp_file.unlink()

        raise OSError(f"Unable to save student data: {error}") from error
