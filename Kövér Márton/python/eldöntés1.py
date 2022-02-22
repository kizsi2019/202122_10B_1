import random
lista = []
for i in range(5):
    szam = random.randint(1,7)
    lista.append(szam)
szam2 = int(input("Adj meg egy számot!"))
print(lista)

talalat = False
index = 0

while index < len(lista) and not talalat:
    if lista[index] == szam2:
        talalat = True
    index = index + 1

if talalat:
    print("Van ilyen szám a listában!")
else:
    print("Nincs ilyen szám a listában!")