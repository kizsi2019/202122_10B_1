import random

dobas = random.randint(1,2)
szam = input("Fej vagy írás (fej-1/iras-2)")
if dobas == szam:
    print("Eltaláltad!")
else:
    print("Nem találtad el!")