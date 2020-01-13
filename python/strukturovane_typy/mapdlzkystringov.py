from typing import List
from random import randint
from functools import reduce

# spojenie nahodnych znakov medzi 
genJednoSlovo = lambda nznakov: reduce(lambda a,i: a + i,
    [ chr(randint(ord('a'), ord('z'))) for i in range(0, nznakov) ]
)
genNahodneSlova = lambda n: [ genJednoSlovo(randint(3, 10)) for i in range(0, n) ]
mapToDlzky = lambda l: list(map(lambda x: len(x), l))

sl = genNahodneSlova(10)
sl_dlzky = mapToDlzky(sl)
print(f"Slová: {sl}")
print(f"Dlžky: {sl_dlzky}")
print(f"Najdlhšie slovo: { sl[ sl_dlzky.index( max(sl_dlzky) ) ] }")