class Car:

    current_speed = 0
    kms_travelled = 0

    def __init__(self, registration, top_speed,):
        self.registration = registration
        self.top_speed = top_speed


car_1 = Car("ABC-123", "142")

print(car_1.registration)
print(car_1.top_speed)
print(car_1.current_speed)
print(car_1.kms_travelled)