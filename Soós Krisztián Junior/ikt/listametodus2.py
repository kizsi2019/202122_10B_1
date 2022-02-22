import random

lista = []

szamlalo = 0


while szamlalo < 10:
    
    szam = random.randint(1,3)
    szamlalo = szamlalo +1
    
    lista.append(szam)
print('A lista tartalma : ', lista)
szam2 = int(input('adj meg egy számot: '))
szamlalo2 = 0
for i in lista:
    if i == szam2:
        print (lista[1])
print('Módosított lista: ', lista)    