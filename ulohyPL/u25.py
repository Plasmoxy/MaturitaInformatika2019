# === Úloha 25===
# Napíšte program, ktorý z intervalu <1, N> vypíše prvočísla. Na overenie toho, či číslo je prvočíslo, vytvorte funkciu s jedným parametrom.
N = 20

def je_prvocislo(x):
  for i in range(2, x): # <2, x)
    if x % i == 0:
      return False
  return True # je prvocislo len ak neni delitelne nicim inym nez len 1 a x

for i in range(2, N+1): # 1 neni prvocislo
  if je_prvocislo(i):
    print(i)