szam = input("Adj meg egy számot: ")
szamlista = []
while szam !='':
    szamlista.append(szam)
    szam = input("Adj meg egy számot: ")
print(szamlista)
max = szamlista[0]
min = szamlista[0]
for elem in szamlista:
    if elem > max:
        max = elem
    if elem < min:
        min = elem
print("A legkissebb szám: ", min)
print("A legnagyobb szám: ", max)