# divisible_by_three.py
def divisible_by_three():
    number = 1
    while number <= 1000:
        if number % 3 == 0:
            print(number)
        number += 1

divisible_by_three()
