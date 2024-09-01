# numbers_operations.py
def numbers_operations():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    sum_ = a + b + c
    product = a * b * c
    average = sum_ / 3
    print(f"Sum: {sum_}")
    print(f"Product: {product}")
    print(f"Average: {average:.2f}")

numbers_operations()
