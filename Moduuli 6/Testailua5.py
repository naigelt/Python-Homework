import math


def pizza_price(diameter, price):
    rad = (diameter / 100) / 2.0
    area = math.pi * rad ** 2
    return price / area

print("Welcome to the Python Pizza Price Price-calculator")
diam = float(input("What is the diameter of the pizza? "))
price = float(input("What is the price of the pizza? "))
pizza1 = pizza_price(diam, price)

diam = float(input("What is the diameter of the pizza? "))
price = float(input("What is the price of the pizza? "))
pizza2 = pizza_price(diam, price)

if pizza1 > pizza2:
    print("Pizza 2 is cheaper.")
else:
    print("Pizza 1 is cheaper.")
