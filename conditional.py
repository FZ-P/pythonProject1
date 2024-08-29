import math


#Check Zander Size
def check_zander_size():
    length = float(input("Enter the length of the zander in centimeters: "))

    if length >= 42:
        print("The zander meets the size limit.")
    else:
        difference = 42 - length
        print(f"Release the fish back into the lake. It is {difference:.2f} centimeters below the size limit.")


#Describe Cabin Class
def describe_cabin_class():
    cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")


#Hemoglobin Value
def check_hemoglobin():
    gender = input("Enter your biological gender (female/male): ").lower()
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

    if gender == "female":
        if 117 <= hemoglobin <= 155:
            print("Your hemoglobin value is normal.")
        elif hemoglobin < 117:
            print("Your hemoglobin value is low.")
        else:
            print("Your hemoglobin value is high.")
    elif gender == "male":
        if 134 <= hemoglobin <= 167:
            print("Your hemoglobin value is normal.")
        elif hemoglobin < 134:
            print("Your hemoglobin value is low.")
        else:
            print("Your hemoglobin value is high.")
    else:
        print("Invalid gender.")


#Check if a Year is a Leap Year
def check_leap_year():
    year = int(input("Enter a year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# Main menu function to run each program
def main_menu():
    print("Choose a program to run:")
    print("1. Check Zander Size")
    print("2. Describe Cabin Class")
    print("3. Check Hemoglobin Value")
    print("4. Check Leap Year")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_zander_size()
    elif choice == "2":
        describe_cabin_class()
    elif choice == "3":
        check_hemoglobin()
    elif choice == "4":
        check_leap_year()
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
