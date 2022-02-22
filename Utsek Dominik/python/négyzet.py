class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4 
    def terulet(self):
        return self.oldalhossz * self.oldalhossz
    def info(self):
        print(f'A(z) {self.oldalhossz} oldalhosszúságu négyzet területe = {self.terulet()} égység, kerülete {self.kerulet()} egység. ')      
negyzet01 = Negyzet(10)
print(negyzet01.info())



