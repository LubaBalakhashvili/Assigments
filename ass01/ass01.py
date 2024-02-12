# 1. OPERATORS

def perform_operations(num1, num2):
    
    sum = num1 + num2
    diff = num1 - num2
    mult = num1 * num2

    if num2 != 0:
        div = num1 / num2
    else:
        div = "Cannot divide by zero"

    pow = num1 ** num2
    
    return sum, diff, mult, div, pow

print ("1. Operators")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = perform_operations(num1, num2)

print("Sum: ",result[0])
print("Difference: ",result[1])
print("Multiplication: ",result[2])
print("Division: ",result[3])
print("Power: ",result[4])



# 2. AREA OF RHOMBUS

def rhombus_area(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area

print ("2. Area Of Rhombus")

diagonal1 = float(input("Enter the first diagonal of the rhombus: "))
diagonal2 = float(input("Enter the second diagonal of the rhombus: "))

area = rhombus_area(diagonal1, diagonal2)
print("The area of the rhombus is: ", area)


# 3.METERS CONVERTER

def length_converter(meters):
    meters_to_cm = meters * 100
    meters_to_dm = meters * 10
    meters_to_mm = meters * 1000
    meters_to_miles = meters / 1609

    return meters_to_cm, meters_to_dm, meters_to_mm, meters_to_miles

print ("3. Meters Converter")

length_in_meters = float(input("Enter the length in meters: "))

result = length_converter(length_in_meters)


print(length_in_meters," meters is equal to:")
print(result[0]," centimeters")
print(result[1]," decimeters")
print(result[2]," millimeters")
print(result[3]," miles")


# 4. AREA OF TRIANGLE

def triangle_area(height, base):
    area = (1/2) * base * height
    return area

print ("4. Area of Triangle")

height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))


area = triangle_area(height, base)
print("The area of the triangle is: ",area)
