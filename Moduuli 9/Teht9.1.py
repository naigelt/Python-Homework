class Car:

    def __init__(self, registration, top_speed, current_speed, kms_travelled):
        self.registration = registration
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.kms_travelled = kms_travelled

    def info(self,):
        print(self.registration, self.top_speed, "Km/h", self.current_speed, "Km/h", self.kms_travelled, "Km")


car_1 = Car("ABC-123", "142", 0, 0)
car_1.info()
