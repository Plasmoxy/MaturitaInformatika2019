# === Úloha 28===
# Napíšte program, ktorý vygeneruje rastúcu postupnosti 100 reálnych čísel tak, že rozdiel každých dvoch susedných prvkov bude najviac dva. Vygenerované prvky postupnosti vypíše a potom užívateľom zadané reálne číslo vloží na správne miesto podľa  veľkosti do vygenerovanej postupnosti. Program vypíše postupnosti pred aj po vložení zadaného čísla.

from random import randint

l = []
x = 0
for i in range(100):
  x += randint(1, 2) # bud prida jednotku alebo dvojku
  l.append(x)
print(l)

s = int(input("Zadajte cislo ktore sa ma vlozit: "))
l = sorted(l + [s]) # co ja som stroj ze to mam checkovat ?? sam sobi posortuj ;)°)°);))°)
print(f"Po vlozeni: {l}")