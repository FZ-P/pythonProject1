# Ex10_3.py

import random

class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        self.speed = max(0, min(self.speed, self.top_speed))

    def travel(self, hours):
        self.distance += self.speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.travel(1)

    def print_status(self):
        print(f"{'Registration':<12} | {'Top Speed':>10} | {'Speed':>6} | {'Distance':>8}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration_number:<12} | {car.top_speed:>10} km/h | {car.speed:>6} km/h | {car.distance:>8} km")

    def race_over(self):
        return any(car.distance >= self.distance for car in self.cars)

# Main program to run the race
if __name__ == "__main__":
    cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
    race = Race("Great Smashup Rally", 8000, cars)

    hour = 0
    while not race.race_over():
        race.hour_passes()
        hour += 1
        if hour % 10 == 0:
            print(f"\nAfter {hour} hours:")
            race.print_status()

    print("\nRace finished! Final standings:")
    race.print_status()
