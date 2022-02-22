szam = input('Adj meg egy számot')
szamlista = []
while szam !='':
    
    szamlista.append(szam)
    szam = input('Adj meg egy számot')
    print(szamlista)

    min = szamlista[0]
    max = szamlista[0]

    for elem in szamlista:

	      if elem < min:
		        min = elem
	      if elem > max:
		        max = elem
    print('A legkisebb szám a listában: ', min)
    print('A legnagyobb szám a listában: ', max)