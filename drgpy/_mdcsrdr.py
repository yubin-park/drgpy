import csv
import re
from pkg_resources import resource_filename as rscfn
from collections import defaultdict

dx_pttrn = "[A-TV-Z][0-9][0-9AB][0-9A-TV-Z]{0,4}"
pr_pttrn = "[A-HJ-NP-Z0-9]{7}"

def shorten(x):
    x = " ".join(x.upper().split())
    x = x.replace("DIAGNOSES", "DIAGNOSIS")
    x = x.replace("PROCEDURES", "PROCEDURE")
    x = x.replace("PRINCIPAL OR SECONDARY DIAGNOSIS", "PSDX")
    x = x.replace("PRINCIPAL DIAGNOSIS", "PDX")
    x = x.replace("SECONDARY DIAGNOSIS", "SDX")
    x = x.replace("OPERATING ROOM PROCEDURE", "ORPCS")
    return x

def get_codetype(dx_lst, pr_lst, cache):
    codetype = ""
    if len(dx_lst) > 0 and len(pr_lst) == 0:
        codetype = "dx"
    elif len(dx_lst) == 0 and len(pr_lst) > 0:
        codetype = "pr"
    else:
        if "DX" in cache["D"]:
            codetype = "dx"
        else:
            codetype = "pr"
    return codetype

def get_label(cache):
    label = f'{cache["C"]}|{cache["D"]}'
    while label in cache["L"]:
        label = label + "*"
    return label 

def update_mapping(dxmap, prmap, cache):
    if len(cache["E"]) > 0:
        codetype = cache["E"][0]
        code = cache["E"][1]
        label = get_label(cache)
        if len(cache["E"]) > 2:
            for code_add in cache["E"][2:]:
                label = f"{label}|{code_add}" # additional code
        if codetype == "dx":
            dxmap[code].append(label)
        elif codetype == "pr":
            prmap[code].append(label)
        cache["E"] = []

def is_A(line, cursor):
    return (line[1:3] == "==")

def parse_A(line, cursor, dxmap, cache):
    mdc_lst = re.findall("MDC\s(\d{2})\s", line)
    dx_lst = re.findall("\s{2}" + dx_pttrn + "\s+", line)
    if len(mdc_lst) > 0:
        cache["A"] = "_MDC" + mdc_lst[0] 
    elif len(dx_lst) > 0:
        dx = dx_lst[0].strip()
        dxmap[dx].append(cache["A"])

def is_B(line, cursor):
    return ((cursor in {"A", "B", "D", "E"} and (line[:2] == "+-" )) or 
            (cursor in {"B"} and line[0]=="|"))

def is_C(line, cursor):
    return (cursor in {"B", "C", "D", "E"} and line[:4] == "DRG ")

def parse_C(line, cursor, cache, _cursor):

    drg_lst = re.findall("DRG\s(\d{3})\s", line)
    if len(drg_lst) > 0:
        drg = drg_lst[0]
        if _cursor != "C":
            cache["C"] = drg
            cache["D"] = ""
            cache["E"] = []
        else:
            cache["C"] += ("&" + drg)

def is_D(line, cursor):
    return (cursor in {"C", "D", "E"} and line[:2].strip() != "")

def parse_D(line, cursor, cache, _cursor):

    line = line.strip()
    if line == "":
        return

    phrase = shorten(line)
    if _cursor != "D":
        # NOTE: to keep track of duplicate names
        cache["L"][get_label(cache)] = 1
        cache["D"] = phrase
        cache["E"] = []
    else:
        cache["D"] += (" " + phrase)

def is_E(line, cursor):
    return (cursor in {"D", "E"} and line[:2] == "  ")

def parse_E(line, cursor, dxmap, prmap, cache, _cursor):

    line = line.strip() 
    if line == "":
        update_mapping(dxmap, prmap, cache)
        return

    dx_lst = re.findall(dx_pttrn + "\s+", line)
    pr_lst = re.findall(pr_pttrn + "\*?\s+", line)
    pr_lst += re.findall("and\s"+pr_pttrn + "\*?\s+", line)
    codetype = get_codetype(dx_lst, pr_lst, cache)
    tokens = [x.replace("*", "") for x in line.split()]
    code = tokens[0]
    if tokens[0] == "and":
        code = tokens[1]
        cache["E"].append(code)
    else:
        if len(cache["E"]) > 0:
            update_mapping(dxmap, prmap, cache)
        cache["E"] = [codetype, code]

def read(fn, dxmap, prmap):

    """
    A        :?=======...                 
    A        MDC XX...
    A        :?=======...
    A          MDC contents
    A        (blank) 
    B        +-------...
    B        | Abstract Table about DRG...
    B        +-------...
    B        (blank)  
    C        DRG XXX...
    C        (blank)
    D        Details...
    D        (blank)
    E          Codes...

    *pattern: A -> [B -> [C -> [D -> (E)]]]
    """

    _cursor = "F"
    cursor = "F"
    cache = {"A": "", 
            "C": "", 
            "D": "",
            "E": [],
            "_": defaultdict(dict),
            "L": {}}
    fn = rscfn(__name__, fn)
   
    with open(fn, "r") as fp:
        for line in fp:
            line = line.replace("\n","")

            if line.strip()=="":
                pass
            elif is_A(line, cursor):
                cursor = "A"
            elif is_B(line, cursor):
                cursor = "B"
            elif is_C(line, cursor):
                cursor = "C"
            elif is_D(line, cursor):
                cursor = "D"
            elif is_E(line, cursor):
                cursor = "E"

            if cursor == "A":
                parse_A(line, cursor, dxmap, cache)            
            elif cursor == "B":
                pass
            elif cursor == "C":
                parse_C(line, cursor, cache, _cursor) 
            elif cursor == "D":
                parse_D(line, cursor, cache, _cursor) 
            elif cursor == "E":
                parse_E(line, cursor, dxmap, prmap, cache, _cursor)

            _cursor = cursor

    return dxmap, prmap
                
if __name__=="__main__":

    fn_lst = ["data/v40/mdcs_00_07.txt",
                "data/v40/mdcs_08_11.txt",
                "data/v40/mdcs_12_21.txt",
                "data/v40/mdcs_22_25.txt"]
    dxmap = defaultdict(list)
    prmap = defaultdict(list)
    for fn in fn_lst[:1]:
        dxmap, prmap = read(fn, dxmap, prmap)

    import json
    #print(json.dumps(prmap, indent=2, sort_keys=True))
    x = {}
    for k, v in prmap.items():
        for vv in v:
            if "246&247" in vv or "248&249" in vv:
                x[vv] = 1
    #from pprint import pprint
    #pprint(x)
    print(dxmap["I2601"])

