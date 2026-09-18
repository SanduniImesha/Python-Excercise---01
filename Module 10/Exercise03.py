class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print("Elevator moved up to floor", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("Elevator moved down to floor", self.current_floor)

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


# main program
building = Building(0, 10, 3)

building.run_elevator(0, 7)
building.run_elevator(1, 3)
building.run_elevator(2, 10)

print("Fire alarm!")
building.fire_alarm()