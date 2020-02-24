# === Úloha 10===
# Chystáte sa na výlet. Poznáte nosnosť batoha a postupne doň ukladáte veci, ktorých hmotnosť tiež poznáte. Zistite, koľko vecí sa vám zmestí do batoha. Napíšte program, ktorý od používateľa načíta hmotnosť batoha, a hmotnosť jednotlivých vecí. Posledná zadaná hmotnosť je 0. Program skončí po načítaní všetkých hodnôt alebo ak je už prekročená nosnosť batoha. Nakoniec vypíše, koľko vecí si so sebou beriete.

# Poznamka od Seba: nebojte sa program zredukovať, ja sa ho snažím robiť čo najviac perfektným ale bude stačiť aj základná funkcionalita

print("Vitajce u nas, dnes vam vypocitame ze ci sa vam vojdu veci do batoha.")

nosnost = float(input("Zadajte nosnost batoha (v kg): "))

# poznámka: tieto personalizacne spravy tu nemusite pisat uprimne
# staci ze viete jak ten program funguje
print("Teraz zadavajte hmotnost jedlotlivych veci - teda napiste hmotnost v kg a stlacte enter.")
print("Pre ukoncenie zadavania zadajte 0.")
print("Ak prekrocite nosnost batoha, zadavanie sa ukonci tiez.")

# zadefinujem premenne
suma = 0 # suma vsetkych hmotnosti veci
i = 0 # pocitadlo veci

while True:
  h = float(input(f"Hmotnost {i+1}. veci (zostava vam {(nosnost - suma):0.2f} kg) -> "))

  # zistim najprv ci netreba ukoncit zadavanie
  if h == 0: # ukoncene vyhladavanie
    break 
  elif suma + h > nosnost: # ak by sme prekrocili nosnost
    print("Prekrocili ste nosnost batoha !!!")
    break

  # ak teda vec naozaj beriem,
  suma += h # pridam jej hmotnost do sumy hmotnosti
  i += 1 # pripocitam pocitadlo bo som pridal novu vec


print(f"Na výlet beriete spolu {i} veci.")