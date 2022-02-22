import random
szamlista = []
for i in range(5):
    szam = random.randint(1,10)
    szamlista.append(szam)
print(szamlista)
összeg = 0
for elem in szamlista: 
    összeg = összeg + elem
print("A lista összege:", összeg)