# === Úloha 22===
# Napíšte program, ktorý zo súboru zoznam.txt vypíše pod seba meno a vek všetkých žiakov, ktorí majú aspoň 17 rokov. Údaje v súbore zoznam.txt sú zoradené tak, že v každom riadku je postupne vek a meno jedného žiaka.

subor = open("ziaci.txt", "r")
ziaci = list(map(lambda x: x.split(" "), subor.read().split("\n")))
aspon17 = filter(lambda x: int(x[0]) >= 17, ziaci)
subor.close()

for z in aspon17:
  print(f"{z[1]}: {z[0]} rokov")