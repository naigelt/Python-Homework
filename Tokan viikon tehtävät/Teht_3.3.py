#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("Sukupuolesi? (nainen/mies) ")
hg_value = int(input("Anna hemoglobiini arvosi (g/l)? "))

if gender == "nainen":
    #TODO: testataan naisen ohjearvot
 if hg_value < 117:
    print("Hemoglobiini arvo on alhainen.")
 elif hg_value <= 175:
    print("Hemoglobiini arvo on normaali.")
 else:
    print("Hemoglobiini arvo on korkea.")

elif gender == "mies":
  if hg_value < 134:
      print("Hemoglobiini arvo on alhainen.")
  if hg_value <= 195:
     print("Hemoglobiini arvo on normaali.")
    #TODO: Miehen arvot
else:
     print("Hemoglobiini arvo on korkea.")

    #TODO: tulosta virheilmoitus(?)


