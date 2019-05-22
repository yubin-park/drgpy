import csv
import re
from pkg_resources import resource_filename as rscfn

def read_a(fn):
    drgmap = {}
    is_drg_section = False
    fn = rscfn(__name__, fn)
    with open(fn, "r") as fp:
        for line in fp:
            drg = line[:4].strip()
            if drg == "DRG":
                is_drg_section = True
                continue
            if not is_drg_section:
                continue
            mdc = line[4:8].strip()
            medsurg = line[8:11].strip()
            desc = line[11:].strip()
            drgmap[drg] = {"mdc": mdc,
                        "is_medical": medsurg=="M",
                        "is_surgical": medsurg=="P",
                        "desc": desc}
    return drgmap

def read_c(fn):
    ccmap = {}
    exmap = {}
    is_cc_section = False
    is_pdx_section = False
    is_part2 = False
    pdx_code = ""
    fn = rscfn(__name__, fn)
    with open(fn, "r") as fp:
        for line in fp:
            if line.strip() == "":
                continue
            if "I10 Dx  Lev PDX Exclusions" in line:
                is_cc_section = True
                continue
            elif "PDX collection " in line:
                is_pdx_section = True
                is_cc_section = False
                pdx = line.split("collection")[1].strip()
                continue
            elif "Appendix C Part 2:" in line:
                is_part2 = True
                is_pdx_section = False
                continue

            if is_cc_section:
                dx = line[:9].strip()
                cc = line[9:12].strip()
                pdx = line[12:29].strip().split(":")[0]
                ccmap[dx] = {"pdx": pdx,
                            "level": cc,
                            "aowa": False} # aowa: apply only when alive
            elif is_pdx_section:
                dx = line.split()[0]
                if pdx not in exmap:
                    exmap[pdx] = []
                exmap[pdx].append(dx)
            elif is_part2:
                dx = line[:8].strip()
                ccmap[dx]["aowa"] = True
    return ccmap, exmap

def read_d(fn):
    rankmap = {}
    rank = 0
    is_rank_section = False
    fn = rscfn(__name__, fn)
    with open(fn, "r") as fp:
        for line in fp:
            if line[:3] == "MDC":
                is_rank_section = True
                continue
            elif is_rank_section and line.strip() == "":
                # End of the rank section
                break

            if is_rank_section:
                tokens = line[:9].strip().split("-")
                if len(tokens) == 1:
                    tokens.append(tokens[0])
                for drg in range(int(tokens[0]), int(tokens[1])+1):
                    rankmap[str(drg)] = rank
                    rank += 1
    return rankmap

if __name__=="__main__":
    #read_a("data/appendix_A.txt")
    #read_c("data/appendix_C.txt")
    #read_d("data/appendix_D_E.txt")




