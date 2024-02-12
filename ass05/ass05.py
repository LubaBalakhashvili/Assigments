#1
def string_to_utf8(input_string):
    utf8_representation = input_string.encode('utf-8')
    return utf8_representation

user_input = input("Enter a string: ")
utf8_result = string_to_utf8(user_input)

print("UTF-8 representation:", utf8_result)


#2
user_input = input("Enter a string: ")

stripped_input = user_input.strip()
lowercase_input = stripped_input.lower()
modified_input = lowercase_input.replace("python", "Python")

print("Modified string:", modified_input)

#3
user_input = input("Enter a string: ")

length = len(user_input)
half_index = length // 2
half_of_string = user_input[:half_index]

print("Half of the string:", half_of_string)

#5
original_string = input("Enter a string: ")
bytes_representation = original_string.encode('utf-8')

print("Bytes Representation:", bytes_representation)

decoded_string = bytes_representation.decode('utf-8')
print("Decoded String:", decoded_string)




