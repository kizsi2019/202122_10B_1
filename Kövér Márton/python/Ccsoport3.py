szam = int(input("Adj meg egy számot -5 és 5 között!"))
szamlista = []
while -5 < szam < 5:
    szamlista.append(szam)
    szam = int(input("Adj meg egy számot -5 és 5 között!"))
print(szamlista)
össeózeg = 0
for elem in szamlista:
    összeg = összeg + elem
print("A lista összege", összeg )