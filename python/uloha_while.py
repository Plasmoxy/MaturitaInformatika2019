"""
vygeneruj cislo mensie ako 100
uzivatel bude hadat
bez break
"""

from random import randint

num = randint(0, 100)
max_hadania = 10
uhadol = False
pokus = 1

print("Idzeme hadac cislo !")
while not uhadol and pokus <= max_hadania:
    x = int(input("Hadaj cele cislo: "))

    if x < num:
        print("Moje cislo je vacsie ako tvoje!")
    elif x > num:
        print("Moje cislo je mensie ako tvoje!")
    else:
        uhadol = True
    
    pokus += 1

if pokus == max_hadania or not uhadol:
    print("Neuhadol si!")
else:
    print(f"Uhadol si na {pokus}. pokus.")