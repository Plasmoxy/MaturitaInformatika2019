# === Úloha 9===
# Napíšte program, ktorý načíta od užívateľa koeficienty kvadratickej rovnice, napíše kvadratickú rovnicu na obrazovku a tiež do textového súboru D:\maturita\kvadrat.txt,
# určí jej korene v R a zapíše ich tiež do uvedeného súboru.
from math import sqrt

# vstup
print("Zadajte koeficienty kvadratickej rovnice: ")
print("( ax^2 + bx + c = 0 )")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# nastavime si textove premenne ktore potom budem vypisovat do
# konzoly ale aj do suboru
text_rovnice = f"{a}*x^2 + {b}*x + {c} = 0"
text_riesenia = ""

# diskriminant
D = b**2 - 4*a*c

# identifikujeme možné riešenia podľa diskriminantu
if D < 0: # ziadne korene
  text_riesenia = "Rovnica nema riesenie v R."
elif D == 0: # jeden koren
  x = -b / 2*a
  text_riesenia = f"x = {x}"
else: # dva korene (D musi byt teraz urcite vacsie ako 0 ked neni 0 a neni mensie ako 0, preto staci else a netreba elif)
  x1 = ( -b + sqrt(D) ) / 2*a
  x2 = ( -b - sqrt(D) ) / 2*a
  text_riesenia = f"x1 = {x1}\nx2 = {x2}"

# na obrazovku vypis
print(f"Rovnica: {text_rovnice}")
print(text_riesenia)

# a nakoniec vypiseme do suboru
f = open("kvadrat.txt", "w")
f.write(f"Rovnica: {text_rovnice}\n{text_riesenia}")
f.close()