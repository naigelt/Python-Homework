import random

class Car:

    def __init__(self, registration, top_speed,):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.kms_travelled = 0
        self.travel_hours = 0

    def info(self,):
        print("Your cars registration", self.registration, "\nYour cars top speed ", self.top_speed, "Km/h","\nYour cars current speed", self.speed, "Km/h", "\nKilometeres travelled", self.kms_travelled, "Km""\n")


    def accelerate(self ,change_speed):
        if 0 < self.speed + change_speed <= self.top_speed:
            self.speed = self.speed + change_speed
        elif self.speed + change_speed <= 0:
            self.speed = 0
        else:
            self.speed = self.top_speed

    def traveling(self, change_speed):
        self.kms_travelled = self.kms_travelled + self.speed * change_speed

    def travel_distance(self, hours):
        self.kms_travelled = self.kms_travelled + (self.speed * hours)
        self.travel_hours = self.travel_hours + hours

def car_making():
    cars = []
    for i in range (10):
        cars.append(Car("ABC-"+ str(i+1), random.randint(100, 200)))
    return cars

cars = car_making()
race_length = 10000

for car in cars:
    while car.kms_travelled < race_length:
        random_speed = random.randint(-10, 15)
        Car.accelerate(car, random_speed)
        Car.traveling(car, 1)
        if car.kms_travelled >= race_length:
            Car.info(car)
