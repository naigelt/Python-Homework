# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan ,
# kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.

inches = float(input("Anna tuuma numero kokonaislukuna.Negatiivinen luku lopettaa ohjelman: "))

while inches >= 0:
    print(inches * 2.54)
    inches = float(input("Anna tuuma numero kokonaislukuna. Negatiivinen luku lopettaa ohjelman "))