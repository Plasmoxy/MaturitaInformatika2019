from codecs import open as copen

b = copen("basen.txt", "r", "utf-8")
cp = copen("kopia.txt", "w", "utf-8")

slovo = input("Zadaj svoje oblubene slovo: ")

for l in b.readlines():
    # ak prazdny riadok, vpis slovo
    if len(l.strip()) == 0:
        cp.write(slovo + "\n") 
    # ak ne, vpis dany riadok
    else:
        cp.write(l)

b.close()
cp.close()