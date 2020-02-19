
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

- **Deleni podľa topologie**

    - stromová sieť: viacero switchov poprepájaných
    - zbernicová sieť: počítače súťažia o zbernicu
        - vŽdy môže používať zbernicu len jeden v danom čase
        - Počítače súťažia medzi sebou = Ethernet
        - náhodne sa vyberie že kto bude mať v danom intervale zbernicu
        - príklad Ethernet
        
    - kruhová sieť: 
        - typ kruhovej siete: **Token ring** = spôsob prístupu k prenosovému médiu
            - kto má token, môže vysielať

- delenie podľa vzdialenosti: LAN, MAN, WAN
- router
    - = zariadenie, ktoré prepája rôzne siete fungujúce na protokole IP
    - prebera udaje z jednej siete (napr. lokálnej siete) a posiela ich na rôzne ciele v nadradenej sieti
    - môže obsahovať bezpečnostné mechanizmy chrániace vnútorné zariadenia siete pred nechcenými prienikmi z vonkajších sietí = firewall
- paketová komunikácia: dáta v sieťach sa prenášajú tak že sa rozdelia na menšie časti - pakety
- paket:
    - hlavička a telo
    - v hlavičke je poradové číslo paketu, zdrojová a cieľová adresa, checksum - overuje integritu dát
    - každý paket môže byť doručený do cieľa inou cestou a v rôznom poradí
- gateway (brána):
    - zvyčajne router, ktorý slúži ako prístupový bod pre počítač do internetu, resp. do inej siete
    - treba IP adresu gateway, aby každý pc v sieti vedel, kde má posielať pakety ak chce ísť do internetu
    - je to brána do inej siete

- rozdelenie IP adreis:
     - verejné - viditeľné v internete
     - lokálne - len pre počítače v sieti
    
- ručné nastavenie parametrov pre sieťovú kartu:
    - Nastavenie siete a internetu
    - Ethernet
    - Sieť -> nastavenie adaptéra
    - IP adresy - IP, maska, brána
    - DNS - DNS servery - domain name system - systém doménových mien
    - prideľovanie mien ku ip adrese
    - DNS server - má tabuľky mien a IP adries
    