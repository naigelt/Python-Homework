
class Car:

    color = None

class Motorcycle:

    color = None
def change_color(vehicle, color):

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "Red")
change_color(car_2, "Blue")
change_color(car_3, "Black")
change_color(bike_1, "Purple")

print(f"Your car is " +car_1.color)
print(f"Your car is " +car_2.color)
print(f"Your car is " +car_3.color)
print(f"Your Bike is " +bike_1.color)