#1
def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence[:n]

# Example usage:
n_terms = int(input("Enter the number of Fibonacci numbers you want: "))
result = fibonacci_sequence(n_terms)
print(f"Fibonacci sequence up to the {n_terms}-th term: {result}")


#2
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


#3
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


n = int(input("Enter an integer to calculate its factorial: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")


#4
def count_character_occurrences(input_string, character):
    count = 0

    for char in input_string:
        if char == character:
            count += 1

    return count

user_string = input("Enter a string: ")
user_character = input("Enter a character to count: ")

result = count_character_occurrences(user_string, user_character)
print(f"The character '{user_character}' appears {result} times in the string.")
