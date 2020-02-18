
def pocet_bodov(original, prepis):
    body = 0
    l = len(original)
    i = 0

    while i < l:
        # osobitne riesime ak sme sa dostali na posledky znak
        # lebo by sme vyuzivali i+1 out of bounds
        if i == l-1 and original[i] != prepis[i]:
            body += 2 # bola zamena? pridaj 2 body
            break # uz necheckujeme nic sme na poslednom

        # pre neposledne znaky:
        # ak nerovanju, moze byt vymena alebo zamena
        if original[i] != prepis[i]:
            # ak plati krizova rovnost s i+1, je to vymena
            if original[i] == prepis[i+1] and original[i+1] == prepis[i]:
                body += 1
                i += 1 # ale kedze sme vyriesili 2 znaky, musime sa dokopy posunut o 2 znaky dopredu
            else:
                body += 2
        # posun sa na dalsi znak
        i += 1
    
    return body

#test:
if __name__ == "__main__":
    print(pocet_bodov("ahoj pes", "aho jpes")) # vymena medzery - 1
    print(pocet_bodov("ahoj", "ahok")) # posledny znak zamena - 2
    print(pocet_bodov("ahoj", "ahjo")) # posloedna vymena - 1
    print(pocet_bodov("ahoj", "hajo")) # aj v strede aj posloedna vymena - 2
    print(pocet_bodov("ahoje", "poiwt")) # celezle = 10

# poznamka: program je v pripade nudze mozne pouzit
# na zistenie gramatickym chyb
# v zdrojovom kode samozhneho programu