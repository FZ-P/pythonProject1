class Dog:
    # Class variable to count the number of Dog objects created
    created = 0

    # Initializer (constructor) to set up properties when a Dog is created
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created += 1  # Increment the class variable whenever a new Dog is created

    # Method to simulate barking a certain number of times
    def bark(self, times):
        for i in range(times):
            print(self.sound)

    # Method to display dog details
    def display_info(self):
        print(f"Dog's name is {self.name} and birth year is {self.birth_year}.")


# Creating two Dog objects with different properties
dog1 = Dog("Rascal", 2018)
dog2 = Dog("Bubbles", 2022, "Yip yip yip")

# Ask the user how many times each dog should bark
times1 = int(input("How many times should Rascal bark? "))
times2 = int(input("How many times should Bubbles bark? "))

# Call the bark method for each dog with user input
dog1.bark(times1)
dog2.bark(times2)

# Display information about each dog
dog1.display_info()
dog2.display_info()

# Print how many Dog objects have been created
print(f"{Dog.created} dogs have been created.")
