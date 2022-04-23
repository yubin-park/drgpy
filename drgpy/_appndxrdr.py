import csv
import re
from pkg_resources import resource_filename as rscfn

def read_a(fn="data/appendix_A.txt"):
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
            drgmap[drg] = {"drg": drg,
                        "mdc": mdc,
                        "is_medical": medsurg=="M",
                        "is_surgical": medsurg=="P",
                        "desc": desc}
    return drgmap

def read_c(fn="data/appendix_C.txt"):
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

def read_d(fn="data/appendix_D_E.txt"):
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

def read_e(fn="data/appendix_D_E.txt"):
    # orpcs: Operating Room Procedures
    orpcsmap = {}
    is_orpcs_section = False
    fn = rscfn(__name__, fn)
    with open(fn, "r") as fp:
        for line in fp:
            if line.strip() == "CODE    MDC MS-DRG  SURGICAL CATEGORY":
                is_orpcs_section = True
            elif line.strip() == "Procedure Cluster/MS-DRG Index":
                # end of the orpcs section
                break

            if is_orpcs_section:
                if len(line) < 9:
                    continue
                code = line[:9].strip()
                is_nonorpcs = (line[9] == "*")
                if not is_nonorpcs and code not in {"", "CODE"}:
                    targets = line[16:24].strip().split('-')
                    drgs = []
                    for drg in range(int(targets[0]), int(targets[-1])+1):
                        drgs.append(str(drg).zfill(3))

                    orpcsmap[code] = drgs
    return orpcsmap

def read_f(fn="data/appendix_F_J.txt"):

    uormap = {}
    is_uor_section = False
    fn = rscfn(__name__, fn)
    with open(fn, "r") as fp:
        for line in fp:
            if "DRG 989 NON-EXTENSIVE O.R. PROCEDURE" in line:
                is_uor_section = True
                continue
            elif is_uor_section and len(line) > 0 and line[0]==":":
                break

            if is_uor_section:
                if len(line) < 9:
                    continue
                code = line[:9].strip()
                if code != "" and len(code) == 7:
                    uormap[code] = 1 
    return uormap


if __name__=="__main__":

    read_e()




