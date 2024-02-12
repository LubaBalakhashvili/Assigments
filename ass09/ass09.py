#1
def group_lists(list1, list2):
    zipped_lists = zip(list1, list2)
    result = [f"({x}, '{y}')" for x, y in zipped_lists]
    
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

output = group_lists(list1, list2)
print(output)

#2
from functools import reduce

def product_of_elements(numbers):
    try:
        result = reduce(lambda x, y: x * y, numbers)
        return result
    except TypeError:
        return "Error: All elements in the list must be numbers."

numbers_list = [1, 2, 3, 4, 5]
output = product_of_elements(numbers_list)
print(f"The product of the elements is: {output}")

#3
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_odd_numbers = lambda x: x % 2 != 0

result = list(filter(get_odd_numbers, numbers_list))

print(result)

#4
def filter_strings_by_ending(string_list, ending):
    try:
        filter_by_ending = lambda x: x.endswith(ending)
        
        result = list(filter(filter_by_ending, string_list))
        return result
    except TypeError:
        return "Error: First parameter must be a list of strings."


string_list = ['hello', 'world', 'coding', 'nod']
ending = 'ing'

output = filter_strings_by_ending(string_list, ending)
print(f"The strings ending with '{ending}' are: {output}")
