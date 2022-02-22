lista =[1, 3, 5, 9]
def paros_e(lista):
    for i in lista:
        if i % 2 == 0:
            return True
        else:
            return False
print(paros_e(lista))