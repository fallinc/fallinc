import random

niz_rijeci = ['reaktor', 'rukomet', 'programiranje', 'lista', 'radijator', 'linijar']
rijec = random.choice(niz_rijeci)
rez = []
counter = 0

for i in rijec:
    rez.append('-')

zivoti = 5
pogodio = len(rijec)

while zivoti > 0 and pogodio > 0:
    ges = input('Pogadjaj slovo: ')

    if len(ges) > 1:
        print('Unijeli ste vise slova. Program prihvata samo jedno slovo.')

    elif len(ges) == 0:
        print('Unesite neko slovo.')

    elif rez.count(ges) > 0:
        print('Vec ste poskusali sa slovom', ges)
        print('------------------------------------------------------------')

    else:
        pogodio -= rijec.count(ges)

        if (rijec.count(ges)) > 0:
            while counter < len(rijec):
                if rijec[counter] == ges:
                    rez[counter] = rijec[counter]
                counter += 1
            counter = 0
            print('------------------------------------------------------------')
            print('Pogodjeno je slovo: ', ges)
            print(rez)
            print('------------------------------------------------------------')

            if pogodio == 0:
                print('------------------------------------------------------------')
                print('Bravo, pogodjena je trazena rijec!')

        else:

            zivoti -= 1
            print('Slovo ' + ges + ' nije u trazenoj rijeci.')
            print('Ostalo je jos ', zivoti, ' pokusaja')
            print(rez)
            print('------------------------------------------------------------')

            if zivoti == 0:

                print('------------------------------------------------------------')
                print("Iskoristili ste sve pokusaje.")
                print('Trazena je rijec: ' + rijec)
                print('')