import random


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

# create 10 cars with random max speed between 100 and 200 km/h
cars = []
for i in range(1, 11):
    max_speed = random.uniform(100, 200)
    registration_number = "ABC-" + str(i)
    cars.append(Car(registration_number, max_speed))

# race until one car has travelled at least 10000 km
while max(car.distance for car in cars) < 10000:
    for car in cars:
        change = random.uniform(-10, 15)
        car.accelerate(change)
        car.drive(1)

# print results as a table
print(f"{'Reg number':10} {'Max speed':>10} {'Speed':>10} {'Distance':>12}")
for car in cars:
    print(f"{car.registration_number:10} {car.max_speed:10.1f} {car.speed:10.1f} {car.distance:12.1f}")