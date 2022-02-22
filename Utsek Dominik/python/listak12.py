# üres listát hoz létre
nevek = []
  
# kezdőérték nélküli változót hoz létre
nev = None
szamlalo = 1
while szamlalo <= 3:
     nev = input('Adj meg egy nevet! ')
     if nev != '':
     # hozzáfűzi a listahoz
      nevek.append(nev)
     szamlalo = szamlalo + 1 
print(nevek)