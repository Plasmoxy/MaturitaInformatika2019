f = open("text.txt", "r")

for line in f:
    for slovo in line.strip().split(" "):
        print(slovo)

f.close()