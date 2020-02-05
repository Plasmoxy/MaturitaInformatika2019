from sys import argv
from codecs import open as copen

parsemap = [
    ["rychlo ", "def "],
    [" je ", " = "],
    [" je tiš ", " == "],
    ["zisci či ", "if "],
    ["inakši:", "else:"],
    [" a ", " and "],
    ["vycahni(", "open("],
    ["zos ", "from "],
    ["doniš ", "import "],
    ["odpočuvanie(", "input("],
    [".užnepouživaj()", ".close()"],
    [".pisaj(", ".write("],
    ["pre šicke ", "for "],
    [" vof ", " in "],
    ["rozsahu(", "range("],
    ["keľozabera(", "len("]
]

def to_python(code: str):
    for c in parsemap:
        code = code.replace(c[0], c[1])
    return code

def to_faggotpython(code: str):
    for c in parsemap:
        code = code.replace(c[1], c[0])
    return code

with copen("python/strukturovane_typy/bubble_retard_sort_visual.py", "r", "utf-8") as src:
    with copen("fagoutput.fag", "w+", "utf-8") as fag:
        fag.write(to_faggotpython(src.read()))