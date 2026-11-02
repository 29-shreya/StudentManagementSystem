
from file_handler import load_students, save_students

# Load student records from the JSON file
students = load_students()


def save_data():
    """Save student records safely."""
    try:
        save_students(students)
        return True
    except (OSError, ValueError) as error:
        print(f"Error saving student data: {error}")
        return False


def display_student(student):
    """Display the details of one student."""
    print("--------------------------")
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Marks:", student["marks"])


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(student["id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)

    if save_data():
        print("Student added successfully!")


def view_students():
    print("\n--- All Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        display_student(student)


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent found!")
            display_student(student)
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("Leave a field empty to keep its old value.")

            name = input(
                f"New name [{student['name']}]: "
            ).strip()

            course = input(
                f"New course [{student['course']}]: "
            ).strip()

            marks_input = input(
                f"New marks [{student['marks']}]: "
            ).strip()

            # Validate marks before changing the record
            if marks_input:
                try:
                    marks = float(marks_input)

                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return

                except ValueError:
                    print("Please enter valid numeric marks.")
                    return

            # Update only the fields entered by the user
            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if marks_input:
                student["marks"] = marks

            if save_data():
                print("Student updated successfully!")

            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:

            confirm = input(
                f"Delete {student['name']}? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                students.remove(student)

                if save_data():
                    print("Student deleted successfully!")

            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
