year = int(input("Anna vuosiluku "))

if year % 400 == 0.0 and year % 100 == 0.0:
    print("Vuosi on karkausvuosi")
elif  year % 4 == 0 and year % 100 != 0:
    print(f"{year} on karkausvuosi")
else:
    print(f"{Year} ei ole karkausvuosi")
