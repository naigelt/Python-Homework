import random

class Car:
    number_of_cars = 0
    def __init__(self, registration, top_speed):
        Car.number_of_cars = Car.number_of_cars + 1
        self.car_number = Car.number_of_cars
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.travel_length = 0
    def print_info(self):
        print(f"Car {self.car_number}: {self.registration}, top speed: {self.top_speed} km/h, travelled:{self.travel_length} km.")


class Electric_car(Car):
    def __init__(self, registration, top_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration, top_speed)

    def print_info(self):
        super().print_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

class Gasoline_car(Car):

    def __init__(self, registration, top_speed, gasoline_tank_size):
        self.gasoline_tank_size = gasoline_tank_size
        super().__init__(registration, top_speed)

    def print_info(self):
        super().print_info()
        print(f"Fuel tanks size: {self.gasoline_tank_size} Liters")

class Race:
    def __init__(self, length, cars):
        self.race_length = length
        self.cars = cars
    def cars_speed_calculator(self):

        for car in self.cars:
            cars_acceleration = random.randint(10, 70)
            if 0 < car.speed + cars_acceleration < car.top_speed:
                car.speed = car.speed + cars_acceleration
            elif car.speed + cars_acceleration <= 0:
                car.speed = 0
            else:
                car.speed = car.top_speed
    def drive(self):
        for car in self.cars:
            car.travel_length = car.travel_length + (car.speed * self.race_length)


cars = []
cars.append(Electric_car("198-KLO", 190, 52.5))
cars.append(Gasoline_car("944-BCE", 200, 32.3))
for t in cars:
    t.print_info()

race = Race(3, cars)
race.cars_speed_calculator()
race.drive()
for t in cars:
    t.print_info()