szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

print(len(szavak[0]))
darab = 0
for szo in szavak:
    for betu in szo:
        if betu == "E" or betu == "e":

            darab =+1
            
print("ennyi darab e betűt tartalmazó szó van!: " ,darab)