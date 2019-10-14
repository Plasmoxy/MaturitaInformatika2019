"""
ciferny sucet

ALGORITMUS -> delim vzdy 10timi a pripocitavam zvysky (postupne sa aplikuje delenie 10, 100, 1000, ... )
= 2 muchy jednou ranou

b) bez //, / a %
"""

vstup = int(input("Zadajte cislo: "))

c = vstup
s = 0
zvysok = 0

while c >= 10:
    # c / 10 = c_vysledok zv. c_zvyskove
    zvysok = c # nastav zaciatocny zvysok na c
    c = 0 # vysledok bude c, zaroven zostane na dalsiu iteraciu
    while zvysok >= 10:
        zvysok -= 10
        c += 1
    
    s += zvysok # pripocitaj zvysok
s += c # pripocitaj c (je mensie ako 10) -> cifry na mieste jednotiek
print(f"Sucet cifier cisla {vstup} je {s}")

