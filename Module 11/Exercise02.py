class Car:
    """Base class from the earlier exercise, included here so the file runs
    on its own. It tracks a registration number, a maximum speed, a current
    driving speed and a kilometer counter (odometer)."""

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.odometer = 0.0

    def accelerate(self, speed):
        # never allow the chosen speed to exceed the car's max speed
        if speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = speed

    def drive(self, hours):
        # distance = speed * time, added onto the running total
        self.odometer += self.speed * hours

    def __str__(self):
        return f"{self.registration_number}: {self.odometer} km"


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        # set up the shared properties via the base class initializer first
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_capacity):
        super().__init__(registration_number, max_speed)
        self.tank_capacity = tank_capacity


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(120)
    gasoline_car.accelerate(100)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Electric car odometer: {electric_car.odometer} km")
    print(f"Gasoline car odometer: {gasoline_car.odometer} km")


if __name__ == "__main__":
    main()