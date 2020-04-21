# === Úloha 26===
# Napíšte program, ktorý vygenerujte všetky päťciferné palindromy (t. j. čísla, ktoré majú cifru na miesta desaťtisícok rovnakú ako na mieste jednotiek a cifru na mieste tisícok rovnakú ako na mieste desiatok napr. 52125 ) a zapíše ich do textového súboru D:\maturita\palindr.txt, každý na jeden riadok.

for c in [x + x[1] + x[0] for x in [str(i) for i in range(100, 1000)]]:
  print(c)