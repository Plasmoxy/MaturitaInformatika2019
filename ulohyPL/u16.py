# === Úloha 16===
# Napíšte program, ktorý vygeneruje postupnosť 100 celých čísel, vypíše ich na obrazovku a následne vypíše najprv párne kladné čísla a ich počet a potom nepárne kladné čísla a ich počet.

from random import randint

l = sorted([ randint(-100, 100) for i in range(0, 100) ])
parne = list(filter(lambda x: x % 2 == 0, l))
neparne = list(filter(lambda x: x % 2 != 0, l))

print(f"Postupnost: {len(l)}")
print(f"Párne ({len(parne)})\n{parne}")
print(f"Nepárne ({len(neparne)})\n{neparne}")