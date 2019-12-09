
def druhy_najmensi(l):
    druhy = l[1] # rozdielne indexy!!!
    prvy = l[0]

    for c in l:
        if c < prvy:
            druhy = prvy
            prvy = c
        
    
    return druhy


lcisla = list(range(8, 29, 3))

print(lcisla)
print(druhy_najmensi(lcisla))

t = [ 2, 1, 3, 4, 5 ]
print(t)
print(druhy_najmensi(t))