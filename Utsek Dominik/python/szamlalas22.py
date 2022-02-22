szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal',]
darab = 0
for szo in szavak:
    if szo[0] == "A" or szo[0] == "a":
        print(szo)
        darab += 1
print("Ennyi a tebűvel kedődő szó van: ",darab)