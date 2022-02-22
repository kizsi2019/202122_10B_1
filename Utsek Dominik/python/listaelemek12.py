eredeti = ['alma', 'körte', 'barack', 'szilva' ]
eredmeny = [x.upper() for x in eredeti if len(x)>3]
print('Eredeti lista: ', eredeti)
print('Eredmeny lista: ', eredmeny)