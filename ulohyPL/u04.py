# === Úloha 4===
# Napíšte program, ktorý náhodne vygeneruje a vypíše postupnosť 50 celých čísel z intervalu
# <-7000, 7000>, potom vypíše všetky záporné čísla z postupnosti na obrazovku a do textového súboru d:\maturita\zaporne.txt.

# https://stackoverflow.com/questions/11479392/what-does-a-for-loop-within-a-list-do-in-python
# -> buď cez for vnútri zoznamu ([? for i in range(0, 10)]), alebo cez for a append do listu

from random import randint

f = open("zaporne.txt", "w")
l = [ randint(-7000, 7000) for i in range(50) ]

print("Nahodne:")
for c in l:
  print(c, end=" ")
print()

print("Zaporne z nich:")
for c in l:
  if c < 0:
    print(c, end=" ")
    f.write(f"{c}\n")
print()

