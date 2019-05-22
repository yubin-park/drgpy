import csv
import re
from pkg_resources import resource_filename as rscfn
from collections import defaultdict

class MDCSReader:

    def __init__(self):
        self._cursor = ""
        self._cache_sh1 = ""
        self._cache_sh2 = ""
        self._cache_sc = []
        self._cache = defaultdict(dict)
        self.dxmap = defaultdict(list)
        self.pcsmap = defaultdict(list)

    def init_fn(self, fn):
        self.fn = rscfn(__name__, fn)
        self._cursor = ""
        self._cache_sh1 = ""
        self._cache_sh2 = ""
        self._cache_sc = []
  
    def parse(self, line):

        def shorten(x):
            x = " ".join(x.split())
            x = x.replace("DIAGNOSES", "DIAGNOSIS")
            x = x.replace("PROCEDURES", "PROCEDURE")
            x = x.replace("PRINCIPAL OR SECONDARY DIAGNOSIS", "PSDX")
            x = x.replace("PRINCIPAL DIAGNOSIS", "PDX")
            x = x.replace("SECONDARY DIAGNOSIS", "SDX")
            x = x.replace("OPERATING ROOM PROCEDURE", "ORPCS")
            return x

        def get_codetype(dx_lst, pcs_lst):
            codetype = ""
            if len(dx_lst) > 0 and len(pcs_lst) == 0:
                codetype = "dx"
            elif len(dx_lst) == 0 and len(pcs_lst) > 0:
                codetype = "pcs"
            else:
                if "diagnos" in self._cache_sh2.lower():
                    codetype = "dx"
                elif "procedure" in self._cache_sh2.lower():
                    codetype = "pcs"
            return codetype

        def get_label():
            i = len(self._cache[self._cache_sh1])
            return "{}|{}.{}".format(self._cache_sh1, i, self._cache_sh2)

        def update_cache(level):
            if self._cache_sh1 != "" and self._cache_sh2 != "":
                self._cache[self._cache_sh1][self._cache_sh2] = 1
            if level[:2] == "SH":
                self._cache_sh2 = ""
            if level == "SH1":
                self._cache_sh1 = ""

        def update_mapping():
            if len(self._cache_sc) > 0:
                codetype = self._cache_sc[0]
                code = self._cache_sc[1]
                label = get_label()
                if len(self._cache_sc) > 2:
                    label = "{}|{}".format(label, self._cache_sc[2])
                if codetype == "dx":
                    self.dxmap[code].append(label)
                elif codetype == "pcs":
                    self.pcsmap[code].append(label)
                self._cache_sc = []

        if self._cursor == "M":
            return

        # sh1
        drg_lst = re.findall("DRG\s(\d{3})\s", line)
        dx_pttrn = "[A-TV-Z][0-9][0-9AB][0-9A-TV-Z]{0,4}"
        pcs_pttrn = "[A-HJ-NP-Z0-9]{7}"
        dx_lst = re.findall("\s{2}"+dx_pttrn + "\s+", line)
        pcs_lst = re.findall("\s{2}"+pcs_pttrn + "\*?\s+", line)
        pcs_lst += re.findall("\s{3}and\s"+pcs_pttrn + "\*?\s+", line)

        if len(drg_lst) > 0 and line[:3] == "DRG": # SH1
            drg = drg_lst[0]
            if self._cursor != "SH1":
                update_mapping()
                update_cache("SH1")
                self._cache_sh1 = drg
            else:
                self._cache_sh1 += ("&" + drg)
            self._cursor = "SH1"
        elif len(dx_lst) == 0 and len(pcs_lst) == 0: # SH2
            if self._cursor != "SH2":
                update_mapping()
                update_cache("SH2")
                self._cache_sh2 = shorten(line.strip())
            else:
                self._cache_sh2 += (" " + shorten(line.strip()))
            self._cursor = "SH2"
        else: # SC: code sections
            codetype = get_codetype(dx_lst, pcs_lst)
            tokens = line.split()
            code = tokens[0]
            if tokens[0] == "and":
                code = tokens[1]
                self._cache_sc.append(code)
            else:
                if len(self._cache_sc) > 0:
                    update_mapping()
                self._cache_sc = [codetype, code]
            self._cursor = "SC"

    def read(self):

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
        with open(self.fn, "r") as fp:
            for line in fp:
                line = line.replace("\n","")
                if line.strip() == "":
                    continue

                if line[1:3] == "==":
                    self._cursor = "M"
                elif line[:2] == "+-" or line[0]=="|":
                    self._cursor = "A"
                else: 
                    self.parse(line)
                    
if __name__=="__main__":

    fn_lst = ["data/mdcs_00_07.txt",
                "data/mdcs_08_11.txt",
                "data/mdcs_12_21.txt",
                "data/mdcs_22_25.txt"]
    reader = MDCSReader()
    for fn in fn_lst:
        reader.init_fn(fn) 
        reader.read()

    #import json
    #print(json.dumps(reader._cache, indent=2, sort_keys=True))
    #with open("dxmap.json", "w") as fp:
    #    json.dump(reader.dxmap, fp, indent=2, sort_keys=True)
    #with open("pcsmap.json", "w") as fp:
    #    json.dump(reader.pcsmap, fp, indent=2, sort_keys=True)

