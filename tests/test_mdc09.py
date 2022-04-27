import unittest
from drgpy.msdrg import DRGEngine

class TestMCD09(unittest.TestCase):

    def test_mdcs09_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["L0211"], ["0HR0X73"])
        self.assertTrue("575" in drg_lst)
        drg_lst = de.get_drg_all(["L0211", "A000"], ["0HR0X73"])
        self.assertTrue("574" in drg_lst)
        drg_lst = de.get_drg_all(["Z411"], ["0HR0X73"])
        self.assertTrue("578" in drg_lst)

        drg_lst = de.get_drg_all(["Z411"], ["4A160BZ"])
        self.assertTrue("581" in drg_lst)

        drg_lst = de.get_drg_all(["C50022"], ["0H0V0JZ"])
        self.assertTrue("583" in drg_lst)

        drg_lst = de.get_drg_all(["Z411"], ["0H0T37Z"])
        self.assertTrue("585" in drg_lst)

        drg_lst = de.get_drg_all(["L89004"], [])
        self.assertTrue("594" in drg_lst)

        drg_lst = de.get_drg_all(["B029"], [])
        self.assertTrue("596" in drg_lst)

        drg_lst = de.get_drg_all(["C50429"], [])
        self.assertTrue("599" in drg_lst)

        drg_lst = de.get_drg_all(["N6012"], [])
        self.assertTrue("601" in drg_lst)

        drg_lst = de.get_drg_all(["L0109"], [])
        self.assertTrue("603" in drg_lst)

        drg_lst = de.get_drg_all(["S0001XA"], [])
        self.assertTrue("605" in drg_lst)

        drg_lst = de.get_drg_all(["A5131"], [])
        self.assertTrue("607" in drg_lst)

    def test_mdcs09_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["L0211"], ["0HR0X73"])
        self.assertTrue("575" in drg_lst)
        drg_lst = de.get_drg_all(["L0211", "A000"], ["0HR0X73"])
        self.assertTrue("574" in drg_lst)
        drg_lst = de.get_drg_all(["Z411"], ["0HR0X73"])
        self.assertTrue("578" in drg_lst)

        drg_lst = de.get_drg_all(["Z411"], ["4A160BZ"])
        self.assertTrue("581" in drg_lst)

        drg_lst = de.get_drg_all(["C50022"], ["0H0V0JZ"])
        self.assertTrue("583" in drg_lst)

        drg_lst = de.get_drg_all(["Z411"], ["0H0T37Z"])
        self.assertTrue("585" in drg_lst)

        drg_lst = de.get_drg_all(["L89004"], [])
        self.assertTrue("594" in drg_lst)

        drg_lst = de.get_drg_all(["B029"], [])
        self.assertTrue("596" in drg_lst)

        drg_lst = de.get_drg_all(["C50429"], [])
        self.assertTrue("599" in drg_lst)

        drg_lst = de.get_drg_all(["N6012"], [])
        self.assertTrue("601" in drg_lst)

        drg_lst = de.get_drg_all(["L0109"], [])
        self.assertTrue("603" in drg_lst)

        drg_lst = de.get_drg_all(["S0001XA"], [])
        self.assertTrue("605" in drg_lst)

        drg_lst = de.get_drg_all(["A5131"], [])
        self.assertTrue("607" in drg_lst)

if __name__=="__main__":
    unittest.main()




