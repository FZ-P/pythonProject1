import random


#print numbers divisible by three
def print_divisible_by_three():
    num = 1
    while num <= 1000:
        if num % 3 == 0:
            print(num)
        num += 1


#convert inches to centimeters
def convert_inches_to_cm():
    while True:
        inches = input("Enter the length in inches (negative value to quit): ")
        if inches.strip() == "":
            print("Exiting conversion.")
            break
        try:
            inches = float(inches)
            if inches < 0:
                print("Exiting conversion.")
                break
            centimeters = inches * 2.54
            print(f"{inches:.2f} inches is equal to {centimeters:.2f} centimeters.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


#the smallest and largest number from user inputs
def find_smallest_and_largest():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input.strip() == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if numbers:
        print(f"Smallest number: {min(numbers)}")
        print(f"Largest number: {max(numbers)}")
    else:
        print("No numbers were entered.")


# Function to play the guessing game
def guess_the_number():
    number_to_guess = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print("Correct!")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Function to authenticate user
def authenticate_user():
    correct_username = "python"
    correct_password = "rules"
    attempts = 0

    while attempts < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Welcome.")
            return
        else:
            attempts += 1
            print(f"Incorrect credentials. You have {5 - attempts} attempts left.")

    print("Access denied.")


# Function to approximate the value of Pi
def approximate_pi():
    try:
        total_points = int(input("Enter the number of random points to generate: "))
        inside_circle = 0

        for _ in range(total_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x ** 2 + y ** 2 <= 1:
                inside_circle += 1

        pi_approximation = 4 * (inside_circle / total_points)
        print(f"Approximation of Pi: {pi_approximation:.6f}")

    except ValueError:
        print("Invalid input. Please enter an integer value.")


# Main function to display the menu and execute selected option
def main_menu():
    while True:
        print("\nChoose a program to run:")
        print("1. Print Numbers Divisible by Three")
        print("2. Convert Inches to Centimeters")
        print("3. Find Smallest and Largest Number")
        print("4. Guess the Number Game")
        print("5. Authenticate User")
        print("6. Approximate Pi")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print_divisible_by_three()
        elif choice == "2":
            convert_inches_to_cm()
        elif choice == "3":
            find_smallest_and_largest()
        elif choice == "4":
            guess_the_number()
        elif choice == "5":
            authenticate_user()
        elif choice == "6":
            approximate_pi()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main_menu()
