# === Úloha 16===
# Napíšte program, ktorý vygeneruje postupnosť 100 celých čísel, vypíše ich na obrazovku a následne vypíše najprv párne kladné čísla a ich počet a potom nepárne kladné čísla a ich počet.

from random import randint

l = [ randint(-100, 100) for i in range(0, 100) ]
print(f"Postupnost: {l}")

print("Párne: ")
for c in l:
  if c % 2 == 0:
    print(c, end=", ")
print()

print("Nepárne: ")
for c in l:
  if c % 2 != 0:
    print(c, end=", ")
print()
