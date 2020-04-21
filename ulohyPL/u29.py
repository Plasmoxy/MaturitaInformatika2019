# === Úloha 29===
# Napíšte program, ktorý zašifruje textový súbor vzor.txt tak, že ho rozdelí na dva súbory. Znaky z nepárnych pozícií sa zapíšu do prvého súboru a z párnych pozícií do druhého súboru. Ak by sme jeden z nich vytlačili na priesvitný papier a položili ho na druhý, vytvoria pôvodný dokument.

with open("text.txt", "r") as f:
  text = f.read()

parne = ""
neparne = ""

for i in range(0, len(text)):
  if i%2 == 0: parne += text[i]
  else: neparne += text[i]

with open("text_parne.txt", "w") as f:
  f.write(parne)
with open("text_neparne.txt", "w") as f:
  f.write(neparne)