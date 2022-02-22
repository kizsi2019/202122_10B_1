import random

class negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    

    def kerulet(self):
        return self.oldalhossz*4

    def terulet(self):
        return self.oldalhossz * self.oldalhossz

    def info(self):
        print(f'A(z) {self.oldalhossz} oldalhosszúságú négyzet területe: {self.terulet():.2f} és a kerülete: {self.kerulet():.2f}')

negyzet01 = negyzet(20)
print(negyzet01.info())