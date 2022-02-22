szo = 'almafa'
betu2 =input("Adj meg egy betut")
talalat = False
index = 0
while index < len(szo) and not talalat:
    if szo[index] == betu2:
        talalat = True
        index = index +1
        if talalat:
            print("Van ilyen szám a listában")
        
    else :
        print("Nincs ilyen szám a listában")