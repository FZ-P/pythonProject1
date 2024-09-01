# rectangle_dimensions.py
def rectangle_dimensions():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    area = length * width
    print(f"The perimeter of the rectangle is: {perimeter:.2f}")
    print(f"The area of the rectangle is: {area:.2f}")

rectangle_dimensions()
