from math import sqrt

"""
Dokonalé číslo je také, ktorého súčet všetky deliteľov okrem neho samého je to samé číslo.

"""

max_n = 10000

# pre vsetky cisla po n
for c in range(1, max_n + 1):

    sum_delitelov = 0

    # zisti sucet delitelov
    for d in range(1, c): # mimo toho cisla samotneho
        if c % d == 0 :
            sum_delitelov += d
    
    if sum_delitelov == c:
        print(c)