# === Úloha 15===
# Napíšte program, ktorý vygeneruje neutriedenú postupnosť reálnych čísel, vypíše ich a vypíše ich usporiadané od najmenšieho po najväčšie.

from random import randint

l = [ randint(-5, 10) for i in range(10) ]
print(f"predtym: {l}")

# funkcia sorted toto riesi perfektne
sl = sorted(l)
print(f"pomocou funkcie sorted: {sl}")


# AVŠAK zrejme bude treba implementovať bez sorted
# nie je napisane presne aky algoritmus treba, bude stacit ist podla minima

# ziska index najmensieho cisla v rozsahu
def minimum_i(zoznam, a, b):
  mi = a # nastavim na prvy prvok
  for i in range(a, b):
    if zoznam[i] < zoznam[mi]:
      mi = i
  return mi

ia = 0
ib = len(l) - 1



# -> alebo jednoduchsie cez l.index(min(l))

print(minimum_i(l))