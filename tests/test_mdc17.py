import unittest
from drgpy.msdrg import DRGEngine

class TestMCD17(unittest.TestCase):

    def test_mdcs17_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["C261"], ["0016070"])
        self.assertTrue("822" in drg_lst)
 
        drg_lst = de.get_drg_all(["C261"], ["D020JZZ"])
        self.assertTrue("825" in drg_lst)
 
        drg_lst = de.get_drg_all(["C37"], ["00160JB"])
        self.assertTrue("828" in drg_lst)
 
        drg_lst = de.get_drg_all(["C37"], ["D021DZZ"])
        self.assertTrue("830" in drg_lst)
 
        drg_lst = de.get_drg_all(["C9242"], [])
        self.assertTrue("836" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z08", "C9100"], [])
        self.assertTrue("838" in drg_lst)
        drg_lst = de.get_drg_all(["Z08", "C9100", "E0800"], [])
        self.assertTrue("837" in drg_lst)
        drg_lst = de.get_drg_all(["Z08"], ["3E03002"])
        self.assertTrue("838" in drg_lst)

        drg_lst = de.get_drg_all(["C261"], [])
        self.assertTrue("842" in drg_lst)
 
        drg_lst = de.get_drg_all(["C37"], [])
        self.assertTrue("845" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z08"], [])
        self.assertTrue("848" in drg_lst)

        drg_lst = de.get_drg_all(["Z510"], [])
        self.assertTrue("849" in drg_lst)
 
    def test_mdcs17_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["C261"], ["0016070"])
        self.assertTrue("822" in drg_lst)
 
        drg_lst = de.get_drg_all(["C261"], ["D020JZZ"])
        self.assertTrue("825" in drg_lst)
 
        drg_lst = de.get_drg_all(["C37"], ["00160JB"])
        self.assertTrue("828" in drg_lst)
 
        drg_lst = de.get_drg_all(["C37"], ["D021DZZ"])
        self.assertTrue("830" in drg_lst)
 
        drg_lst = de.get_drg_all(["C9242"], [])
        self.assertTrue("836" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z08", "C9100"], [])
        self.assertTrue("838" in drg_lst)
        drg_lst = de.get_drg_all(["Z08", "C9100", "E0800"], [])
        self.assertTrue("837" in drg_lst)
        drg_lst = de.get_drg_all(["Z08"], ["3E03002"])
        self.assertTrue("838" in drg_lst)

        drg_lst = de.get_drg_all(["C261"], [])
        self.assertTrue("842" in drg_lst)
 
        drg_lst = de.get_drg_all(["C37"], [])
        self.assertTrue("845" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z08"], [])
        self.assertTrue("848" in drg_lst)

        drg_lst = de.get_drg_all(["Z510"], [])
        self.assertTrue("849" in drg_lst)


if __name__=="__main__":
    unittest.main()




