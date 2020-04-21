# === Úloha 27===
# Naprogramujte hru hádaj číslo. Počítač si vymyslí celé číslo z intervalu 1..100. Hráč zadá číslo, počítač mu vždy poradí, či je hádané číslo menšie alebo väčšie ako zadané. Hra končí, ak hráč háda neúspešne viac ako 10 krát alebo výpisom uhádnutého čísla. Program vypíše všetky nesprávne tipy hráča a počet jeho hádaní.

from random import randint

print("Uhádni číslo!")
c = randint(1, 100)
print(c)
pokusy = []

while True:
  x = int(input("Zadaj číslo: "))
  
  if x == c:
    print("Uhádol si!")
    break
  elif x > c:
    print(f"Hádané číslo je menšie ako {x}")
  else: # x < c
    print(f"Hádané číslo je väčšie ako {x}")
  
  pokusy.append(str(x))

print(f"Tvoje nesprávne pokusy: {', '.join(pokusy)}")
print(f"Počet nesprávnych pokusov: {len(pokusy)}")