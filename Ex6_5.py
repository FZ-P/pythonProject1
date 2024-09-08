def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = remove_odds(numbers)
    print(f"Original list: {numbers}")
    print(f"List with odd numbers removed: {even_numbers}")

main()