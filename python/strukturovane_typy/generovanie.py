"""
zrob rastucu postupnost cisel
na vstupe zada cislo uzivatel
program vlozi to cislo do vygenerovanej rastucej postupnosti na taku poziciu, aby postupnost bola tiez rastuca
cez polenie intervalov vyriesit!
"""
from random import randint
from typing import List

def rastuca(n: int) -> List[int]:
    j = [randint(0, 5)]
    for i in range(1, n):
        j += [ j[i-1] + randint(1, 5) ]
    return j

def vloz_aby_bola_rastuca(x: int, l: List[int]):

    ia = 0
    ib = len(l)

    while True:
        mid = int((ib+ia)/2)

        # napol intervaly a limituj vstup krokoveho algoritmu
        if l[mid] < x:
            ia = mid
        else:
            ib = mid
        
        # diferencia indexov, potom pouzi krokovy algoritmus na ukoncenie
        if ib-ia < 4:
            while l[ia] <= x:
                ia += 1
            l.insert(ia, x)
            return

l = rastuca(10000)
print(f"l = {l}")

vloz_aby_bola_rastuca(5230, l)
print(f"po vlozeni 13: {l}")