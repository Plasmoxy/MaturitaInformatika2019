# === Úloha 18===
# Napíšte program, ktorý vygeneruje  a vypíše  postupnosť  N  náhodne vygenerovaných celých čísel  z intervalu <-10000,10000>, N >1000. Následne z postupnosti vygenerovaných čísel vypíše  všetky čísla deliteľné číslom  3 a súčasne číslom 2 a tiež zistí aj ich počet.

from random import randint
N = 10

l = [ randint(-10000, 10000) for i in range(0, N) ]
delitelne3a2 = list(filter( lambda x: x % 2 == 0 and x % 3 == 0, l ))
print(f"Delitelne 3 a 2: {delitelne3a2}")
print(f"Pocet = {len(delitelne3a2)}")