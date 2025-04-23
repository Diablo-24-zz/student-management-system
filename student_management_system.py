students = {}

def create_student(student_id, name, age, grade):
    students[student_id] = {
        'Name': name,
        'Age': age,
        'Grade': grade
    }
    print(f"Student {name} added successfully!")

def read_student(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Grade: {student['Grade']}\n")
    else:
        print(f"Student with ID {student_id} not found!")

def update_student(student_id, name=None, age=None, grade=None):
    if student_id in students:
        if name:
            students[student_id]['Name'] = name
        if age:
            students[student_id]['Age'] = age
        if grade:
            students[student_id]['Grade'] = grade
        print(f"Student ID {student_id} updated successfully!")
    else:
        print(f"Student with ID {student_id} not found!")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully!")
    else:
        print(f"Student with ID {student_id} not found!")

def display_students():
    if students:
        print("\nAll Students:")
        for student_id, student_info in students.items():
            print(f"ID: {student_id} - Name: {student_info['Name']} - Age: {student_info['Age']} - Grade: {student_info['Grade']}")
    else:
        print("No student records found!")

def search_students():
    print("\nSearch by:")
    print("1. Name")
    print("2. Grade")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        name = input("Enter student name to search: ").lower()
        found = False
        for student_id, student_info in students.items():
            if name in student_info['Name'].lower():
                print(f"\nFound - ID: {student_id} - Name: {student_info['Name']} - Age: {student_info['Age']} - Grade: {student_info['Grade']}")
                found = True
        if not found:
            print("No student found with that name.")
    
    elif choice == '2':
        grade = input("Enter student grade to search: ").upper()
        found = False
        for student_id, student_info in students.items():
            if grade == student_info['Grade']:
                print(f"\nFound - ID: {student_id} - Name: {student_info['Name']} - Age: {student_info['Age']} - Grade: {student_info['Grade']}")
                found = True
        if not found:
            print("No student found with that grade.")
    
    else:
        print("Invalid choice!")

def sort_students():
    print("\nSort by:")
    print("1. Name")
    print("2. Student ID")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        sorted_students = sorted(students.items(), key=lambda x: x[1]['Name'].lower())
        print("\nSorted by Name:")
        for student_id, student_info in sorted_students:
            print(f"ID: {student_id} - Name: {student_info['Name']} - Age: {student_info['Age']} - Grade: {student_info['Grade']}")
    
    elif choice == '2':
        sorted_students = sorted(students.items(), key=lambda x: x[0])
        print("\nSorted by Student ID:")
        for student_id, student_info in sorted_students:
            print(f"ID: {student_id} - Name: {student_info['Name']} - Age: {student_info['Age']} - Grade: {student_info['Grade']}")
    
    else:
        print("Invalid choice!")

def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student (Create)")
        print("2. View Student (Read)")
        print("3. Update Student Information")
        print("4. Delete Student (Delete)")
        print("5. Display All Students")
        print("6. Search Students")
        print("7. Sort Students")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            student_id = get_numeric_input("Enter Student ID (numeric only): ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")
            create_student(student_id, name, age, grade)

        elif choice == '2':
            student_id = get_numeric_input("Enter Student ID to view: ")
            read_student(student_id)

        elif choice == '3':
            student_id = get_numeric_input("Enter Student ID to update: ")
            name = input("Enter new Name (or press Enter to skip): ")
            age = input("Enter new Age (or press Enter to skip): ")
            grade = input("Enter new Grade (or press Enter to skip): ")
            update_student(student_id, name, age, grade)

        elif choice == '4':
            student_id = get_numeric_input("Enter Student ID to delete: ")
            delete_student(student_id)

        elif choice == '5':
            display_students()

        elif choice == '6':
            search_students()

        elif choice == '7':
            sort_students()

        elif choice == '8':
            print("Exiting the Student Management System...")
            break

        else:
            print("Invalid choice! Please enter a valid option (1-8).")

if __name__ == "__main__":
    main()
