import random

# Define the Car class
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.speed = 0  # Start speed at 0
        self.distance = 0  # Start distance at 0

    def accelerate(self, change):
        """Adjusts speed based on the change and ensures it stays within limits."""
        self.speed += change
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0

    def travel(self, hours):
        """Updates distance based on speed and time traveled."""
        self.distance += self.speed * hours

    def print_attributes(self):
        """Prints the current attributes of the car in table format."""
        print(
            f"{self.registration_number:<12} | {self.top_speed:>10} km/h | {self.speed:>6} km/h | {self.distance:>8} km")


# Main program
# Step 1: Create a list of 10 Car objects with random top speeds and unique registration numbers
cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    top_speed = random.randint(100, 200)
    car = Car(registration_number, top_speed)
    cars.append(car)

# Step 2: Simulate the race until a car reaches 10,000 km
race_finished = False
while not race_finished:
    for car in cars:
        # Random speed change between -10 and +15 km/h
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        # Make each car travel for 1 hour
        car.travel(1)

        # Check if any car has traveled 10,000 km or more
        if car.distance >= 10000:
            race_finished = True
            break

# Step 3: Print the final status of each car in a table format
print("\nThe race has ended! Final standings:")
print(f"{'Registration':<12} | {'Top Speed':>10} | {'Speed':>6} | {'Distance':>8}")
print("-" * 45)
for car in cars:
    car.print_attributes()
