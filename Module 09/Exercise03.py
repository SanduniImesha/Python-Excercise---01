class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change

        if self.speed > self.max_speed:
            self.speed = self.max_speed

        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours


# main program
car = Car("ABC-123", 142)
car.distance = 2000
car.accelerate(60)     # speed is now 60 km/h

car.drive(1.5)         # 60 km/h for 1.5 hours -> +90 km
print("Travelled distance:", car.distance)