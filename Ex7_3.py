def airport_manager():
    airports = {}

    while True:
        print("\nOptions:")
        print("1 - Enter a new airport")
        print("2 - Fetch an existing airport")
        print("3 - Quit")

        choice = input("Enter your choice (1, 2, 3): ")

        if choice == "1":
            icao = input("Enter the ICAO code of the airport: ").upper()
            name = input("Enter the name of the airport: ")
            airports[icao] = name
            print(f"Airport {name} with ICAO code {icao} has been added.")
        elif choice == "2":
            icao = input("Enter the ICAO code of the airport to fetch: ").upper()
            if icao in airports:
                print(f"The name of the airport is: {airports[icao]}")
            else:
                print("No airport found with that ICAO code.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


airport_manager()
