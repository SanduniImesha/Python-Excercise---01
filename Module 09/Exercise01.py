class Car:
 def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0


# main program

car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Max speed:", car.max_speed)
print("Current speed:", car.speed)
print("Travelled distance:", car.distance)