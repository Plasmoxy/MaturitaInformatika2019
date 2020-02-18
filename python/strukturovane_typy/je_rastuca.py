from random import randint

def je_rastuca(l):
    for i in range(0, len(l) - 1):
        if (l[i] >= l[i+1]): # ak ide vacsi a za nim mensi alebo rovny, neni rastuca
            return False
    return True

j = [ randint(0, 3) for i in range(0, 3) ]
print(j)
print(je_rastuca(j))