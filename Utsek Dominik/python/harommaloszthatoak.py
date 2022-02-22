lista = [1, 3, 5, 6, 9, 12, 14]
def harommal_osszhatoak(lista):
    szamalalo = 0
    for i in lista:
        if i % 3 == 0:
            szamalalo += 1 
    return szamalalo

darab = harommal_osszhatoak(lista)
print("Ennyi darab hárommal osztható: ", darab)