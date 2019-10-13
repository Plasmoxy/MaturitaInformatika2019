"""
Sebo robi minecraft server. Na začiatku chce od svojich poddaných zozbierať začiatočné množstvo €, každý ďalší mesiac však bude zbierať stále o 1 € menej.
Keďže je však kokot, každý mesiac pripočítava daň, čo je niekoľko eur.
Napíšte program, do ktorého používateľ zadá počiatočnú platbu a daň, a potom vypíše, koľko € treba jeho poddaným zaplatiť KAŽDÝ mesiac.
Mesiace vypisujte dovtedy, kým platba bez dane nebude 0€.
Používajte iba celé čísla.
Vypíšte  vždy aj číslo mesiaca ( napr "mesiac 1 = 69€" ...)
"""

zaciatocna_cena = int(input("Zadajte pociatocnu platbu v €: "))
dan = int(input("Zadajte Sebovu dan v €: "))

cena_za_mesiac = 1
pocet_mesiacov = int(zaciatocna_cena/cena_za_mesiac)

for mesiac in range(1, pocet_mesiacov):
    platba = zaciatocna_cena - mesiac*cena_za_mesiac + dan
    print("Mesiac ", mesiac, " = ", platba)
