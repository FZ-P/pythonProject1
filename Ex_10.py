# Dog class definition
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)

# Hotel class definition
class Hotel:
    def __init__(self):
        self.dogs = []  # List to store dogs checked into the hotel

    def dog_checkin(self, dog):
        self.dogs.append(dog)  # Add the dog to the hotel
        print(f"{dog.name} checked in.")

    def dog_checkout(self, dog):
        self.dogs.remove(dog)  # Remove the dog from the hotel
        print(f"{dog.name} checked out.")

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)  # Each dog barks once when greeted

# Main program
dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

hotel = Hotel()  # Create a hotel object

hotel.dog_checkin(dog1)  # Check Rascal into the hotel
hotel.dog_checkin(dog2)  # Check Boi into the hotel

hotel.greet_dogs()  # Greet all the dogs (they will bark)

hotel.dog_checkout(dog1)  # Check Rascal out of the hotel
hotel.greet_dogs()  # Greet the remaining dogs (only Boi will bark)
