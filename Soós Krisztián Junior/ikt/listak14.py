import random

list = []

szamlalo = 1

while szamlalo <=10:
    szam = random.randint(0,50)
if szam % 4 == 0:
    list.append(szam)
    
    szamlalo = szamlalo +1
    
    print(" A lista elemei: ", list)
    print(" A lista hossza: ", len(list))