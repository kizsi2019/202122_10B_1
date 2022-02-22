lista = []
szam = int(input("Adj meg egy pozítív számot! "))
while szam >=0:
    lista.append
    szam = int(input("Adj meg egy pozítív számot! "))
print(lista)
def legkisebb(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min
print("A lista legkisebb eleme: ",legkisebb(lista))
