
S = [[10, 2], [20, 4], [30, 3]]

def vyska_bambusu(strihania, den):
    # vyska bambusu je den lebo dy/dx=1
    # den=vyska, od tejto vysky dalej odpocitam vsetky diferencie
    # ktorych datum je mensi ako den
    d = 0
    # st[den, odstrih]
    for st in strihania:
        if st[0] <= den:
            d += st[1]
    return den - d

# test:
if __name__ == "__main__":
    for i in range(S[-1][0]+2):
        print(vyska_bambusu(S, i), end=" ")
        for j in S:
            if i == j[0]:
                print()
    
