# === Úloha 6===
# Napíšte program, ktorý vypíše na obrazovku tabuľku malej násobilky od 1 po číslo, ktoré zadá užívateľ.
# Pr. pre vstup 3:    	1	2	3
# 1	1	2	3
# 2	2	4	6
# 3	3	6	9

c = int(input("Zadajte cislo: "))

for y in range(1, c+1):
  for x in range(1, c+1):
    print(f"{x*y:3}", end="")
  print()
