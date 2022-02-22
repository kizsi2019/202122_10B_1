  # üres listát hoz létre
nevek = []

  # kezdőérték nélküli változót hoz létre
nev = None
while nev != '':
    nev = input('Adj meg egy nevet! ')
    if nev != '':
      # hozzáfűzi a listahoz
      nevek.append(nev)

print(nevek)  