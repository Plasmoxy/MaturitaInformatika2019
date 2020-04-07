
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
        - Počítače súťažia medzi sebou -> Ethernet = spôsob prístupu ku prenosovému médiu
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

- média pri prenose v sieti:
    - metalické kable
    - optické vlákna
    - elektromagnetické vlnenie

- TLD (top level domain) = doména prvej úrovne = .sk, .cz, .com

- ako získam doménu 2. úrovne?
    - oslovím registrátora
    - registrátor sa pokúsi zaregistrovať túto doménu s poskytovateľom domény

- ked nejde net: checc DNS servery 8.8.8.8 google server, checc ip adresu
- DHCP - Dynamic Host Configuration Protocol
    - protokol na automatické prideľovanie IP adries zariadeniam resp. sieťovým kartám
    - DHCP server = dynamicky priraďuje IP adresy zariadeniam
    - princíp: karta vyšle cez broadcast adresu (255.255.255.255 alebo ipsiete a na konci 255) požiadavku o pridelenie IP adresy 
    - všetky zariadenia v sieti počúvaju na tej broadcast adrese, ak je v sieti DHCP server, tak obslúži požiadavku

- FTP - file transfer protocol
- pop3/imap = emaily
- SMTP - posielanie emailov na email server
- SSH - secure shell - vzdialené pripojenie (šifrované)
- telnet - vzdialené pripojenie



# Hardware
- **technické vybavenie počítača**
- procesor (CPU), matičná doska, grafická karta (GPU), RAM (Random Acces Memory), napájací zdroj, oprická mechanika, HDD, SSD, dalšie rozširujúce karty, myš, klávesnica, monitor, tlačiareň, slúchadlá, reproduktory
- **CPU**
    - mikroprocesor, integrovaný obvod, obsahuje niekoľko desitok miliónov tranzistorov
    - **dve základné časti**
        - riadiaca jednotka
        - aritmeticko-logická jednotka (ALU)

- **tranzistor**
    - polovodičová súčiastka
    - PNP alebo NPN
    - vieme vytvárať logické obovody

- **MOBO**
    - chipset, typ socketu, pci PCIe, USB porty, integrovaná grafická karta, zvuková karty, BIOS
    - **princíp práce**
        - **4 takty** - načítanie, rozkodovanie, komunikovanie s RAM, vstupno - vystupne zariadenie

- **GPU**
    - generuje signaly pre monitor, podla obsahu video pamäte (grafické rozlíšenie), do vdieopamäte zapisuje procesor
    - pri integrovanej grafickej karte môžeme veľkosť vyhradenej pamäte pre jej činnosť môžeme nastaviť v BIOS-e

# Suborove systemy n shit

- FAT - File Allocation Table
    - = Tabuľka umiestnenia súborov (na začiatku niekde v pamäťovom priestore)
    - meno + jeho adresa v dátovej časti pamäti
- NTFS vs FAT32 (používame bežne vo Windowse) ?
    - ext4 je podobné ako NTFS
    - vo FAT32 nie sú práva ku súborom
    - vo FAT32 nemôže byť súbor väčší ako 4 GB
    - oprávnenia: ![](permissions.png)
- čo je formátovanie ?
    - pri formátovaní sa vytvorí nová tabuľka súborového systému