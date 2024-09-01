# smallest_largest_number.py
def smallest_largest_number():
    numbers = []
    while True:
        input_str = input("Enter a number (or press Enter to quit): ")
        if input_str == "":
            break
        numbers.append(float(input_str))

    if numbers:
        print(f"Smallest number: {min(numbers)}")
        print(f"Largest number: {max(numbers)}")
    else:
        print("No numbers were entered.")

smallest_largest_number()

