import random

rezultat = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

redovi = 4
kolone = 3
rezultat = [[0 for x in range(kolone)] for x in range(redovi)]

for i in range(redovi):
    for j in range(kolone):
        import random

        broj = random.getrandbits(8)
        if broj % 2 == 0:
           broj = broj + 1

        rezultat[i][j] = broj

print(rezultat)
