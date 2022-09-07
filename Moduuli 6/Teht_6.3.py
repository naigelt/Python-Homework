def converter(gallon):
    liter = (gallon * 3.785)
    return liter

gallons = float(input("Give the liquid amount in gallons: "))
while gallons > 0:
    liters = converter(gallons)
    print(liters)
    gallons = float(input("Give the liquid amount in gallons: "))
    if liters < 0:
        break



