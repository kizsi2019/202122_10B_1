import random 
lista = []
for i in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)
print(lista)
darab = 0
for szam in lista:
    if szam % 2 == 0:
            darab = darab + 1
print("A páros számok száma:",darab)
