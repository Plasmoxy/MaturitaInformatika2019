# === Úloha 19===
# Napíšte program, ktorý od používateľa načíta malé písmeno a vypíše na obrazovku a do textového súboru D:\maturita\pismenka.txt trojuholník z písmen. Napr. pre vstup d
# a
# bb
# ccc
# dddd
# Posledný riadok je vytvorený zo zadaného písmena.

p = input("Zadajte pismeno: ")[0]
A = ord('a')
P = ord(p)
n = P - A + 1

for i in range(0, n):
  print( (i+1)*chr(A+i) )