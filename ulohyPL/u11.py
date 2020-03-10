# === Úloha 11===
# Nech N je prirodzené číslo z intervalu <1,65500>.  Napíšte program, ktorý vypíše cifry prislúchajúce číslu N po prevode do dvojkovej sústavy.

from random import randint

x = randint(1, 65500)

# najlahsi sposob by to bolo cez formatovaci string
print(f"Cifry cisla {x} v binarnej sustave pomocou formatovania: {x:b}")

# => lenze neviem ci formatovanie nebude zakazane takze da sa to
# zrobit velmi jednoducho pomocou delenia 2kou
# 1. zoberiem cislo, vydelim 2kou => zvysok zapisem ako cifru
# 2. zoberiem ten podiel, zasa videlim 2kou => zvysok zapisem ako cofiru nalavo od predchadzajucej cifry
# 3. opakujem az kym mi podiel nezostane 0

cifry = "" # string !!!
while x > 0:
  zv = x % 2 # zvysok po deleni 2 bude vzdy 0 alebo 1
  cifry = str(zv) + cifry # string zvysku pridam NALAVO!
  x = x // 2 # predelim x CELOCISELNE 2kou

print(f"Cifry pomocou delenia: {cifry}")

# Poznamka: taketo konvertovanie cifier sa da pouzit na hocijaku ciselnu sustavu
# (pri 3-kovej sustave by sme vyuzivali miesto 2-ky 3-ku)