"""
triedenie pomocou minima
zložitosť algoritmu sa značí O(n)


"""

# minimum v <a, b)
def minimumpos(l, a, b):
    mpoz = a
    for i in range(a, b):
        if l[i] < l[mpoz]:
            mpoz = i
    return mpoz

def retard_sort(l):
    lenl = len(l)

    for i in range(lenl):
        # najdi najmensie cislo v rozsahu <i, len-1)
        x = minimumpos(l, i, lenl)

        # trepni ho na zaciatok
        l[i], l[x] = l[x], l[i]
        print(l)
    return l

ls = [4, 6, 2, 0, -2]
print(f"Original = {ls}")
print(f"Sorted = {retard_sort(ls)}")