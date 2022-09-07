def laskekolmioala(kanta, korkeus):
    A = (kanta * korkeus)/2
    print(f"Kolmion ala on {A:.2f}")
    return

ka = float(input("Anna kolmion kanta: "))
ko = float(input("Anna kolmion korkeus: "))
laskekolmioala(ka, ko)
print(f"pääohjelmassa kanta = {ka} ka korkeus = {ko}")
