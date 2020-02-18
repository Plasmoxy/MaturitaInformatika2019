"""
najdite sedlové body v dvojrozmernom poli
s. bod = najmensi v riadku a najvacsi v stlpci
"""
from typing import List

def sedlove_body(pole: List[List[int]]):
    body: List[List[int]] = []
    # pole[y][x] -> pole[riadok][stlpec]
    # predpokladajme sirku a vysku pola
    len_y = len(pole) 
    len_x = len(pole[0])

    # pre kazdy riadok:
    for i_riadok in range(len_y):

        # pre kazde cislo x (stlpec, y) v tom riadku,
        for i_stlpec in range(len_x):
            x = pole[i_riadok][i_stlpec] # x je hodnota

            #  zistim ci je minimum tohto riadku
            if x == min(pole[i_riadok]):

                # ak hej, zistim ci to cislo je maximum => prejdem cislami stlpca
                # a ak najdem vacsie tak urcite nebude maximum

                je_maximum = True
                for y in range(len_y): # prejdem ostatnymi prvkami v stlpca
                    if pole[y][i_stlpec] > x: # ak najdem vacsie:
                        je_maximum = False # tak to nebude maximum urcite
                        break
                
                if je_maximum:
                    body.append([i_riadok, i_stlpec])
    return body


print_arr = lambda arr: print('\n'.join(str(x) for x in arr))

w = 5
h = 5
arr: List[List[int]] = [
    [1, 0, 4, 8],
    [7, 4, 9, 7],
    [3, 2, 1, 4],
    [20, 5, 10, 7] # v tomto pripade je sedlovy bod iba 5
]
print_arr(arr)
arr_sbody = sedlove_body(arr)
print(f"body = {arr_sbody}")
for b in arr_sbody:
    print(f"bod (y, x) [{b[0]}, {b[1]}] = { arr[ b[0] ][ b[1] ] }")
