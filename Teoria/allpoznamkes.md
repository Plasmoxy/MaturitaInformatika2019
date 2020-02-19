
# Siete
- IP adresa = 4 miestne cislo, identifikator pocitaca v sieti, 255.255.255.255 max
    - 255.255.255.0 = Cčková sieť
    - 255.255.0.0 = B-čková sieť
    - sú aj iné masky keď sa delí sieť na podsiete
    - maska rozdeľuje IP adresu tak, že prvá časť je číslo siete a druhá časť číslo počítača

- MAC adresa = hardvérová adresa sieťovej karty zariadenia v sieti (wifi modul, ethernet karta)
    - napr 34:00:6e:b1:08:aa
    - prve 3 cisla = výrobca, druhe 3 cislo karty u výrobcu
- switch je zariadenie ktoré prepája počítače pričom používa na prepájanie MAC adresy
- stromová sieť: viacero switchov poprepájaných
- zbernicová sieť: počítače súťažia o zbernicu
    - vŽdy môže používať zbernicu len jeden v danom čase
    - Počítače súťažia medzi sebou = Ethernet
    - náhodne sa vyberie že kto bude mať v danom intervale zbernicu
    - príklad Ethernet
    
- kruhová sieť: 
    - typ kruhovej siete: **Token ring** = spôsob prístupu k prenosovému médiu
         - kto má token, môže vysielať

