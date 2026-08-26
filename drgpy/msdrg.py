
import drgpy._mdcs0007 as mdcs0007
import drgpy._mdcs0811 as mdcs0811
import drgpy._mdcs1221 as mdcs1221
import drgpy._mdcs2225 as mdcs2225
from collections import Counter
import re

from drgpy._runtime_data import load_runtime_data
from drgpy._versions import get_version

class DRGEngine:

    def __init__(self, version=None):
        version_info = get_version(version)
        version = version_info.name
        runtime_data = load_runtime_data(version)
        self.dxmap = runtime_data.dxmap
        self.prmap = runtime_data.prmap
        self.version = version
        self.version_info = version_info
        self.drgmap = runtime_data.drgmap
        self.ccmap = runtime_data.ccmap
        self.exmap = runtime_data.exmap
        self.drg_exclusions = runtime_data.drg_exclusions
        self.orpcsmap = runtime_data.orpcsmap
        self.surgical_rank = runtime_data.surgical_rank
        self.neoormap = runtime_data.neoormap

    def get_features(
            self,
            dx_lst,
            pr_lst,
            gender="F",
            is_alive=True,
            poa=None,
            discharge_status="01",
            severity_exclusions=None):

        def remove_dups(seq):
            seen = set()
            seen_add = seen.add
            return [x for x in seq if not (x in seen or seen_add(x))]

        x = [] # MDC, DRG, etc.
        dx_lst = remove_dups(list(dx_lst))
        pr_lst = remove_dups(list(pr_lst))
        severity_exclusions = severity_exclusions or set()
        if not isinstance(gender, str):
            raise ValueError("gender must be 'F' or 'M'")
        gender = gender.strip().upper()
        if gender not in {"F", "M"}:
            raise ValueError("gender must be 'F' or 'M'")

        def get_poa(index, dx):
            if poa is None:
                return "Y"
            if isinstance(poa, dict):
                return poa.get(dx, "Y").upper()
            if index < len(poa):
                return poa[index].upper()
            return "Y"
       
        if len(dx_lst) > 0:
            # dx_lst[0]: primary/principal diagnosis
            # dx_lst[1:]: secondary diagnoses
            pdx = dx_lst[0]
            if len(self.dxmap[pdx]) == 0:
                pdx = pdx[:-1] # generalize; maybe too specific
                dx_lst[0] = pdx

            mdc24_principal = False
            mdc24_sites_by_diagnosis = []
            for j, dx in enumerate(dx_lst):
                is_pdx = j==0
                labels = self.dxmap[dx]
                if is_pdx and "_MDC24_PDX" in labels:
                    mdc24_principal = True
                mdc24_sites = {
                    label.removeprefix("_TRAUMA24_SITE_")
                    for label in labels
                    if label.startswith("_TRAUMA24_SITE_")
                }
                if mdc24_sites:
                    mdc24_sites_by_diagnosis.append(mdc24_sites)

                for x_i in labels:
                    if is_pdx:
                        x.append(x_i)
                    elif "PDX OR SDX" in x_i:
                        x.append(x_i)
                    elif ("PDX" not in x_i and 
                        "_MDC" not in x_i):
                        x.append(x_i)

                if dx in self.ccmap and not is_pdx:
                    cc_info = self.ccmap[dx]
                    excluded_by_pdx = pdx in self.exmap.get(cc_info["pdx"], set())
                    excluded_by_drg = dx in severity_exclusions
                    excluded_by_alive = cc_info["aowa"] and not is_alive
                    excluded_by_hac = (
                        cc_info.get("hac") is not None and
                        get_poa(j, dx) in {"N", "U"}
                    )
                    if not any((excluded_by_pdx, excluded_by_drg,
                                excluded_by_alive, excluded_by_hac)):
                        x.append("_" + cc_info["level"])

            mdc24_sites = set().union(*mdc24_sites_by_diagnosis)
            if (
                mdc24_principal
                and len(mdc24_sites_by_diagnosis) >= 2
                and len(mdc24_sites) >= 2
            ):
                x.append("_MDC24")

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
                x.append("_ORPCS_UNIQUE")
                for matched_drg in self.orpcsmap[pr]:
                    x.append(f"_ORPCS|{matched_drg}")
                    x.append("_ORPCS_ANY")
                if pr in self.neoormap:
                    x.append("_ORPCS_NON_EXTENSIVE")
                else:
                    x.append("_ORPCS_EXTENSIVE")

        if gender == "F":
            x.append("_FEMALE")
        else:
            x.append("_MALE")

        if is_alive:
            x.append("_ALIVE")
        
        if len(dx_lst) == 1:
            x.append("_NDX1")
        elif len(dx_lst) > 1:
            x.append("_NDX2+")
        x.append(f"_STATUS{discharge_status}")
        
        return Counter(x)

    def _evaluate(self, x):
        pre_mdc_results = mdcs0007.mdc00(x)
        major_version = self.version_info.major
        mdc_results = []
        mdc_results += mdcs0007.mdc01(x, major_version)
        mdc_results += mdcs0007.mdc02(x)
        mdc_results += mdcs0007.mdc03(x)
        mdc_results += mdcs0007.mdc04(x, major_version)
        mdc_results += mdcs0007.mdc05(x, major_version)
        mdc_results += mdcs0007.mdc06(x, major_version)
        mdc_results += mdcs0007.mdc07(x)
        mdc_results += mdcs0811.mdc08(x, major_version)
        mdc_results += mdcs0811.mdc09(x)
        mdc_results += mdcs0811.mdc10(x)
        mdc_results += mdcs0811.mdc11(x)
        mdc_results += mdcs1221.mdc12(x)
        mdc_results += mdcs1221.mdc13(x)
        mdc_results += mdcs1221.mdc14(x, major_version)
        mdc_results += mdcs1221.mdc15(x)
        mdc_results += mdcs1221.mdc16(x)
        mdc_results += mdcs1221.mdc17(x, major_version)
        mdc_results += mdcs1221.mdc18(x)
        mdc_results += mdcs1221.mdc19(x)
        mdc_results += mdcs1221.mdc20(x)
        mdc_results += mdcs1221.mdc21(x)
        mdc_results += mdcs2225.mdc22(x)
        mdc_results += mdcs2225.mdc23(x)
        mdc_results += mdcs2225.mdc25(x)

        mdc24_results = mdcs2225.mdc24(x)
        if pre_mdc_results:
            priority_results = pre_mdc_results
            remaining_results = mdc24_results + mdc_results
        elif mdc24_results:
            priority_results = mdc24_results
            remaining_results = mdc_results
        else:
            priority_results = mdc_results
            remaining_results = []

        has_related_surgical_result = any(
            self.drgmap.get(drg, {}).get("is_surgical", False)
            for drg in priority_results
        )
        excluded_delivery_orpcs = 0
        if x["_MDC14"] > 0:
            excluded_delivery_orpcs = x["768|WITH ANY ORPCS EXCEPT"]
        has_appendix_f_orpcs = (
            x["_ORPCS_UNIQUE"] > excluded_delivery_orpcs
        )
        if (
            not pre_mdc_results
            and not has_related_surgical_result
            and has_appendix_f_orpcs
        ):
            if x["_ORPCS_EXTENSIVE"] > 0:
                if x["_MCC"] > 0:
                    priority_results.insert(0, "981")
                elif x["_CC"] > 0:
                    priority_results.insert(0, "982")
                else:
                    priority_results.insert(0, "983")
            elif x["_ORPCS_NON_EXTENSIVE"] > 0:
                if x["_MCC"] > 0:
                    priority_results.insert(0, "987")
                elif x["_CC"] > 0:
                    priority_results.insert(0, "988")
                else:
                    priority_results.insert(0, "989")

        def sort_results(results):
            unique_results = list(dict.fromkeys(results))
            indexed_results = list(enumerate(unique_results))
            indexed_results.sort(
                key=lambda item: (
                    0 if self.drgmap.get(item[1], {}).get("is_surgical") else 1,
                    self.surgical_rank.get(
                        item[1],
                        self.surgical_rank.get(item[1].lstrip("0"), item[0]),
                    ),
                    item[0],
                )
            )
            return [drg for _, drg in indexed_results]

        ordered_results = sort_results(priority_results)
        ordered_results += sort_results(remaining_results)
        return list(dict.fromkeys(ordered_results))

    def get_drg_all(
            self,
            dx_lst,
            pr_lst,
            gender="F",
            is_alive=True,
            poa=None,
            discharge_status="01"):
        severity_exclusions = set()
        previous_drg = None

        for _ in range(3):
            features = self.get_features(
                dx_lst,
                pr_lst,
                gender,
                is_alive,
                poa,
                discharge_status,
                severity_exclusions,
            )
            results = self._evaluate(features)
            selected_drg = results[0] if results else None
            if selected_drg is None or selected_drg == previous_drg:
                return results
            previous_drg = selected_drg
            updated_exclusions = self.drg_exclusions.get(selected_drg, set())
            if updated_exclusions == severity_exclusions:
                return results
            severity_exclusions = updated_exclusions

        return results

    def get_drg(
            self,
            dx_lst,
            pr_lst,
            gender="F",
            is_alive=True,
            poa=None,
            discharge_status="01"):
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
        poa: list or dict, optional
                Present-on-admission indicators aligned with dx_lst or keyed
                by diagnosis code. Missing values default to "Y".
        discharge_status: str
                Two-character patient discharge status.
        """

        y_all = self.get_drg_all(
            dx_lst,
            pr_lst,
            gender,
            is_alive,
            poa,
            discharge_status,
        )
        y_all = y_all + ["000"]
        return y_all[0]

    def get_code_drg_candidates(self, code, code_type="diagnosis"):
        """Return DRGs directly referenced by a code's CMS value-set mappings."""
        if code_type not in {"diagnosis", "procedure"}:
            raise ValueError("code_type must be 'diagnosis' or 'procedure'")

        code_map = self.dxmap if code_type == "diagnosis" else self.prmap
        lookup_code = code
        labels = code_map.get(lookup_code, [])
        if code_type == "diagnosis" and not labels and lookup_code:
            lookup_code = lookup_code[:-1]
            labels = code_map.get(lookup_code, [])

        candidates = set()
        for label in labels:
            prefix = label.split("|", 1)[0]
            candidates.update(re.findall(r"(?<!\d)\d{3}(?!\d)", prefix))

        if code_type == "procedure":
            candidates.update(self.orpcsmap.get(lookup_code, []))

        return sorted(candidates, key=int)

    def simulate_drg_permutations(
            self,
            dx_lst,
            pr_lst,
            gender="F",
            is_alive=True,
            poa=None,
            discharge_status="01"):
        """Group once for each diagnosis selected as the principal diagnosis."""
        original_diagnoses = list(dx_lst)
        diagnoses = list(dict.fromkeys(original_diagnoses))
        procedures = list(dict.fromkeys(pr_lst))

        if isinstance(poa, dict) or poa is None:
            poa_by_code = poa
        else:
            poa_by_code = {}
            for index, code in enumerate(original_diagnoses):
                if code not in poa_by_code:
                    poa_by_code[code] = poa[index] if index < len(poa) else "Y"

        principal_choices = diagnoses or [None]
        simulations = []
        for principal in principal_choices:
            if principal is None:
                ordered_diagnoses = []
            else:
                ordered_diagnoses = [principal] + [
                    code for code in diagnoses if code != principal
                ]

            if isinstance(poa_by_code, dict) and not isinstance(poa, dict):
                ordered_poa = [poa_by_code[code] for code in ordered_diagnoses]
            else:
                ordered_poa = poa_by_code

            matching_drgs = self.get_drg_all(
                ordered_diagnoses,
                procedures,
                gender,
                is_alive,
                ordered_poa,
                discharge_status,
            )
            selected_drg = matching_drgs[0] if matching_drgs else "000"
            simulations.append({
                "principal_diagnosis": principal,
                "secondary_diagnoses": ordered_diagnoses[1:],
                "procedures": procedures.copy(),
                "drg": selected_drg,
                "matching_drgs": matching_drgs,
            })

        return simulations

    def get_possible_drgs(
            self,
            dx_lst,
            pr_lst,
            gender="F",
            is_alive=True,
            poa=None,
            discharge_status="01"):
        """Return distinct selected DRGs across all principal-diagnosis choices."""
        simulations = self.simulate_drg_permutations(
            dx_lst,
            pr_lst,
            gender,
            is_alive,
            poa,
            discharge_status,
        )
        return sorted({result["drg"] for result in simulations}, key=int)

        
