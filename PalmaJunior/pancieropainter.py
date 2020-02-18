# cena je zaroven id
# Symboly
T=5 # trojuholnik
K=8 # kruh
S=3 # stvorec

def over_postupnost(postupnost, rozpocet):
    s = 0 # suma
    i = 0 # iterator, vsimame iteracnu dvojicu i, i+1
    l = len(postupnost)

    exist = set() # mnozina unikatnych prvkov
    # mozeme pouzit in
    for i in range(0, l-1): # <0, l-2>
        a = postupnost[i]
        b = postupnost[i + 1]

        # v pripade prvej dvojice testujeme existenciu i AJ i+1, dalej uz len i+1
        # existencia prvkov
        if i == 0:
            exist.add(a)
            s += a
        exist.add(b)
        s += b

        # za sebou 2 su
        if a == b:
            return False

    # nesu aspoň raz = mnozina existencie neni 3
    # print(f"Exist {exist}")
    if len(exist) != 3:
        return False
    
    # print(f"suma = {s}")
    # suma prevysuje rozpocet
    if s > rozpocet:
        return False
    
    # v ostatnych pripadoch vsetko v pohode
    return True


if __name__ == "__main__":
    print(over_postupnost([S, T, K, T], 21)) # tru
    print(over_postupnost([S, T], 50)) # fals lebo ne vsetky
    print(over_postupnost([S, T, T, K], 50)) # fals 2 za sebou