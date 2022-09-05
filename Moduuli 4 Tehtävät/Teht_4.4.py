# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random
random_num = random.randint(1, 10)
UI = int(input("The program has generated a random number, now try to guess the number: "))

while UI != random_num:
    if UI < random_num:
        print("Your answer is too low")
    else:
        print("Your guess is too high")

    UI = int(input("The program has generated a random number, now try to guess the number: "))
print("You are correct.")