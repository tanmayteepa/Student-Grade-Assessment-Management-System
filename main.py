"""
main.py
Entry point for the Student Grade & Assessment Management System.
Shows the menu and calls the other modules.
"""

from validator import get_valid_choice, get_valid_student_id
from student_manager import add_student, update_student_scores, delete_student
from grade_calculator import calculate_average, assign_letter_grade
from search_filter import find_student_by_id, filter_by_status, get_top_performers
from report_writer import (display_all_students, display_class_statistics,
                           export_report_to_file)
from storage import load_students, save_students

MENU_OPTIONS = [str(i) for i in range(1, 11)]


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 45)
    print("  STUDENT GRADE & ASSESSMENT MANAGEMENT")
    print("=" * 45)
    print(" 1. Add New Student")
    print(" 2. Update Student Scores")
    print(" 3. Delete Student Record")
    print(" 4. View All Students")
    print(" 5. Search Student by ID")
    print(" 6. Filter Students (Pass/Fail)")
    print(" 7. View Top Performers")
    print(" 8. View Class Statistics")
    print(" 9. Export Report to File")
    print("10. Exit Application")
    print("=" * 45)


def show_student(students_db):
    """Menu option 5: look up one student."""
    student_id = get_valid_student_id("Enter Student ID to search: ")
    student = find_student_by_id(students_db, student_id)
    if student:
        avg = calculate_average(student["scores"])
        print(f"\nFound -> ID: {student_id} | Name: {student['name']} | "
              f"Marks: {student['scores']} | Avg: {avg:.2f} | Grade: {assign_letter_grade(avg)}")
    else:
        print(f"Error: Student ID '{student_id}' not found.")


def show_filtered(students_db):
    """Menu option 6: list only passed or only failed students."""
    status_choice = get_valid_choice("Filter by (1) Pass or (2) Fail? Choice: ", ["1", "2"])
    target = "Pass" if status_choice == "1" else "Fail"
    print(f"\n--- Students with Status: {target} ---")
    display_all_students(filter_by_status(students_db, target))


def show_top(students_db):
    """Menu option 7: top 3 students by average."""
    if not students_db:
        print("\nNo student records available.")
        return
    print("\n--- TOP PERFORMERS ---")
    for rank, (s_id, name, avg) in enumerate(get_top_performers(students_db, top_n=3), 1):
        print(f"{rank}. {name} (ID: {s_id}) - Average: {avg:.2f}")


def main():
    students_db = load_students()
    if students_db:
        print(f"Loaded {len(students_db)} saved student record(s).")

    try:
        while True:
            print_menu()
            choice = get_valid_choice("Select an option (1-10): ", MENU_OPTIONS)

            if choice == "1":
                add_student(students_db)
                save_students(students_db)
            elif choice == "2":
                update_student_scores(students_db)
                save_students(students_db)
            elif choice == "3":
                delete_student(students_db)
                save_students(students_db)
            elif choice == "4":
                display_all_students(students_db)
            elif choice == "5":
                show_student(students_db)
            elif choice == "6":
                show_filtered(students_db)
            elif choice == "7":
                show_top(students_db)
            elif choice == "8":
                display_class_statistics(students_db)
            elif choice == "9":
                export_report_to_file(students_db)
            elif choice == "10":
                print("\nThank you for using the Grade Management System. Goodbye!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted. Saving data and exiting...")

    save_students(students_db)


if __name__ == "__main__":
    main()
