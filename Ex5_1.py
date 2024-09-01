import random


def roll_dice():
    # Ask user how many dice to roll
    num_dice = int(input("How many dice would you like to roll? "))

    # Roll the dice and calculate the sum
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)  # Dice roll between 1 and 6
        total += roll
        print(f"Rolled: {roll}")

    # Print the total sum of dice rolls
    print(f"Total sum of dice rolls: {total}")


# Run the dice rolling function
if __name__ == "__main__":
    roll_dice()
