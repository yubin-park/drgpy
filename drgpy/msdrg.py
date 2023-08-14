
import drgpy._mdcsrdr as mdcsrdr
import drgpy._appndxrdr as appndxrdr
import drgpy._mdcs0007 as mdcs0007
import drgpy._mdcs0811 as mdcs0811
import drgpy._mdcs1221 as mdcs1221
import drgpy._mdcs2225 as mdcs2225
from collections import defaultdict
from collections import Counter

class DRGEngine:

    def __init__(self, version="v40"):
        dxmap = defaultdict(list)
        prmap = defaultdict(list)
        dxmap, prmap = mdcsrdr.read(
                f"data/{version}/mdcs_00_07.txt", dxmap, prmap)
        dxmap, prmap = mdcsrdr.read(
                f"data/{version}/mdcs_08_11.txt", dxmap, prmap)
        dxmap, prmap = mdcsrdr.read(
                f"data/{version}/mdcs_12_21.txt", dxmap, prmap)
        dxmap, prmap = mdcsrdr.read(
                f"data/{version}/mdcs_22_25.txt", dxmap, prmap)
        self.dxmap = dxmap
        self.prmap = prmap
        self.version = version

        self.drgmap = appndxrdr.read_a(
            f"data/{version}/appendix_A.txt")
        
        ccmap, exmap = appndxrdr.read_c(
            f"data/{version}/appendix_C.txt")
        self.ccmap = ccmap
        self.exmap = exmap

        orpcsmap = appndxrdr.read_e(
            f"data/{version}/appendix_D_E.txt")
        self.orpcsmap = orpcsmap

        neoormap = appndxrdr.read_f(
            f"data/{version}/appendix_F_J.txt")
        self.neoormap = neoormap

    def get_features(self, dx_lst, pr_lst, gender="F", is_alive=True):

        def remove_dups(seq):
            seen = set()
            seen_add = seen.add
            return [x for x in seq if not (x in seen or seen_add(x))]

        x = [] # MDC, DRG, etc.
        z = [] # CC/MCC
        dx_lst = remove_dups(dx_lst)
        pr_lst = remove_dups(pr_lst)
       
        if len(dx_lst) > 0:
            # dx_lst[0]: primary/principal diagnosis
            # dx_lst[1:]: secondary diagnoses
            pdx = dx_lst[0]
            if len(self.dxmap[pdx]) == 0:
                pdx = pdx[:-1] # generalize; maybe too specific
                dx_lst[0] = pdx

            for j, dx in enumerate(dx_lst):
                is_pdx = j==0
                for x_i in self.dxmap[dx]:
                    if is_pdx:
                        x.append(x_i)
                    elif "PDX OR SDX" in x_i:
                        x.append(x_i)
                    elif ("PDX" not in x_i and 
                        "_MDC" not in x_i):
                        x.append(x_i)

                if dx in self.ccmap and not is_pdx:
                    cc_info = self.ccmap[dx]
                    if pdx not in self.exmap.get(cc_info["pdx"],[]):
                        x.append("_" + cc_info["level"])

            # NOTE: special cases to handle EXCEPT conditions
            if "_MDC18" in x and "853&854&855|PDX FROM MDC 18 EXCEPT" not in x:
                x.append("853&854&855|PDX")

        # keep the procedures that made the multi-proc definitions
        multi_proc_set = {} 
        for pr_1 in pr_lst:
            for x_i in self.prmap[pr_1]:
                tokens = x_i.split("|")
                if len(tokens) < 3:
                    continue
                # multi-procedure rule  
                if all((pr_i in pr_lst) for pr_i in tokens[2:]):
                    x_j = tokens[0] + "|" + tokens[1]
                    x.append(x_j)
                    # DRG 466-468; multi-proc definitions precede...
                    if x_j == "466&467&468|ORPCS":
                        multi_proc_set[pr_1] = 1
                        for pr_i in tokens[2:]:
                            multi_proc_set[pr_i] = 1

        for pr in pr_lst:
            for x_i in self.prmap[pr]:
                if pr in multi_proc_set:
                    continue
                if len(x_i.split("|")) > 2:
                    continue
                x.append(x_i)

            if pr in self.orpcsmap:
                for matched_drg in self.orpcsmap[pr]:
                    x.append(f"_ORPCS|{matched_drg}")
                    x.append("_ORPCS_ANY")
                if pr in self.neoormap:
                    x.append("_ORPCS_NON_EXTENSIVE")
                else:
                    x.append("_ORPCS_EXTENSIVE")

        if gender=="F":
            x.append("_FEMALE")
        else:
            x.append("_MALE")

        if is_alive:
            x.append("_ALIVE")
        
        if len(dx_lst) == 1:
            x.append("_NDX1")
        elif len(dx_lst) > 1:
            x.append("_NDX2+")
        x.append("_STATUS01") # NOTE: AMA, other statuses ignored
        
        return Counter(x)

    def get_drg_all(self, 
                    dx_lst, 
                    pr_lst, 
                    gender="F", 
                    is_alive=True):

        y = []
        x = self.get_features(dx_lst, pr_lst, gender, is_alive)
        
        # NOTE: This is for debugging.
        #from pprint import pprint
        #pprint(x)
        
        y += mdcs0007.mdc00(x)
        y += mdcs0007.mdc01(x)
        y += mdcs0007.mdc02(x)
        y += mdcs0007.mdc03(x)
        y += mdcs0007.mdc04(x)
        y += mdcs0007.mdc05(x, self.version)
        y += mdcs0007.mdc06(x)
        y += mdcs0007.mdc07(x)
        y += mdcs0811.mdc08(x)
        y += mdcs0811.mdc09(x)
        y += mdcs0811.mdc10(x)
        y += mdcs0811.mdc11(x)
        y += mdcs1221.mdc12(x)
        y += mdcs1221.mdc13(x)
        y += mdcs1221.mdc14(x, self.version)
        y += mdcs1221.mdc15(x)
        y += mdcs1221.mdc16(x)
        y += mdcs1221.mdc17(x)
        y += mdcs1221.mdc18(x)
        y += mdcs1221.mdc19(x)
        y += mdcs1221.mdc20(x)
        y += mdcs1221.mdc21(x)
        y += mdcs2225.mdc22(x)
        y += mdcs2225.mdc23(x)
        y += mdcs2225.mdc24(x)
        y += mdcs2225.mdc25(x)

        # NOTE: Appendix F - No PDX mapped
        if len(y) == 0:
            if x["_ORPCS_EXTENSIVE"] > 0:
                if x["_MCC"] > 0:
                    y.append("981")
                elif x["_CC"] > 0:
                    y.append("982")
                else:
                    y.append("983")
            elif x["_ORPCS_NON_EXTENSIVE"] > 0:
                if x["_MCC"] > 0:
                    y.append("987")
                elif x["_CC"] > 0:
                    y.append("988")
                else:
                    y.append("989")
 
        return y

    def get_drg(self, dx_lst, pr_lst, gender="F", is_alive=True):
        """
        Return the corresponding DRG code for the diagnoses and procedures

        Parameters
        ----------
        dx_lst : list
                A list of ICD-10 diagnosis codes
        pr_lst : list
                A list of ICD-10 procedure codes
        gender: str
                "F" or "M"
        is_alive: boolean
                if the patient is alive at discharge (True)
        """

        y_all = self.get_drg_all(dx_lst, pr_lst, gender, is_alive) 
        y_all = y_all + ["000"]
        return y_all[0]

        





