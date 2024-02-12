my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

def print_student_ids():
    student_ids = [student["id"] for student in my_dict["students"]]
    print("Available Student IDs:", ", ".join(map(str, student_ids)))

def print_student_info(student_id):
    student_info = next((student for student in my_dict["students"] if student["id"] == student_id), None)

    if student_info:
        print(f"Student information:\nID: {student_info['id']}, name: {student_info['name'].capitalize()}, age: {student_info['age']}")
        
        for subject in my_dict["subjects"]:
            grade = subject["grades"].get(str(student_id), "N/A")
            print(f"Subject: {subject['name']}, grade: {grade}")
    else:
        print(f"Student with ID {student_id} not found.")


print_student_ids()
student_id_input = int(input("Enter student ID: "))
print_student_info(student_id_input)
