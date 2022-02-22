import random
grafika = ['''
 
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
szavak = ('programozás akasztófa ciklus értékadás változó algoritmus elágazás objektum rekurzió függvény szótár szintaxis kaparóssorsjegy kereszt takaró ajtó macska kutya kenyér játék').split()
 
def szovalasztas(szavakListaja):    
    szoSorszam = random.randint(0, len(szavakListaja) - 1)
    return szavakListaja[szoSorszam]
 
def megjelenites(grafika, rontottBetuk, eltalaltBetuk, titkosSzo):
    print(grafika[len(rontottBetuk)])
    print()
 
    print('Elrontott betűk:', end=' ')
    for betu in rontottBetuk:
         print(betu, end=' ')
    print()
  
    ismeretlen = '_' * len(titkosSzo)
 
    for i in range(len(titkosSzo)):
         if titkosSzo[i] in eltalaltBetuk:
             ismeretlen = ismeretlen[:i] + titkosSzo[i] + ismeretlen[i+1:]
 
    for betu in ismeretlen:
        print(betu, end=' ')
    print()
 
def tippeles(voltMarTipp):    
     while True:
         print('Válassz egy betűt!')
         tipp = input()
         tipp = tipp.lower()
         if len(tipp) != 1:
                print('Csak egyjegyű betűket választhatsz!')
         elif tipp in voltMarTipp:
                print('Ezt már tippelted egyszer! Tippelj újra!')
         elif tipp not in 'aábcdeéfghijklmnoóöpqrstuúüvwxyz':
                print('Betűt adj meg!')
         else:
            return tipp
def ujJatek():    
    print('Szeretnél egy új játékot? (i/n)')
    return input().lower().startswith('i')


print('A K A S Z T Ó F A')
rontottBetuk = ''
eltalaltBetuk = ''
titkosSzo = szovalasztas(szavak)
vegeVan = False

while True:
    megjelenites(grafika, rontottBetuk, eltalaltBetuk, titkosSzo)
   
    tipp = tippeles(rontottBetuk + eltalaltBetuk)

    if tipp in titkosSzo:
        eltalaltBetuk = eltalaltBetuk + tipp
      
        mindenBetuEltalalva = True
        for i in range(len(titkosSzo)):
          if titkosSzo[i] not in eltalaltBetuk:
               mindenBetuEltalalva = False
                    
        if mindenBetuEltalalva:
            print('Gratulálok! Sikerült eltalálnod a titkos szót: "' + titkosSzo + '". Nyertél!')
            vegeVan = True
    else:
       rontottBetuk = rontottBetuk + tipp
       
       if len(rontottBetuk) == len(grafika) - 1:
           megjelenites(grafika, rontottBetuk, eltalaltBetuk, titkosSzo)
           print('Nincs több tippelési lehetőséged!\n' + str(len(rontottBetuk)) + ' rossz tipp és ' + str(len(eltalaltBetuk)) + ' jó tipp, a titkos szó: "' + titkosSzo + '"')      
           vegeVan = True    
    if vegeVan:
        if ujJatek():
            rontottBetuk = ''
            eltalaltBetuk = ''
            vegeVan = False
            titkosSzo = szovalasztas(szavak)
        else:
            break