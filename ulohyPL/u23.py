# === Úloha 23===
# Vytvorte program, ktorý sa bude používať na vyhodnotenie IQ testu žiakov v triede. Zistí priemerné IQ žiakov v triede a vypíše početnosti podľa IQ pre intervaly menej ako 90, 90-110, 110-130, viac ako 130. Počet žiakov v triede nie je vopred určený.

iqziakov = [90, 130, 24, 150, 152, 122, 100]
kateg = [0]*4

avg = sum(iqziakov)/len(iqziakov)

for iq in iqziakov:
  if iq < 90: kateg[0] += 1
  elif iq >= 90 and iq < 110: kateg[1] += 1
  elif iq >= 110 and iq <= 130: kateg[2] += 1
  elif iq > 130: kateg[3] += 1

print(f"< 90: {kateg[0]}") # 1
print(f"90-110: {kateg[1]}") # 2
print(f"110-130: {kateg[2]}") # 2
print(f"> 130: {kateg[3]}") # 2