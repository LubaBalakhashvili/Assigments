from student_management_system import StudentManagementSystem

student_system = StudentManagementSystem()

while True:
    #let users choose actions they want to do with students list
    print("\nMenu:")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by number")
    print("4. Update student's grade")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    #depending on choice, functions are called from student manager class
    if choice == '1':
        print("\nEnter details for the new student:")
        name = input("Name: ")
        roll_number = input("Roll Number: ")
        grade = input("Grade: ")
        student_system.add_student(name, roll_number, grade)

    elif choice == '2':
        student_system.view_students()

    elif choice == '3':
        roll_number = input("\nEnter the Roll Number to search for: ")
        student_system.search_student_by_number(roll_number)

    elif choice == '4':
        roll_number = input("\nEnter the Roll Number of the student to update grade: ")
        new_grade = input("Enter the new grade: ")
        student_system.update_student_grade(roll_number, new_grade)

    elif choice == '5':
        print("\nExiting the program. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a valid option.")