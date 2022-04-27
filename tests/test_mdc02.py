import unittest
from drgpy.msdrg import DRGEngine

class TestMCD02(unittest.TestCase):

    def test_mdcs02_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["H16021", "E0800"], ["08B00ZX"])
        self.assertTrue("113" in drg_lst)
        drg_lst = de.get_drg_all(["H16021"], ["08B00ZX"])
        self.assertTrue("114" in drg_lst)
       
        drg_lst = de.get_drg_all(["H16021"], ["039S0ZX"])
        self.assertTrue("115" in drg_lst)

        drg_lst = de.get_drg_all(["H16021"], ["08123J4"])
        self.assertTrue("117" in drg_lst)

        drg_lst = de.get_drg_all(["H4419"], [])
        self.assertTrue("122" in drg_lst)

        drg_lst = de.get_drg_all(["A3982"], [])
        self.assertTrue("123" in drg_lst)

        drg_lst = de.get_drg_all(["A1850"], [])
        self.assertTrue("125" in drg_lst)

    def test_mdcs02_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["H16021", "E0800"], ["08B00ZX"])
        self.assertTrue("113" in drg_lst)
        drg_lst = de.get_drg_all(["H16021"], ["08B00ZX"])
        self.assertTrue("114" in drg_lst)
       
        drg_lst = de.get_drg_all(["H16021"], ["039S0ZX"])
        self.assertTrue("115" in drg_lst)

        drg_lst = de.get_drg_all(["H16021"], ["08123J4"])
        self.assertTrue("117" in drg_lst)

        drg_lst = de.get_drg_all(["H4419"], [])
        self.assertTrue("122" in drg_lst)

        drg_lst = de.get_drg_all(["A3982"], [])
        self.assertTrue("123" in drg_lst)

        drg_lst = de.get_drg_all(["A1850"], [])
        self.assertTrue("125" in drg_lst)



if __name__=="__main__":
    unittest.main()




