# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

UI = input("Anna luku. Ohjelma loppuu, kun annat tyhjän merkkijonon: ")
lowest_num = 0
highest_num = 0
index = 0

while UI != "":

    number = int(UI)
    if lowest_num == 0:
        if index == 0:
            lowest_num = number

    if highest_num == 0:
        highest_num = number

    if number < lowest_num:
        lowest_num = number

    if number > highest_num:
        highest_num = number

    index += 1

    UI = input('Anna luku. Ohjelma loppuu, kun annat tyhjän merkkijonon: ')

print('Pienin syötetty luku: ' + str(lowest_num))
print('Suurin syötetty luku: ' + str(highest_num))