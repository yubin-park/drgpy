import csv
import re
from pkg_resources import resource_filename as rscfn
from collections import defaultdict

def shorten(x):
    x = " ".join(x.split())
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
        if "diagnos" in cache["sh2"].lower():
            codetype = "dx"
        elif "procedure" in cache["sh2"].lower():
            codetype = "pr"
    return codetype

def get_label(cache):
    i = len(cache["_"][cache["sh1"]])
    return "{}|{}.{}".format(cache["sh1"], i, cache["sh2"])

def update_cache(level, cache):
    if cache["sh1"] != "" and cache["sh2"] != "":
        cache["_"][cache["sh1"]][cache["sh2"]] = 1
    if level[:2] == "SH":
        cache["sh2"] = ""
    if level == "SH1":
        cache["sh1"] = ""

def update_mapping(dxmap, prmap, cache):
    if len(cache["sc"]) > 0:
        codetype = cache["sc"][0]
        code = cache["sc"][1]
        label = get_label(cache)
        if len(cache["sc"]) > 2:
            label = "{}|{}".format(label, cache["sc"][2]) # additional code
        if codetype == "dx":
            dxmap[code].append(label)
        elif codetype == "pr":
            prmap[code].append(label)
        cache["sc"] = []
 
def parse(line, cursor, dxmap, prmap, cache):

    # sh1
    drg_lst = re.findall("DRG\s(\d{3})\s", line)
    dx_pttrn = "[A-TV-Z][0-9][0-9AB][0-9A-TV-Z]{0,4}"
    pr_pttrn = "[A-HJ-NP-Z0-9]{7}"
    dx_lst = re.findall("\s{2}"+dx_pttrn + "\s+", line)
    pr_lst = re.findall("\s{2}"+pr_pttrn + "\*?\s+", line)
    pr_lst += re.findall("\s{3}and\s"+pr_pttrn + "\*?\s+", line)

    if len(drg_lst) > 0 and line[:3] == "DRG": # SH1
        drg = drg_lst[0]
        if cursor != "SH1":
            update_mapping(dxmap, prmap, cache)
            update_cache("SH1", cache)
            cache["sh1"] = drg
        else:
            cache["sh1"] += ("&" + drg)
        cursor = "SH1"
    elif len(dx_lst) == 0 and len(pr_lst) == 0: # SH2
        if cursor != "SH2":
            update_mapping(dxmap, prmap, cache)
            update_cache("SH2", cache)
            cache["sh2"] = shorten(line.strip())
        else:
            cache["sh2"] += (" " + shorten(line.strip()))
        cursor = "SH2"
    else: # SC: code sections
        codetype = get_codetype(dx_lst, pr_lst, cache)
        tokens = line.split()
        code = tokens[0]
        if tokens[0] == "and":
            code = tokens[1]
            cache["sc"].append(code)
        else:
            if len(cache["sc"]) > 0:
                update_mapping(dxmap, prmap, cache)
            cache["sc"] = [codetype, code]
        cursor = "SC"

    return cursor

def read(fn, dxmap, prmap):

    """
    M        :?=======...                 
    M        MDC XX...
    M        :?=======...
    M          MDC contents
    (blank) 
    A        +-------...
    A        | Abstract Table about DRG...
    A        +-------...
    (blank)  
    SH1      DRG XXX...
    (blank)
    SH2      Details...
    SC         Codes...

    * e.g. M -> A -> Sx -> Sx -> A -> Sx -> M
    * Sx is always followed by either A or Sx
    * M always precedes A
    * SH2 
    """
    cursor = ""
    cache = {"sh1": "", 
            "sh2": "", 
            "sc": "", 
            "_": defaultdict(dict)}
    fn = rscfn(__name__, fn)
   
    with open(fn, "r") as fp:
        for line in fp:
            line = line.replace("\n","")
            if line.strip() == "":
                continue

            if line[1:3] == "==":
                cursor = "M"
            elif line[:2] == "+-" or line[0]=="|":
                cursor = "A"
            elif cursor != "M": 
                cursor = parse(line, cursor, dxmap, prmap, cache) 

    return dxmap, prmap
                
if __name__=="__main__":

    fn_lst = ["data/mdcs_00_07.txt",
                "data/mdcs_08_11.txt",
                "data/mdcs_12_21.txt",
                "data/mdcs_22_25.txt"]
    dxmap = defaultdict(list)
    prmap = defaultdict(list)
    for fn in fn_lst[1:2]:
        dxmap, prmap = read(fn, dxmap, prmap)

    import json
    print(json.dumps(prmap, indent=2, sort_keys=True))

