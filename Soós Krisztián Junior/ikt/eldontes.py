import random 
szamlista = []
for i in range(5):
    szam = random.randint(1,7)
    szamlista.append(szam)
    szam2 = int(input("Adj meg egy számot!"))
    
    print(szamlista)
    
    talalat = False
    index = 0
    
    while index < len(szamlista) and not talalat:
        if szamlista[index] == szam2:
           talalat = True
           
        index = index + 1
        
    if talalat:
        print("Van ilyen szám a listában")
        
    else:
        print("Nincs ilyen szám a listában")