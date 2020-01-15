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

    print(f"x = {x}")

    while ib-ia > 2:
        mid = int((ib+ia)/2)

        # ak pridame nieco velke, returnni priamo
        if x >= l[-1]:
            l.append(x)
            return

        if l[mid] < x:
            ia = mid
        else:
            ib = mid
        
    # teraz mam 2 hodnoty vedla seba
    if l[ia] == x:
        l.insert(ia+1, x)
    elif l[ib] == x:
        l.insert(ib+1, x)

l = rastuca(5)
print(f"l = {l}")

vloz_aby_bola_rastuca(14, l)
print(f"po vlozeni: {l}")