
def minimumpos(l, a, b):
    mpoz = a
    for i in range(a, b):
        if l[i] < l[mpoz]:
            mpoz = i
    return mpoz

def retard_sort(l):
    orlen = len(l)

    for i in range(orlen):
        # najdi najmensie cislo v rozsahu <i, len)
        x = minimumpos(l, i, orlen)

        # trepni ho na zaciatok
        l[i], l[x] = l[x], l[i]
        print(l)
    return l

ls = [4, 6, 2, 0, -2]
print(f"Original = {ls}")
print(f"Sorted = {retard_sort(ls)}")