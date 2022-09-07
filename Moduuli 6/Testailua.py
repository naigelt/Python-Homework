def toinenfunktio():
     print("ollaan toisessa funktiossa")


def tervehdi():
    print("Moi!")
    toinenfunktio()
    print("tämä on tervehdys funktiosta")
    return

print("ollaan pääohjelmassa")
tervehdi()
print("Ollaan takaisin pääoohjelmassa")
tervehdi()
tervehdi()
print("Nyt loppu")
