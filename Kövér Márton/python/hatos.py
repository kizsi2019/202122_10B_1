import random
szamlalo = 1
darab = 0
while szamlalo <= 20:
    szam = random.randint(1,12)
    if szam % 3 == 0:
        print(szam)
        darab = darab + 1
    szamlalo = szamlalo + 1
print(darab,"hárommal osztható számot talált!")