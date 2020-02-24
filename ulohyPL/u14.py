# === Úloha 14===
# Napíšte program, ktorý vytvorí z textového súboru basen.txt súbor kopia.txt tak, že nahradí všetky prázdne riadky v súbore basen.txt reklamným sloganom zadaným  používateľom. Program vypíše aj informáciu o počte počet riadkov vzniknutého súboru.

basen = open("basen.txt", "r")
kopia = open("kopia.txt", "w")

slogan = input("Zadajte slogan: ")

while True:
  l = basen.readline()

  # narazili sme na koniec
  if len(l) == 0:
    break

  # ak je prazdny riadok
  if l.strip() == "":
    kopia.write(slogan + "\n")
  else:
    kopia.write(l)

basen.close()
kopia.close()