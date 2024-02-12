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

def update_student_grade(file_path, student_id, subject, updated_grade):
    student_data = read_student_data(file_path)

    if student_data:
        updated = False
        for student in student_data:
            if student['id'] == student_id and student['subject_name'] == subject:
                student['grade'] = updated_grade
                updated = True
                break

        if updated:
            try:
                with open(file_path, 'w', newline='') as csvfile:
                    fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
                    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    csv_writer.writeheader()

                    csv_writer.writerows(student_data)

                print(f"Grade updated successfully for Student with ID {student_id} in {subject}.")
            except Exception as e:
                print(f"Error updating grade: {e}")
        else:
            print(f"No matching student found with ID {student_id} and subject {subject}.")
    else:
        print("No student data available.")


file_path = input("Enter the CSV file path: ")
student_data = read_student_data(file_path)

if student_data:
    student_id = input("Enter the ID of the student: ")
    subject = input("Enter the subject: ")
    updated_grade = input("Enter the updated grade: ")

    update_student_grade(file_path, student_id, subject, updated_grade)

