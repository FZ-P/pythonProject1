import math
import random

def greet_user():
    name = input("Fatema Zohora Prianka")
    print(f"Hello, {name}!")


# Function to Calculate the Area of a Circle
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f}")


# Function to Calculate Rectangle Properties
def calculate_rectangle_properties():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    area = length * width
    print(f"The perimeter of the rectangle is: {perimeter:.2f}")
    print(f"The area of the rectangle is: {area:.2f}")

def operate_on_integers():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    total_sum = num1 + num2 + num3
    product = num1 * num2 * num3
    average = total_sum / 3

    print(f"The sum of the numbers is: {total_sum}")
    print(f"The product of the numbers is: {product}")
    print(f"The average of the numbers is: {average:.2f}")

def convert_medieval_units():
    talents = float(input("Enter talents: "))
    pounds = float(input("Enter pounds: "))
    lots = float(input("Enter lots: "))

    total_pounds = talents * 20 + pounds
    total_lots = total_pounds * 32 + lots
    total_grams = total_lots * 13.3

    kilograms = int(total_grams // 1000)
    grams = total_grams % 1000

    print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")

def generate_combinations():
    code_3_digit = [random.randint(0, 9) for _ in range(3)]
    print(f"3-digit code: {''.join(map(str, code_3_digit))}")

    code_4_digit = [random.randint(1, 6) for _ in range(4)]
    print(f"4-digit code: {''.join(map(str, code_4_digit))}")

def main():
    greet_user()
    calculate_circle_area()
    calculate_rectangle_properties()
    operate_on_integers()
    convert_medieval_units()
    generate_combinations()

if __name__ == "__main__":
    main()

