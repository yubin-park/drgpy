
import drgpy._mdcsrdr as mdcsrdr
import drgpy._appndxrdr as appndxrdr
import drgpy._mdcsrls as mdcsrls
from collections import defaultdict


class DRGEngine:

    def __init__(self):
        dxmap = defaultdict(list)
        prmap = defaultdict(list)
        dxmap, prmap = mdcsrdr.read("data/mdcs_00_07.txt", dxmap, prmap)
        dxmap, prmap = mdcsrdr.read("data/mdcs_08_11.txt", dxmap, prmap)
        dxmap, prmap = mdcsrdr.read("data/mdcs_12_21.txt", dxmap, prmap)
        dxmap, prmap = mdcsrdr.read("data/mdcs_22_25.txt", dxmap, prmap)
        self.dxmap = dxmap
        self.prmap = prmap
        
        ccmap, exmap = appndxrdr.read_c()
        self.ccmap = ccmap
        self.exmap = exmap

    def get_dxel(self, dx_lst):

        el_lst = []
        cc_lst = []
        if len(dx_lst)==0:
            return code_lst
        
        # dx_lst[0]: primary/principal diagnosis
        # dx_lst[1:]: secondary diagnoses
        pdx = dx_lst[0]
        for i, dx in enumerate(dx_lst):
            elements = self.dxmap[dx]
            if dx in self.ccmap and i > 0:
                cc_info = self.ccmap[dx]
                if pdx not in self.exmap[cc_info["pdx"]]:
                    cc_lst.append(cc_info["level"])
            for el in elements:
                if "PDX" in el and i > 0:
                    continue
                el_lst.append(el)
        
        if "MCC" in cc_lst:
            el_lst.append("MCC")
        elif "CC" in cc_lst:
            el_lst.append("CC")
   
        return el_lst

    def get_prel(self, pr_lst):
        el_lst = []
        for pr in pr_lst:
            elements = self.prmap[pr]
            el_lst += elements
        return el_lst 

    def get_drg(self, dx_lst, pr_lst):

        el_lst = self.get_dxel(dx_lst)
        el_lst += self.get_prel(pr_lst)

        pass


    





