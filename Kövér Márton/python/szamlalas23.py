szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

print(len(szavak[0]))
darab = 0
for szo in szavak:
    for betu in szo:
        if betu == "E" or betu == "e":
            darab = darab + 1
print("Ennyi darab e betű van: ", darab)