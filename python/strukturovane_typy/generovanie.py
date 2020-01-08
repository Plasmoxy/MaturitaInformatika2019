"""
zrob rastucu postupnost cisel
na vstupe zada cislo uzivatel
program vlozi to cislo do vygenerovanej rastucej postupnosti na taku poziciu, aby postupnost bola tiez rastuca
cez polenie intervalov vyriesit!
"""
from random import randint

def rastuca(n):
    j = [randint(0, 5)]
    for i in range(1, n):
        j += [ j[i-1] + randint(1, 5) ]
    return j

print(rastuca(10))