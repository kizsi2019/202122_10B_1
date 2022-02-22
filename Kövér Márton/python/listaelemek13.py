eredeti = ["alma", "körte", "barack", "szi"]
eredmeny = [x.upper() for x in eredeti if len(x) > 3]
print("Eredeti lista: ", eredeti)
print("Eredmény lista: ", eredmeny)
