import random

class Race:
    def __init__(self, lenght, name, cars):
        self.name = name
        self.race_lenght = lenght
        self.cars = cars
    def hour_spend(self):
        for car in self.cars:
            random_speed = random.randint(-50, 80)
            Car.accelerate(car, random_speed)
            car.traveling(1)
    def situation_info(self):
        for car in self.cars:
            Car.info(car)
    def race_over(self):
        for car in self.cars:
            if car.travel_distance >= self.race_lenght:
                return True
            else:
                continue

class Car:

    def __init__(self, registration, top_speed,):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.travel_distance = 0


    def info(self):
        print("Your cars registration", self.registration, "\nYour cars top speed ", self.top_speed,
              "Km/h","\nYour cars current speed", self.speed, "Km/h", "\nKilometeres travelled", self.travel_distance, "Km""\n")


    def accelerate(self, change_speed):
        if 0 < self.speed + change_speed <= self.top_speed:
            self.speed = self.speed + change_speed
        elif self.speed + change_speed <= 0:
            self.speed = 0
        else:
            self.speed = self.top_speed

    def traveling(self, change_speed):
        self.travel_distance = self.travel_distance + self.speed * change_speed


def car_making():
    cars = []
    for i in range (10):
        cars.append(Car("ABC-"+ str(i+1), random.randint(100, 200)))
    return cars

if __name__=='__main__':
    race = Race(8000, str("Bigcrashrace"), car_making())
    hour = 0
    while True:
        race.hour_spend()

        if race.race_over():
            print("Race over")
            race.situation_info()
            break
        else:
            hour = hour + 1
            if hour % 10 == 0:
                print(f"Hour: {hour}\n")
                race.situation_info()
            else:
                continue



