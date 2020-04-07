# === Úloha 15===
# Napíšte program, ktorý vygeneruje neutriedenú postupnosť reálnych čísel, vypíše ich a vypíše ich usporiadané od najmenšieho po najväčšie.

from random import randint

l = [ randint(-5, 10) for i in range(10) ]
print(f"predtym: {l}")

# funkcia sorted toto riesi perfektne
sl = sorted(l)
print(f"pomocou funkcie sorted: {sl}")

# AVŠAK zrejme bude treba implementovať bez sorted
# nie je napisane presne aky algoritmus treba, ja zrobim cez bubble sort
# budem postupovat od zaciatku (i=0) po koniec, hodnoty teda budu bublovat tymto smerom

koniec = len(l)-1 # na zaciatku ideme cez cely zoznam, postupne potom znizujeme koniec

while True:
  vymeny = 0 # overujeme pocet vymen

  # nevratane konca, lebo ak sme na koniec-1, tak potom overujeme koniec-1 a koniec (lebo i+1)
  for i in range(0, koniec):
    # ak je i vacsie ako i+1
    if l[i] > l[i+1]:
      l[i], l[i+1] = l[i+1], l[i] # vymen ich (vybublaj)
      vymeny += 1

  if vymeny == 0: 
    break # ak uz nic nebubla, ukonci bublanie
  else:
    koniec -= 1 # toto nie je nevyhnutne; zniz koniec (pretoze vybublala na koniec hodnota a ta uz dalej bublat vyssie nebude)


print(f"Posortovany pomocou bubble sortu: {l}")