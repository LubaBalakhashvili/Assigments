import csv

def read_student_data(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            student_data = list(csv_reader)

        return student_data
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error reading data from file: {e}")
        return None

def display_all_students(student_data):
    if student_data:
        print("All Students:")
        for student in student_data:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Subject Name: {student['subject_name']}, Marks: {student['marks']}")
    else:
        print("No student data available.")

def display_specific_student(student_data, student_id):
    if student_data:
        for student in student_data:
            if student['id'] == student_id:
                print(f"Information for Student with ID {student_id}:")
                print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Subject Name: {student['subject_name']}, Marks: {student['marks']}")
                return
        print(f"No student found with ID {student_id}.")
    else:
        print("No student data available.")


file_path = input("Enter the CSV file path: ")

student_data = read_student_data(file_path)

if student_data:
    print("\nChoose an option:")
    print("1. All Student's Information.")
    print("2. Specific Student's Information.")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        display_all_students(student_data)
    elif choice == '2':
        student_id = input("Enter the ID of the student: ")
        display_specific_student(student_data, student_id)
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

