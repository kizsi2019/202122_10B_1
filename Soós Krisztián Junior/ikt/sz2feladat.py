szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
for szo in szavak:

    if szo[0] == "A" or szo[0] == "a":

        print(szo)

        darabka = 0

for szo in szavak:
        if szo[0] == "A" or szo[0] == "a":
             darabka = darabka +1
print("Ennyi a betűvel kezdődő szó van:",darabka)