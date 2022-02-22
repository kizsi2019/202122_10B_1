# egysoros komment
'''
több soros
komment
'''
"""
def inputStr(szoveg):
    return input(szoveg)


nev=input('Add meg a neved: ')
# print(nev)
kor=input('Add meg a korod: ')
# print(kor)

print(nev+" kora "+kor)
print(nev+ " jövőre " + str((int(kor)+1)))

labmeret=inputStr("Add meg a lábméreted: ")
print(labmeret)

def osszead(a,b):
    return a+b
"""
'''
def osztas(a, b):
    return int(a/b);

#print(osszead(3,4))
a= 4
b= 3
print(osztas(a,b))
print('A '+ str(a) + ' osztva '+
        str(b)+'-vel: '+str(osztas(a,b)))

'''

import random
n = random.random() # (0,1)
# feladat: 1től 10ig számkitalálós játék
randomszam=int(n*10)+1 #1-10
print(str(randomszam))
print("Gondoltam egy számra!")

eltalatad=False
while (eltalatad != True):
    felhaszszam= int(input("Adj meg egy számot: "))
    if felhaszszam<randomszam:
        print("a szám kisebb ennnél")
    elif felhaszszam>randomszam:
        print("a szám nagyobb ennnél")
    else:
        print("Eltaláltad! gratulálok!")
        eltalatad=True

