from math import sqrt

def jePrvocislo(x):
    maxnum = int(sqrt(x))
    last_progress = 0
    for i in range(2, maxnum + 1):

        progress = int(i/maxnum * 100)
        
        if (progress != last_progress):
            last_progress = progress
            print(f"{progress} %")

        if x % i == 0:
            print("100 % HOTOVO")
            return False
    
    print("100 % HOTOVO")
    return x != 1 # default True ale mimo jednotky podla def

n = int(input("Zadajte cislo: "))

print(jePrvocislo(n))