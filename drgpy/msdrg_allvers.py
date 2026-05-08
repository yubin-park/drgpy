from drgpy.msdrg import DRGEngine


class DRGEngineAllVers:
    def __init__(self):
        self.de36 = DRGEngine(version="v36")
        self.de37 = DRGEngine(version="v37")
        self.de38 = DRGEngine(version="v38")
        self.de39 = DRGEngine(version="v39")
        self.de40 = DRGEngine(version="v40")
        self.de41 = DRGEngine(version="v41")
        self.de42 = DRGEngine(version="v42")
        self.de43 = DRGEngine(version="v43")

    def get_drg(self, dx_lst, pr_lst, date, gender="F", is_alive=True, poa_lst=None):
        """
        Return the corresponding DRG code for the diagnoses and procedures

        Parameters
        ----------
        dx_lst : list
                A list of ICD-10 diagnosis codes
        pr_lst : list
                A list of ICD-10 procedure codes
        date: str
                YYYY-MM-DD format
                Depending on the date of the claim,
                the engine will choose the appropriate version.
                e.g. date between 2020-10-01 will use v39...
        gender: str
                "F" or "M"
        is_alive: boolean
                if the patient is alive at discharge (True)
        poa_lst : list of str, optional
                POA indicators parallel to dx_lst ("Y", "N", "U", "E", "W").
                Secondary diagnoses with poa="N" are excluded from CC/MCC credit.
        """
        if date <= "2019-09-30":
            return self.de36.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        elif date <= "2020-09-30":
            return self.de37.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        elif date <= "2021-09-30":
            return self.de38.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        elif date <= "2022-09-30":
            return self.de39.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        elif date <= "2023-09-30":
            return self.de40.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        elif date <= "2024-09-30":
            return self.de41.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        elif date <= "2025-09-30":
            return self.de42.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
        else:
            return self.de43.get_drg(dx_lst, pr_lst, gender, is_alive, poa_lst)
