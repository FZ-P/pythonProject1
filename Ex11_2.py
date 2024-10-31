# Ex11_2.py

class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.speed = 0  # Current speed starts at 0
        self.distance = 0  # Distance traveled starts at 0

    def set_speed(self, speed):
        self.speed = min(speed, self.top_speed)  # Speed cannot exceed top speed

    def travel(self, hours):
        self.distance += self.speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, top_speed, battery_capacity):
        super().__init__(registration_number, top_speed)
        self.battery_capacity = battery_capacity  # Battery capacity in kWh

    def print_details(self):
        print(f"Electric Car: {self.registration_number}")
        print(f"Top Speed: {self.top_speed} km/h")
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Distance Traveled: {self.distance} km")

class GasolineCar(Car):
    def __init__(self, registration_number, top_speed, fuel_tank_capacity):
        super().__init__(registration_number, top_speed)
        self.fuel_tank_capacity = fuel_tank_capacity  # Fuel tank capacity in liters

    def print_details(self):
        print(f"Gasoline Car: {self.registration_number}")
        print(f"Top Speed: {self.top_speed} km/h")
        print(f"Fuel Tank Capacity: {self.fuel_tank_capacity} liters")
        print(f"Distance Traveled: {self.distance} km")

# Main program to test the car hierarchy
if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Set speed and drive for 3 hours
    electric_car.set_speed(100)
    gasoline_car.set_speed(120)

    electric_car.travel(3)
    gasoline_car.travel(3)

    # Print details of each car
    electric_car.print_details()
    print()  # Empty line for separation
    gasoline_car.print_details()
