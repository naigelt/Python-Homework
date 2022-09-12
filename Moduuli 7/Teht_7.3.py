def Choose():
    print("1 - Enter a new one")
    print("2 - Search")
    print("0 - Stop")
    choice = -1
    while choice < 0 or choice > 2:
        choice = int(input("Choose: "))
    return choice

# Add a new one to the dictionary
def Add(airports):
    icao = input("Airports ICAO-code : ")
    name = input("Ports name       : ")
    airports[icao] = name

# Prints any given airport from the dictionary
def Search(airports):
    ICAO = input("Airports ICAO-code : ")
    if ICAO in airports:
        print(airports[ICAO])
    else:
        print("Unknown ICAO-code")
# Main
airports = {}
choice = Choose()
while choice != 0:
    if choice == 1:
        Add(airports)
    elif choice == 2:
        Search(airports)
    choice = Choose()


