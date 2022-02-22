import random
szamlista = []
szam2 =int(input("Adj meg egy számot! "))
for i in range(5):
    szam = random.randint(1,7)
    szamlista.append(szam)
print(szamlista)
talalat = False
index = 0
while index < 6 and not talalat:
    if szam2 == szamlista[index]:
        talalat = True
    index = index + 1
if talalat:
    print("van találat!")
else:
    print("Nincs találat!")    