# === Úloha 20===
# Napíšte program, ktorý vygeneruje  postupnosť N slov náhodnej dĺžky nie dlhších ako 20 znakov a vypíše ich postupne pod seba a tiež v opačnom poradí ako boli generované. Na generovanie slov vytvorte funkciu.
from random import randint

def gen_slova(N):
  znak = lambda: chr(randint(ord('a'), ord('z')))
  slovo = lambda: "".join([ znak() for i in range(1, randint(1, 21)) ])
  return [ slovo() for i in range(0, N) ]

print("Normal:")
slova = gen_slova(3)
for s in slova:
  print(s)

print("Naopak:")
for s in reversed(slova):
  print(s)