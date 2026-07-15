"""
Project Name: Student Grade Management System

Description:
This is a simple command-line student management system.
It allows you to:
- Add student records
- View all students
- Update student information
- Delete student records
- Show an individual student report card

Each student has:
- ID
- Name
- Marks
- Grade (calculated automatically)

Concepts Used:
- Variables
- Lists
- Dictionaries
- Functions
- Loops (while, for)
- Conditional statements (if, elif, else)
- User input using input()
- String formatting (f-strings)
- enumerate() function
- Basic input validation
"""

students = []  # List to store student dictionaries


def calculate_grade(mark):
    """Return grade based on marks."""
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'


def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")

    while True:
        marks = float(input("Enter Marks (Out of 100): "))
        if 0 > marks or marks >100:
            print("Invalid Marks!,\nPlease Enter the marks in range [0-100]")
        else :
            break

    grade = calculate_grade(marks)
    
    student = {
        "id": student_id,
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    print(f"{'ID':<10}{'Name':<20}{'Marks (Out of 100)':<25}{'Grade':<8}")
    print("-" * 65)

    for student in students:
        print(f"{student['id']:<10}{student['name']:<20}{student['marks']:<25}{student['grade']:<8}")


def update_student():
    student_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["marks"] = float(input("Enter New Marks: "))
            student["grade"] = calculate_grade(student["marks"])
            print("Record updated successfully!")
            return

    print("Student not found!")


def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid input!")
        return

    for i, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(i)
            print("Student deleted successfully!")
            return

    print("Student not found!")


def show_report_card():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == student_id:
            print("\n--- Report Card ---")
            print(f"{'ID:':<15}{student['id']}")
            print(f"{'Name:':<15}{student['name']}")
            print(f"{'Marks:':<15}{student['marks']}")
            print(f"{'Grade:':<15}{student['grade']}")

            print(f"{'Performance:':<15}", end="")
            if student["grade"] == 'A':
                print("Excellent")
            elif student["grade"] == 'B':
                print("Very Good")
            elif student["grade"] == 'C':
                print("Good")
            elif student["grade"] == 'D':
                print("Average")
            else:
                print("Fail")
            return

    print("Student not found!")


def main():
    while True:
        print("\n=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show Report Card")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            show_report_card()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


main()