import random
def arpoja(tahkot):
      noppa = random.randint(1, tahkot)
      return noppa

tahkotLKM = int(input("Anna nopan tahkojen määrä: "))
while True:
   nopanluku = arpoja(tahkotLKM)
   print(nopanluku)
   if nopanluku == tahkotLKM:
       break

