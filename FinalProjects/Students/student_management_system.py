from students import Student

class StudentManagementSystem:
    #creates a new array of students
    def __init__(self):
        self.students = []

    #adds stuents to the array of students. Checks if student roll number is unique
    def add_student(self, name, roll_number, grade):
        if not name or not roll_number.isdigit() or not grade.isalpha() or len(grade) != 1:
            print("Invalid input. Please provide valid information.")
            return

        existing_student = next((student for student in self.students if student.roll_number == int(roll_number)), None)
        if existing_student:
            print(f"A student with Roll Number {roll_number} already exists.")
        else:
            new_student = Student(name, int(roll_number), grade.upper())
            self.students.append(new_student)
            print(f"Student '{name}' added successfully.")

    #returns a list of students from array
    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(student)

    #finds the students with roll_number
    def search_student_by_number(self, roll_number):
        if not roll_number.isdigit():
            print("Invalid input. Please provide a valid roll number.")
            return

        found_student = next((student for student in self.students if student.roll_number == int(roll_number)), None)
        if found_student:
            print(f"\nStudent details for Roll Number {roll_number}:")
            print(found_student)
        else:
            print(f"No student found with Roll Number {roll_number}.")

    # finds student with roll number and changes student's grades
    def update_student_grade(self, roll_number, new_grade):
        if not roll_number.isdigit() or not new_grade.isalpha() or len(new_grade) != 1:
            print("Invalid input. Please provide valid roll number and grade.")
            return

        student = next((s for s in self.students if s.roll_number == int(roll_number)), None)
        if student:
            student.grade = new_grade.upper()
            print(f"Grade for student with Roll Number {roll_number} updated successfully.")
        else:
            print(f"No student found with Roll Number {roll_number}.")
