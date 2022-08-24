
# kaikki grammoina, kun tiedät grammat, jaa grammat 1000 on yhtäkuin kilogrammat,
#math.floor tasaa alaspäin kokonais lukuun.
# kilot = math.floor(grammaa/1000)
#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.
import math

leviskät = float(input("Anna leviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

#laskut
massa = (luodit * 13.3) + (naulat *32 * 13.3) + (leviskät * 20 * 32 * 13.3)
kilo = massa // 1000
massa_g = massa % 1000
#tulosteet

(print(f"Massa nykymittojen mukaan {kilo:.0f} + kilogrammaa ja {massa_g:.2f} grammaa"))

