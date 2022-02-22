import random

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    

    def kerulet(self):
        return self.oldalhossz*4

    def terulet(self):
        return self.oldalhossz * self.oldalhossz

    def info(self):
        print(f'A(z) {self.oldalhossz} oldalhosszúságú négyzet területe: {self.terulet():.2f} és a kerülete: {self.kerulet():.2f}')
negyzetek=[]

hossz = int(input("Add meg a négyzet hosszát!"))
while hossz !=0:
    negyzet = Negyzet(hossz)
    negyzetek.append(negyzet)
    hossz = int(input("Add meg a négyzet hosszát!"))
    for i in range(len(negyzetek)):
        print(negyzet.info())

