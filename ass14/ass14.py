import json

def create_file(file_address, file_name):
    try:
        # Combine the file address and name to get the full path
        full_path = f"{file_address}/{file_name}"

        # Using the with statement to create the file
        with open(full_path, 'w') as file:
            print(f"File '{file_name}' created successfully at '{file_address}'.")
    except OSError as e:
        print(f"Error creating file: {e}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File not found at '{file_path}'."
    except OSError as e:
        return f"Error reading file: {e}"

def update_file_content(file_path, new_content):
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"File content updated successfully.")
    except OSError as e:
        print(f"Error updating file content: {e}")


# Get file address and name from user
file_address = input("Enter the file address (directory path): ")
file_name = input("Enter the file name: ")

# Create the file
create_file(file_address, file_name)

# Read and display the file content
file_path = f"{file_address}/{file_name}"
file_content = read_file(file_path)

if file_content:
    print(f"File content:\n{file_content}")

# Get new content from user and update the file
new_content = input("Enter new content to update the file: ")
update_file_content(file_path, new_content)

# Read and display the updated file content
updated_content = read_file(file_path)

if updated_content:
    print(f"Updated file content:\n{updated_content}")
