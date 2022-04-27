import unittest
from drgpy.msdrg import DRGEngine

class TestMCD16(unittest.TestCase):

    def test_mdcs16_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z9481"], ["07CP0ZZ"])
        self.assertTrue("801" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9481"], ["02LV4DZ"])
        self.assertTrue("804" in drg_lst)

        drg_lst = de.get_drg_all(["D592"], [])
        self.assertTrue("810" in drg_lst)

        drg_lst = de.get_drg_all(["D4620"], [])
        self.assertTrue("812" in drg_lst)

        drg_lst = de.get_drg_all(["D65"], [])
        self.assertTrue("813" in drg_lst)

        drg_lst = de.get_drg_all(["A182"], [])
        self.assertTrue("816" in drg_lst)

    def test_mdcs16_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z9481"], ["07CP0ZZ"])
        self.assertTrue("801" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9481"], ["02LV4DZ"])
        self.assertTrue("804" in drg_lst)

        drg_lst = de.get_drg_all(["D592"], [])
        self.assertTrue("810" in drg_lst)

        drg_lst = de.get_drg_all(["D4620"], [])
        self.assertTrue("812" in drg_lst)

        drg_lst = de.get_drg_all(["D65"], [])
        self.assertTrue("813" in drg_lst)

        drg_lst = de.get_drg_all(["A182"], [])
        self.assertTrue("816" in drg_lst)


if __name__=="__main__":
    unittest.main()




