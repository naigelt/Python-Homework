rahaa_taskussa =  int(input("Paljonko sinulla on rahaa? "))
maistuuko_kahvi = input("Maistuuko kahvi? ")
laten_hinta =  5
kahvin_hinta = 3
teen_hinta  = 2
if rahaa_taskussa >= laten_hinta and maistuuko_kahvi == "joo":
    print("Ostan latte")
    print("Juon latte")
    rahaa_taskussa = rahaa_taskussa - laten_hinta
elif rahaa_taskussa >= kahvin_hinta and maistuuko_kahvi == "joo":
    print("ostan normikahvi")
    rahaa_taskussa = rahaa_taskussa - kahvin_hinta
elif rahaa_taskussa >= teen_hinta:
    print("otan teen")
else:
    print("Lähden kotiin")

if rahaa_taskussa == 0:
    print("Rahat loppu")
else:
    print(f"Sinulla on vielä {rahaa_taskussa} euroa taskussa")