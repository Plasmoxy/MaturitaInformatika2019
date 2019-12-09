from random import randint

nahodny_zoznam = lambda n, a, b: [randint(a,b) for i in range(0, n)]

print(nahodny_zoznam(20, 1, 1000))