# 1. FIND NUMBER

print ("1.Find Number in List")

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

user_input = int(input("Enter a number: "))

if user_input in num_list:
    print(f"{user_input} is in the list.")
else:
    print(f"{user_input} is not in the list.")


# 2. EVEN OR ODD

print ("2.Even or Odd")

user_input = int(input("Enter an integer: "))

if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")

# 3. SAME STRINGS

print ("3.Same Strings")

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if str1 is str2:
    print("Same object")
else:
    print("Different object")


# 4. CHECK NUMBER

print ("4. Check Number")
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
user_input = int(input("Enter a number: "))
counter = 0


if (user_input > num_list[2] and user_input < num_list[len(num_list)-1]): print("More than list elements")
elif (user_input == num_list[5]): print("Equal")
else: print("None of the conditions were met")

