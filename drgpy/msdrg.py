
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

        self.drgmap = appndxrdr.read_a(
            f"data/{version}/appendix_A.txt")
        
        ccmap, exmap = appndxrdr.read_c(
            f"data/{version}/appendix_C.txt")
        self.ccmap = ccmap
        self.exmap = exmap

        orpcsmap = appndxrdr.read_e(
            f"data/{version}/appendix_D_E.txt")
        self.orpcsmap = orpcsmap

        uormap = appndxrdr.read_f(
            f"data/{version}/appendix_F_J.txt")
        self.uormap = uormap

    def get_features(self, dx_lst, pr_lst):

        x = [] # MDC, DRG, etc.
        z = [] # CC/MCC
       
        if len(dx_lst) > 0:
            # dx_lst[0]: primary/principal diagnosis
            # dx_lst[1:]: secondary diagnoses
            pdx = dx_lst[0]
            for j, dx in enumerate(dx_lst):
                is_pdx = j==0
                for x_i in self.dxmap[dx]:
                    if is_pdx:
                        x.append(x_i)
                    elif ("PDX" not in x_i and 
                        "_MDC" not in x_i):
                        x.append(x_i)
                if dx in self.ccmap and not is_pdx:
                    cc_info = self.ccmap[dx]
                    if pdx not in self.exmap.get(cc_info["pdx"],[]):
                        x.append("_" + cc_info["level"])

        for pr in pr_lst:
            for x_i in self.prmap[pr]:
                tokens = x_i.split("|")
                if len(tokens) > 2:
                    if all((x in pr_lst) for x in tokens[2:]):
                        x.append(tokens[0] + "|" + tokens[1])
                else:
                    x.append(x_i)
                
            if pr in self.orpcsmap:
                for matched_drg in self.orpcsmap[pr]:
                    x.append(f"_ORPCS|{matched_drg}")
                if pr not in self.uormap:
                    x.append("_ORPCS*")
            if pr in self.uormap:
                x.append("_UNREALTED_ORPCS")
    
        # TODO: need to identify if the patient is live at discharge
        # For now, we just assume all patients are alive
        x.append("_ALIVE")
        if len(dx_lst) == 1:
            x.append("_NDX1")
        elif len(dx_lst) > 1:
            x.append("_NDX2+")
        x.append("_STATUS01") # NOTE: AMA, other statuses ignored

        return Counter(x)

    def get_drg_all(self, dx_lst, pr_lst):

        y = []
        x = self.get_features(dx_lst, pr_lst)
        
        # NOTE: This is for debugging.
        #from pprint import pprint
        #pprint(x)
        
        y += mdcs0007.mdc00(x)
        y += mdcs0007.mdc01(x)
        y += mdcs0007.mdc02(x)
        y += mdcs0007.mdc03(x)
        y += mdcs0007.mdc04(x)
        y += mdcs0007.mdc05(x)
        y += mdcs0007.mdc06(x)
        y += mdcs0007.mdc07(x)
        y += mdcs0811.mdc08(x)
        y += mdcs0811.mdc09(x)
        y += mdcs0811.mdc10(x)
        y += mdcs0811.mdc11(x)
        y += mdcs1221.mdc12(x)
        y += mdcs1221.mdc13(x)
        y += mdcs1221.mdc14(x)
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
            if x["_ORPCS*"] > 0:
                if x["_MCC"] > 0:
                    y.append("981")
                elif x["_CC"] > 0:
                    y.append("982")
                else:
                    y.append("983")
            elif x["_UNRELATED_ORPCS"] > 0:
                if x["_MCC"] > 0:
                    y.append("987")
                elif x["_CC"] > 0:
                    y.append("988")
                else:
                    y.append("989")
 
        return y
  
    def get_drg_all2(self, dx_lst, pr_lst):

        y = []
        drg_lst = self.get_drg_all(dx_lst, pr_lst)
        for drg in drg_lst:
            y.append(self.drgmap.get(drg, None))
        y = [item for item in y if item is not None]
        return y

    def get_drg(self, dx_lst, pr_lst):
        """
        Return the corresponding DRG code for the diagnoses and procedures

        Parameters
        ----------
        dx_lst : list
                A list of ICD-10 diagnosis codes
        pr_lst : list
                A list of ICD-10 procedure codes
        """

        y_all = self.get_drg_all(dx_lst, pr_lst) 
        y_all = y_all + ["000"]
        return y_all[0]

        





