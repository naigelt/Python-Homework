#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
flag = 0
number = int(input('\nEnter whole number to check : '))
i = 2
while i <= (number / 2):
    if (number % i) == 0:
        flag = 1
        break
    i += 1
if number == 1:
    print(number, "is a special case, but not a prime number.")
elif flag == 0:
    print(number, " is a prime number.")
elif flag == 1:
    print(number, " is not a prime number.")