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


# main program
h = Elevator(0, 10)

h.go_to_floor(5)
h.go_to_floor(h.bottom_floor)