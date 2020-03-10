# === Úloha 4===
# Napíšte program, ktorý (náhodne) vygeneruje a vypíše postupnosť 50 celých čísel z intervalu
# <-7000, 7000>, potom vypíše všetky záporné čísla z postupnosti na obrazovku a do textového súboru d:\maturita\zaporne.txt.

from random import randint

f = open("zaporne.txt", "w")
l = [randint(-7000, 7000) for i in range(50)]

for c in l:
    if c < 0:
        print(c)
        f.write(f"{c}\n")
