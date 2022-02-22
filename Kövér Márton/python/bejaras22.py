szavak = ['ajtó','tojás','Ottó','Tamás','tép','Tesla','alma','python']
A_betusok = []
for szo in szavak:
    if szo[0] == "a" or szo[0] == "A":
        #print(szo)
        A_betusok.append(szo)
print("A betűsök: ", A_betusok)