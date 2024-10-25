# Ex10_2.py

from Ex10_1 import Elevator  # Import Elevator class from Ex10_1.py

class Building:
    def __init__(self, lowest_floor, highest_floor, num_elevators):
        self.elevators = [Elevator(lowest_floor, highest_floor) for _ in range(num_elevators)]

    def operate_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Operating elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].move_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm! All elevators moving to the ground floor.")
        for elevator in self.elevators:
            elevator.move_to_floor(self.elevators[0].lowest_floor)

# Testing the Building class
if __name__ == "__main__":
    building = Building(1, 10, 3)
    building.operate_elevator(0, 7)
    building.operate_elevator(1, 3)
    building.fire_alarm()
