# === Úloha 2===
# Napíšte program, ktorý  nájde v súbore vzor.txt najdlhšie slovo, vypíše ho a vypíše aj číslo riadka, na ktorom sa nachádza.

f = open("text.txt", "r")
riadky = f.readlines() # všetky riadky

najdlhsie_slovo = ""
riadok_najdlhsieho = 0

for i_riadka in range(0, len(riadky)):
    orezany_r = riadky[i_riadka].strip() # prec s \n na konci riadka
    slova_v_riadku = orezany_r.split(" ") # rozdel podla medzier

    for slovo in slova_v_riadku:
        if len(slovo) > len(najdlhsie_slovo):
            najdlhsie_slovo = slovo
            riadok_najdlhsieho = i_riadka + 1 # pretoze i_riadka=0 je pre PRVY riadok

print(f"Najdlhsie slovo: {najdlhsie_slovo}")
print(f"Je v riadku {riadok_najdlhsieho}")