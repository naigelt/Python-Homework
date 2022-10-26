
#happy = True
#print(happy)

#print(happy := True)

#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

# Sama kun ylemmät kommentit walrus operaattorilla

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)