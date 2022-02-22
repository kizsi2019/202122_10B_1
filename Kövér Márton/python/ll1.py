import random

tarolo = []
szamok1 = []
szamok2 = []
szamok3 = []
szamok4 = []

for i in range(3):
    szam = random.randint(0, 25)
    szamok1.append(szam)
for i in range(3):
    szam = random.randint(0, 25)
    szamok2.append(szam)
for i in range(3):
    szam = random.randint(0, 25)
    szamok3.append(szam)
for i in range(3):
    szam = random.randint(0, 25)
    szamok4.append(szam)

tarolo.append(szamok1)
tarolo.append(szamok2)
tarolo.append(szamok3)
tarolo.append(szamok4)

print(tarolo)