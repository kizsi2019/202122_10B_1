lista = [1, 3, 5,6,9,12,14]
def harommal_oszthatok(lista):
    szamlalo = 0
    for i in lista:
        if i % 3 == 0:
            szamlalo = szamlalo +1
    return szamlalo
darab = harommal_oszthatok(lista)
print("Ennyi darab 3-mmal osztható szám van:", darab)        