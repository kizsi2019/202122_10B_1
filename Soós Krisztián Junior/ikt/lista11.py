nevek = []

nev = None
szamlalo = 1
while szamlalo <= 3:
    nev= input('Adj meg egy keresztnevet!')
if nev != '':
    nevek.append(nev)
    
    szamlalo = szamlalo + 1
    
print(nevek)  
