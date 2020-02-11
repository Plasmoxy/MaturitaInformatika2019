from codecs import open
print("konverter")

f = open("./ulohy/Ulohy.txt", "r", "utf-8")
lns = f.readlines()
f.close()

outs = "# ====== Maturitné úlohy z inf 2020 ======\n\n"
ucount = 1

for l in lns:
  if l.strip() == "Uloha" :
    outs += f"print(\"=== Uloha [{ucount}] ===\")\n"
    outs += f"===================================\n"
    ucount += 1
  elif l.strip() == "" :
    outs += "\n\n\n"
  else:
    outs += f"### {l}"

print(outs)

f = open("./ulohy/ulohyall.py", "w", "utf-8")
f.write(outs)
f.close()


    