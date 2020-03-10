# === Úloha 13===
# Napíšte program, ktorý zašifruje užívateľom zadanú správu tak, že všetky písmená zmení na veľké a za každý znak pôvodnej správy sa vloží náhodne vygenerované veľké písmeno. Zašifrovanú správu vypíše.

# -> pozor vkladame nahodne pismeno ZA kazdy znak
from random import randint

sprava = input("Zadajte spravu: ").upper()

sifra = ""
for z in sprava:
  # najprv znak, potom random pismeno
  sifra += z + chr( randint(ord('A'), ord('Z')) )

print(f"Sifra: {sifra}")