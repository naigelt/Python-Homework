class Car:

    def __init__(self, registration, top_speed,):
        self.registration = registration
        self.top_speed = top_speed
        self.current_speed = 0
        self.kms_travelled = 0

    def info(self,):
        print("Your cars registration", self.registration, "\nYour cars top speed ", self.top_speed, "Km/h","\nYour cars current speed", self.current_speed, "Km/h" ,"\nKilometeres travelled", self.kms_travelled, "Km")


    def accelerate(self ,change_speed):
        if 0 < self.current_speed + change_speed <= self.top_speed:
            self.current_speed = self.current_speed + change_speed
        elif self.current_speed + change_speed <= 0:
            self.current_speed = 0
        else:
            self.current_speed = self.top_speed

    def traveling(self, change_speed):
        self.kms_travelled = self.kms_travelled + (self.current_speed * change_speed)


car_1 = Car("ABC-123", 142)
car_1.accelerate(30)
car_1.accelerate(-20)
car_1.traveling(1)
car_1.info()