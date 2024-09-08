def determine_season():
    # Tuple of seasons; index represents the month (1-12)
    seasons = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
               "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter")

    while True:
        month = input("Enter the number of the month (1-12): ")
        if month.isdigit():
            month = int(month)
            if 1 <= month <= 12:
                print(f"The season for month {month} is {seasons[month - 1]}.")
                break
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        else:
            print("Please enter a valid number.")


determine_season()
