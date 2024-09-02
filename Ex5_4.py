def list_cities():
    cities = []

    for _ in range(5):
        city = input("Enter the name of a city: ")
        cities.append(city)

    print("List of cities:")
    for city in cities:
        print(city)

# Call the function to test it
list_cities()

