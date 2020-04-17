# === Úloha 17===
# Napíšte program, ktorý bude dešifrovať vetu uloženú v textovom súbore sprava.txt. Veta bola zašifrovaná tak, že za každý znak pôvodnej správy bol vložený náhodne vygenerovaný znak.

# (nacitaj zo suboru ten string cez read)
TEST = "A?h?o?j? ?j?a? ?s?o?m? ?S?e?b?o?.?"

sprava = ""
for i in range(0, len(TEST), 2):
  sprava += TEST[i]

print(sprava)