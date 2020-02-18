from time import sleep
from random import randint, choice

def wrtarray(a):
    with open("kys.txt", "w+") as f:
        s = ""
        for y in range(0, len(a)):
            for x in range(0, len(a[y])):
                s += str(a[y][x])
            s += "\n"
        f.writelines(s)

genrand = lambda w, h: [[choice(["\\", "/", "_", "|", " "]) for i in range(w)] for i in range(h)]

while True:
    wrtarray(genrand(50, 20))
    sleep(0.5)