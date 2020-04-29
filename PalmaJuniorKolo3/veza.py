delba = [1]

for i in range (2,1000000):
    DELITe = True
    for o in delba:
        if i%o != 0:
            DELITe =False
        else:
            continue
    if DELITe == True:
        delba.append(i)


print( delba)
