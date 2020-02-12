from codecs import open
print("konverter")

f = open("./ulohy/Ulohy.txt", "r", "utf-8")
ulohyStr= f.read()
f.close()

ucount = 1
usplt = ulohyStr.split("Uloha\r\n")
i = 1

while i < len(usplt):
  ustr = usplt[i].strip()

  if ustr.strip() != "":
    f = open(f"./ulohy/u{str(i).zfill(2)}.py", "w+", "utf-8")
    f.write(f"# === Úloha {i}===\r\n")
    ulns = ustr.split("\r\n")
    for l in ulns:
      f.write(f"# {l.strip()}\r\n")
    f.write("\r\n")
    f.close()

  i += 1
