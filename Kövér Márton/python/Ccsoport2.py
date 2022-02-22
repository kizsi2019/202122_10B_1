import random 
szamlista = []
for i in range(5):
    szam = random.randint(1,10)
    szamlista.append(szam)
print(szamlista)
osszeg = 0
for szam in szamlista:
    if szam % 2 == 0:
         osszeg = osszeg + 1
print("A páros számok száma:", osszeg)