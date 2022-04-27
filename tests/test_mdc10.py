import unittest
from drgpy.msdrg import DRGEngine

class TestMCD10(unittest.TestCase):

    def test_mdcs10_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z6845"], ["0Y6X0Z3"])
        self.assertTrue("618" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["0D160JA"])
        self.assertTrue("621" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["06LB3ZZ"])
        self.assertTrue("615" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["0HR0XK4"])
        self.assertTrue("624" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["0G5G3ZZ"])
        self.assertTrue("627" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["02LV3ZZ"])
        self.assertTrue("630" in drg_lst)
        drg_lst = de.get_drg_all(["Z6845"], ["0SP908Z", "0SRR01A"])
        self.assertTrue("630" in drg_lst)

        drg_lst = de.get_drg_all(["E08638"], [])
        self.assertTrue("639" in drg_lst)

        drg_lst = de.get_drg_all(["E41"], [])
        self.assertTrue("641" in drg_lst)

        drg_lst = de.get_drg_all(["E70318"], [])
        self.assertTrue("642" in drg_lst)

        drg_lst = de.get_drg_all(["C7400"], [])
        self.assertTrue("645" in drg_lst)

    def test_mdcs10_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z6845"], ["0Y6X0Z3"])
        self.assertTrue("618" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["0D160JA"])
        self.assertTrue("621" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["06LB3ZZ"])
        self.assertTrue("615" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["0HR0XK4"])
        self.assertTrue("624" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["0G5G3ZZ"])
        self.assertTrue("627" in drg_lst)

        drg_lst = de.get_drg_all(["Z6845"], ["02LV3ZZ"])
        self.assertTrue("630" in drg_lst)
        drg_lst = de.get_drg_all(["Z6845"], ["0SP908Z", "0SRR01A"])
        self.assertTrue("630" in drg_lst)

        drg_lst = de.get_drg_all(["E08638"], [])
        self.assertTrue("639" in drg_lst)

        drg_lst = de.get_drg_all(["E41"], [])
        self.assertTrue("641" in drg_lst)

        drg_lst = de.get_drg_all(["E70318"], [])
        self.assertTrue("642" in drg_lst)

        drg_lst = de.get_drg_all(["C7400"], [])
        self.assertTrue("645" in drg_lst)

if __name__=="__main__":
    unittest.main()




