# === Úloha 30===
# Napíšte program, ktorý zašifruje vetu zadanú užívateľom tak, že znaky v zašifrovanej vete budú posunuté o jeden znak v ASCII tabuľke vpravo. Zašifrovanú vetu vypíše a vypíše ju aj naopak - od posledného znaku k prvému.
# (Príklad: AHOJ sa zašifruje na BIPK)

v = input("Zadajte vetu: ")
s = "".join([ chr(ord(c) + 1) for c in v ])

print(f"Sifra: {s}")
print(f"Sifra naopak: {''.join(reversed(s))}")