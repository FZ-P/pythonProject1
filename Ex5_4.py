def list_cities():
    cities = []

    for i in range(5):
        city = input(f"Enter the name of city {i + 1}: ")
        cities.append(city)

    print("List of cities:")
    for city in cities:
        print(city)


# Run the city list function
if __name__ == "__main__":
    list_cities()
