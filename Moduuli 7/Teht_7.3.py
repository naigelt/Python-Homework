def Choose():
    print("1 - syötä uusi")
    print("2 - haku")
    print("0 - lopetus")
    valinta = -1
    while valinta < 0 or valinta > 2:
        valinta = int(input("Valitse: "))
    return valinta

# Lisää uuden lentoaseman annettuun sanakirjaan.
def Add(asemat):
    icao = input("Aseman ICAO-koodi : ")
    nimi = input("Aseman nimi       : ")
    asemat[icao] = nimi

# Tulostaa halutun aseman annetusta sanakirjasta.
def Search(asemat):
    ICAO = input("Aseman ICAO-koodi : ")
    if ICAO in asemat:
        print(asemat[ICAO])
    else:
        print("Tuntematon ICAO-koodi")
# Pääohjelma
#
lentoasemat = {}
valinta = Choose()
while valinta != 0:
    if valinta == 1:
        Add(lentoasemat)
    elif valinta == 2:
        Search(lentoasemat)
    valinta = Choose()


