paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']
darab = 0
szin = input('Adj meg egy színt!\t')
for i in paletta:
    if i == szin:
	    print('A megadott szín szerepel a listában.')
    darab = darab + 1
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
print("Ennyiszer szerepel: ", darab)