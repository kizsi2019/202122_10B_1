import random
lista =[]
szamlalo = 0

while szamlalo < 10:
    szam = random.randint(1,3)
    lista.append(szam)
    szamlalo = szamlalo + 1
print("A lista tartalma: ", lista)
szam2 = int(input("Adj meg egy számot! "))
szamlalo2 = 0
for i in lista:
    if i == szam2:
        del lista[i]
print("Módosított lista: ", lista)