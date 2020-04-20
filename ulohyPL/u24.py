# === Úloha 24===
# Napíšte program, ktorý zistí koľko je v súbore vzor.txt riadkov aj znakov a taktiež  určí počet znakov v najdlhšom riadku.
from functools import reduce

with open("text.txt", "r") as f:
  t = f.readlines()
najdlh = max(list(map(lambda riadok: len(riadok), t)))
znakov = reduce(lambda a, x: a + len(x), t, 0)
print(f"Pocet riadkov: {len(t)}, pocet znakov: {znakov}")
print(f"Najdlhsi riadok ma {najdlh} znakov.")