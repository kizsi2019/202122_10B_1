import datetime

class Diak:
    felnott_diak = 0
    gyerek_diak =0
    def __init__(self, szuletes, osztaly, nev):

        self.szuletes = szuletes
        self.osztaly = osztaly
        self.nev = nev
        if szuletes > 18:
            type(self).felnott_diak +=1
        else:
            type(self).gyerek_diak +=1
    def eletkor(self):
        return datetime.datetime.now().year - self.szuletes
    def info(self):
        print(f'Szia, {self.nev} vagyok, a {self.osztaly} osztalyba jarok,{self.eletkor()} eves vagyok')

diak_01 = Diak("Kiss Péter","10.A", 2006)
print(diak_01.info())