# === Úloha 8===
# Napíšte program, ktorý vygeneruje reťazec náhodných znakov dĺžky väčšej ako 50 znakov a zistí počet výskytov písmena zadaného užívateľom vo vygenerovanom reťazci.

from random import randint

zoznam_znakov = [chr( randint(ord('a'), ord('z')) ) for i in range(0, 51)]
slovo = "".join(zoznam_znakov)

# z inputu vyjde string, ktorý sa správa rovnako ako array
# teda z neho môžem vytiahnuť prvý znak cez [0]
znak = input("Zadajte znak ktory chcete hladat: ")[0]
n = 0

for z in slovo:
  if z == znak:
    n += 1


print(f"slovo: {slovo}")
print(f"Znak '{znak}' sa v slove nachádza {n}-krát.")