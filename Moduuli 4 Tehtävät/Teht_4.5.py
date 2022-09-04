# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).
username = "python"
password = "rules"
login_succeeded = False
number_of_tries = 0

userNameInput = input("Give username: ")
passwordInput = input("Give password: ")
number_of_tries += 1

if userNameInput == username and passwordInput == password:
    login_succeeded = True

while login_succeeded == False and number_of_tries < 5:
    userNameInput = input("Give username ")
    passwordInput = input("Give password: ")
    number_of_tries += 1

    if userNameInput == username and passwordInput == password:
        login_succeeded = True

if login_succeeded == True:
    print("Welcome.")
else:
    print("Access.")