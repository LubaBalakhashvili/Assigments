import csv

def add_data_to_csv(file_path, data):
    try:
        with open(file_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(data)
            csvfile.write('\n')

        print("Data added to the CSV file successfully.")
    except Exception as e:
        print(f"Error adding data to the CSV file: {e}")



file_path = input("Enter the CSV file path: ")

id_value = input("Enter ID: ")
name_value = input("Enter Name: ")
age_value = input("Enter Age: ")
grade_value = input("Enter Grade: ")
subject_name_value = input("Enter Subject Name: ")
marks_value = input("Enter Marks: ")

data_to_add = [id_value, name_value, age_value, grade_value, subject_name_value, marks_value]

add_data_to_csv(file_path, data_to_add)

