# Ex2_2.py
import math

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")

# Call the function
calculate_circle_area()
