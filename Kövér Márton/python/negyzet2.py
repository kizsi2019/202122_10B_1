class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4
    def terulet(self):
        return self.oldalhossz * self.oldalhossz
    def info(self):
        print(f'A(z) {self.oldalhossz} oldalhosszúságú, négyzet területe = {self.terulet()}, és kerülete = {self.kerulet()} egység.')
negyzetek =[]
hossz = int(input("Add meg a negyzet hosszát! "))
while hossz != 0:
    negyzet = Negyzet(hossz)
    negyzetek.append(negyzet)
    hossz = int(input("Add meg a negyzet hosszát! "))
for i in range(len(negyzetek)):
    print(negyzet.info())