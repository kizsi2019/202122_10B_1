import random
szamlista = []
for i in range(5):
    szam = random.randint(1,10)
    szamlista.append(szam)
print(szamlista)
darab = 0
for elem in szamlista:
    if elem % 2 == 0:
        darab = darab + 1
print("A páros számok összege:", darab)