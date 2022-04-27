import unittest
from drgpy.msdrg import DRGEngine

class TestMCD13(unittest.TestCase):

    def test_mdcs13_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["A57"], ["07T00ZZ"])
        self.assertTrue("735" in drg_lst)
        drg_lst = de.get_drg_all(["A57"], 
                ["0TTB0ZZ", "0TTD0ZZ", "0UT20ZZ", "0UT70ZZ", 
                    "0UT90ZZ", "0UTC0ZZ", "0UTG0ZZ"])
        self.assertTrue("735" in drg_lst)

        drg_lst = de.get_drg_all(["C561"], ["015P0ZZ"])
        self.assertTrue("738" in drg_lst)
        drg_lst = de.get_drg_all(["C510"], ["015P0ZZ"])
        self.assertTrue("741" in drg_lst)

        drg_lst = de.get_drg_all(["A510"], ["0U15079"])
        self.assertTrue("743" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["0DJU4ZZ"])
        self.assertTrue("745" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["0U5C7ZZ"])
        self.assertTrue("747" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["0JQC0ZZ"])
        self.assertTrue("748" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["00HV4MZ"])
        self.assertTrue("750" in drg_lst)

        drg_lst = de.get_drg_all(["C55"], [])
        self.assertTrue("756" in drg_lst)

        drg_lst = de.get_drg_all(["A55"], [])
        self.assertTrue("759" in drg_lst)

        drg_lst = de.get_drg_all(["D250"], [])
        self.assertTrue("761" in drg_lst)

    def test_mdcs13_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["A57"], ["07T00ZZ"])
        self.assertTrue("735" in drg_lst)
        drg_lst = de.get_drg_all(["A57"], 
                ["0TTB0ZZ", "0TTD0ZZ", "0UT20ZZ", "0UT70ZZ", 
                    "0UT90ZZ", "0UTC0ZZ", "0UTG0ZZ"])
        self.assertTrue("735" in drg_lst)

        drg_lst = de.get_drg_all(["C561"], ["015P0ZZ"])
        self.assertTrue("738" in drg_lst)
        drg_lst = de.get_drg_all(["C510"], ["015P0ZZ"])
        self.assertTrue("741" in drg_lst)

        drg_lst = de.get_drg_all(["A510"], ["0U15079"])
        self.assertTrue("743" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["0DJU4ZZ"])
        self.assertTrue("745" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["0U5C7ZZ"])
        self.assertTrue("747" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["0JQC0ZZ"])
        self.assertTrue("748" in drg_lst)

        drg_lst = de.get_drg_all(["A57"], ["00HV4MZ"])
        self.assertTrue("750" in drg_lst)

        drg_lst = de.get_drg_all(["C55"], [])
        self.assertTrue("756" in drg_lst)

        drg_lst = de.get_drg_all(["A55"], [])
        self.assertTrue("759" in drg_lst)

        drg_lst = de.get_drg_all(["D250"], [])
        self.assertTrue("761" in drg_lst)

if __name__=="__main__":
    unittest.main()




