szo = 'krucifiksz'
betu2 = input("Adj meg egy betűt!")
talalat = False
index = 0

while index < len(szo) and not talalat:
    if szo[index] == betu2:
        talalat = True
        index = index + 1
if talalat:
    print("Van ilyen betű a listában!")
else:
    print("Nincs ilyen betű a listában!")