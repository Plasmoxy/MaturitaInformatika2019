"""
aspoň 89% ... 100% = 1
75% ... = 2
50% ... = 3
35% ... = 4
0% ... = 5


"""

def znamka(p):
    if p < 35 :
        return 5
    elif p < 50 :
        return 4
    elif p < 75 :
        return 3
    elif p < 89 :
        return 2
    else :
        return 1

for i in range(0, 100, 5):
    print(f"{i}% -> {znamka(i)}")