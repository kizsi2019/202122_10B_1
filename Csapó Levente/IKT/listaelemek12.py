eredeti = ['alma', 'körte' , 'barack' , 'szilva']
eredmeny = [x.upper() for x in eredeti  if len(x)>3]
print('Erdetei lista:',eredeti)
print('Eredmény lista: ',eredmeny)