szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
for szo in szavak:

    if szo[0] == "A" or szo[0] == "a":

        print(szo)

        darab = 0

for szo in szavak:
        if szo[0] == "A" or szo[0] == "a":
             darab = darab +1
print("Ennyi a betűvel kezdődő szó van:",darab)