#1
number_list = []

while True:
    user_input = input("Enter 'a' to add a number, 'r' to remove a number, or 'e' to exit: ")

    if user_input == 'a':
        
        number = float(input("Enter a number to add to the list: "))
        number_list.append(number)
        print(f"Number {number} added to the list.")
       
    elif user_input == 'r':
        if not number_list:
            print("List is empty. Cannot remove a number.")
        else:
            
            number = float(input("Enter a number to remove from the list: "))
            if number in number_list:
                number_list.remove(number)
                print(f"Number {number} removed from the list.")
            else:
                print(f"Number {number} not found in the list.")
          

    elif user_input == 'e':
        print("Exiting the program.")
        break

    else:
        print("Invalid input. Please enter 'a', 'r', or 'e'.")
    
    print("Current List:", number_list)


#2
# a.
my_list = [43, '22', 12, 66, 210, ["hi"]]
index_210 = my_list.index(210)
print(f"a. Index of 210: {index_210}")

# b. 
my_list[-1].append("hello")
print(f"b. List after adding 'hello' to the last element: {my_list}")

# c.
del my_list[2]
print(f"c. List after deleting element at index 2: {my_list}")

# d.
my_list_2 = my_list.copy()
my_list_2.clear()
print(f"d. my_list: {my_list}")
print(f"   my_list_2 (cleared): {my_list_2}")


#3
import re

def validate_phone_number(phone_number):
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{3}$')

    if pattern.match(phone_number):
        return f"Valid phone number: {phone_number}"
    else:
        return "Invalid format"


user_input = input("Enter a phone number (format: (123) 456-789): ")

result = validate_phone_number(user_input)
print(result)
