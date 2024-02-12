# 1. SUM

n = int(input("Enter number: "))

sum = 0

for i in range(n+1):
    sum += i

print(f"The sum of integers from 1 to {n} is: {sum}")


# 2. REVERSE

n = int(input("Enter number: "))

while n >= 1:
    print(n, end=" ")
    n -= 1


# 3. GUESS THE NUMBER

import random

number_to_guess = random.randint(1, 10)

user_guess = 0

while user_guess != number_to_guess:
    user_guess = int(input("\nGuess the number (between 1 and 10): "))

    if user_guess == number_to_guess: print("You guessed the correct number.")
    else: print("Try again.")


# 4. TOTAL SUM

total_sum = 0

while (1):
    user_input = input('Enter a number or "sum" to quit: ')

    if user_input.lower() == "sum": break
    if int(user_input) > 0: total_sum += int(user_input)

print(f"The sum is: {total_sum}")



