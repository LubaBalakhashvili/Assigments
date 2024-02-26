import math

memory = 0
history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number."
    else:
        return math.sqrt(x)

def floor_divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x // y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x % y
    
def clear_calculator():
    global memory
    global history
    memory = 0
    history = []
    print("\nCalculator memory and history cleared.")

def see_memory():
    global memory
    print(f"\nMemory: {memory}")

def see_history():
    print("\nCalculation History:")
    for entry in history:
        print(entry)


# This function does all the calculations (add, difference, multiplication, division, power, square root, floor division, modulus)
def start_calculation():
    print("\n>>>>>>> Starting Calculation <<<<<<<")
    global memory
    global history
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /, **, //, %, sqrt): ")
            
            if operation not in ('+', '-', '*', '/', '**', '//', '%', 'sqrt'):
                print("Invalid operation. Please enter +, -, *, /, **, //, % or sqrt.")
                continue

            #if entered operation is square root we don't need second number
            if operation == 'sqrt':
                if num1 < 0:
                    print("Error: Square root operation requires a non-negative number.")
                    continue
                result = square_root(num1)
                num2 = 0
            else:
                num2 = float(input("Enter the second number: "))

            if operation == '/' and num2 == 0:
                print("Error: Cannot divide by zero.")
                continue

            if operation in ('**', '//', '%') and not num2.is_integer():
                print("Error: Exponentiation, floor division, and modulus require integer second operand.")
                continue

            if operation in ('//', '%') and num2 == 0:
                print("Error: Cannot perform floor division or modulus by zero.")
                continue

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '**':
                result = exponentiate(num1, num2)
            elif operation == '//':
                result = floor_divide(num1, num2)
            elif operation == '%':
                result = modulus(num1, num2)
            
            # make history of previous operations
            print(f"Result: {result}")
            if (num2): history.append(f"{num1} {operation} {num2} = {result}")
            else: history.append(f"{operation} {num1} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")

        # asks users if they want to save data in memory
        memory_operation = input("Do you want to store the result in memory? (M+/M-): ").lower()
        if memory_operation == 'm+':
            memory = result

        # asks users if they want to calculate another thing or make other actions
        another_calculation = input("Do you want to perform another calculation? (Yes/No): ").lower()
        if another_calculation != 'yes':
            break

def calculator():
    global memory
    while True:

        # User chooses what to do with calculator. Also numbers (1-5) and sentences are valid for actions
        print("\nWhat would you like to do? \n 1. Calculation\n 2. Show Memory\n 3. Show History\n 4. Clear\n 5. EXIT")
        action = input("Enter your choice: ").upper()

        if action == '1' or action == 'Calculation':
            start_calculation()
            continue
        elif action == '2' or action == 'Show Memory':
            see_memory()
            continue
        elif action == '3' or action == 'Show History':
            see_history()
            continue
        elif action == '4' or action == 'Clear':
            clear_calculator()
            continue
        elif action == '5' or action == 'EXIT':
            break
        else:
            print("Invalid action. Please enter correct number or action")
            continue

        

if __name__ == "__main__":
    calculator()
