#1
int_list = [10, 20, 30, 40]

def add_to_int_list(number):
    global int_list
    int_list.append(number)
    print(f"{number} added to the list. Updated list: {int_list}")

user_number = int(input("Enter a number to add to the list: "))
add_to_int_list(user_number)

#2
numbers_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = sum(numbers_list)
print(f"The sum of the numbers is: {result}")


#3
gl_str = "Global"

def create_local_variable():
    gl_str = "Local"
    return gl_str

result = create_local_variable()
print(f"Local variable: {result}")
print(f"Global variable: {gl_str}")

#4
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)

user_number = int(input("Enter a number: "))
result = sum_of_digits(user_number)
print(f"The sum of the digits of {user_number} is: {result}")

#5
def reverse_string(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return input_str[-1] + reverse_string(input_str[:-1])

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"The reversed string of '{user_input}' is: {result}")
