
from drgpy.msdrg import DRGEngine

class DRGEngineAllVers:

    def __init__(self):
        self.de36 = DRGEngine(version="v36")
        self.de37 = DRGEngine(version="v37")
        self.de38 = DRGEngine(version="v38")
        self.de39 = DRGEngine(version="v39")
        self.de40 = DRGEngine(version="v40")

    def get_drg(self, dx_lst, pr_lst, date, gender="F", is_alive=True):
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
        """
         
        if date <= "2019-09-30":
            return self.de36.get_drg(dx_lst, pr_lst, gender, is_alive)
        elif date <= "2020-09-30":
            return self.de37.get_drg(dx_lst, pr_lst, gender, is_alive)
        elif date <= "2021-09-30":
            return self.de38.get_drg(dx_lst, pr_lst, gender, is_alive)
        elif date <= "2022-09-30":
            return self.de39.get_drg(dx_lst, pr_lst, gender, is_alive)
        else:
            return self.de40.get_drg(dx_lst, pr_lst, gender, is_alive)