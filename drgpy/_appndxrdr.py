import csv
import re
from dataclasses import dataclass

from drgpy._resources import open_text


@dataclass
class AppendixCData:
    ccmap: dict
    exmap: dict
    drg_exclusions: dict

def read_a(fn="data/appendix_A.txt"):
    drgmap = {}
    is_drg_section = False
    with open_text(fn) as fp:
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
    drg_exclusions = {}
    section = "intro"
    pdx_collection = None
    exclusion_drgs = ()
    cc_pattern = re.compile(
        r"^\s*([A-Z][A-Z0-9]{2,6})\s+(MCC|CC)(?:\s+(\d{2}))?\s+(\d{4}):"
    )
    code_pattern = re.compile(r"^\s*([A-Z][A-Z0-9]{2,6})(?:\s|$)")
    collection_pattern = re.compile(r"PDX collection\s+(\d{4})")
    drg_pattern = re.compile(r"^(?:MDC \d+ )?DRGs?\s+(\d{3})(?:-(\d{3}))?")

    with open_text(fn) as fp:
        for line in fp:
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.startswith("Appendix C Part 2:"):
                section = "alive"
                pdx_collection = None
                continue
            if (stripped.startswith("Appendix C Part 3:") or
                    stripped == "Secondary Diagnosis CC/MCC Severity Exclusions in Select MS-DRGs"):
                section = "drg_exclusions"
                pdx_collection = None
                continue
            if "I10 Dx" in line and "Lev" in line:
                section = "cc"
                continue

            collection_match = collection_pattern.search(line)
            if collection_match and section in {"cc", "pdx_exclusions"}:
                section = "pdx_exclusions"
                pdx_collection = collection_match.group(1)
                exmap.setdefault(pdx_collection, set())
                continue

            if section == "cc":
                match = cc_pattern.match(line)
                if match:
                    dx, level, hac, pdx_collection_code = match.groups()
                    ccmap[dx] = {
                        "pdx": pdx_collection_code,
                        "level": level,
                        "hac": hac,
                        "aowa": False,
                    }
            elif section == "pdx_exclusions" and pdx_collection:
                match = code_pattern.match(line)
                if match:
                    exmap[pdx_collection].add(match.group(1))
            elif section == "alive":
                match = code_pattern.match(line)
                if match and match.group(1) in ccmap:
                    ccmap[match.group(1)]["aowa"] = True
            elif section == "drg_exclusions":
                drg_match = drg_pattern.match(stripped)
                if drg_match:
                    start = int(drg_match.group(1))
                    end = int(drg_match.group(2) or start)
                    exclusion_drgs = tuple(str(drg).zfill(3) for drg in range(start, end + 1))
                    for drg in exclusion_drgs:
                        drg_exclusions.setdefault(drg, set())
                    continue
                match = code_pattern.match(line)
                if match:
                    for drg in exclusion_drgs:
                        drg_exclusions[drg].add(match.group(1))

    return AppendixCData(ccmap, exmap, drg_exclusions)

def read_d(fn="data/appendix_D_E.txt"):
    rankmap = {}
    rank = 0
    is_rank_section = False
    with open_text(fn) as fp:
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
    with open_text(fn) as fp:
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

    oormap = {} # oor = Only Operating Room
    is_oor_section = False
    with open_text(fn) as fp:
        for line in fp:
            if "DRG 989 NON-EXTENSIVE O.R. PROCEDURE" in line.upper():
                is_oor_section = True
                continue
            elif is_oor_section and len(line) > 0 and line[0]==":":
                break

            if is_oor_section:
                if len(line) < 9:
                    continue
                code = line[:9].strip()
                if code != "" and len(code) == 7:
                    oormap[code] = 1 
    return oormap


if __name__=="__main__":

    read_e()


