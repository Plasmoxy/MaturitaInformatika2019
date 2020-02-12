# === Úloha 1===
# Napíšte program, ktorý vypočíta súčin, celočíselný podiel a zvyšok pri delení dvoch náhodne vygenerovaných prirodzených čísel bez použitia operácií *, div a mod.

from random import randint

a = randint(1, 100)
b = randint(1, 100)

sucin = 0
for i in range(a):
  sucin += b

zv = a
podiel = 0
while zv >= b:
  zv -= b
  podiel += 1


print(f"{a}*{b} = {sucin}")
print(f"{a}/{b} = {podiel} zv {zv}")