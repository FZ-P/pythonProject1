def find_greatest_numbers():
    numbers = []

    while True:
        input_str = input("Enter a number (or press Enter to quit): ")
        if input_str == "":
            break
        try:
            number = float(input_str)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    # Sort numbers in descending order and get the five greatest
    numbers.sort(reverse=True)
    top_five = numbers[:5]

    print("The five greatest numbers are:")
    for number in top_five:
        print(number)


# Run the function
if __name__ == "__main__":
    find_greatest_numbers()
