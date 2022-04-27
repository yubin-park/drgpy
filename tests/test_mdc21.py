import unittest
from drgpy.msdrg import DRGEngine

class TestMCD21(unittest.TestCase):

    def test_mdcs21_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z041"], ["0JBB0ZZ"])
        self.assertTrue("903" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z041"], ["0HR1XJ3"])
        self.assertTrue("905" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z041"], ["0HRFX73"])
        self.assertTrue("906" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z041"], ["XRGD0F3"])
        self.assertTrue("909" in drg_lst)
 
        drg_lst = de.get_drg_all(["S0570XS"], [])
        self.assertTrue("914" in drg_lst)
 
        drg_lst = de.get_drg_all(["T7800XA"], [])
        self.assertTrue("916" in drg_lst)
 
        drg_lst = de.get_drg_all(["M1A10X1"], [])
        self.assertTrue("918" in drg_lst)
 
        drg_lst = de.get_drg_all(["D47Z1"], [])
        self.assertTrue("921" in drg_lst)
 
        drg_lst = de.get_drg_all(["T3341XS"], [])
        self.assertTrue("923" in drg_lst)

    def test_mdcs21_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z041"], ["0JBB0ZZ"])
        self.assertTrue("903" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z041"], ["0HR1XJ3"])
        self.assertTrue("905" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z041"], ["0HRFX73"])
        self.assertTrue("906" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z041"], ["XRGD0F3"])
        self.assertTrue("909" in drg_lst)
 
        drg_lst = de.get_drg_all(["S0570XS"], [])
        self.assertTrue("914" in drg_lst)
 
        drg_lst = de.get_drg_all(["T7800XA"], [])
        self.assertTrue("916" in drg_lst)
 
        drg_lst = de.get_drg_all(["M1A10X1"], [])
        self.assertTrue("918" in drg_lst)
 
        drg_lst = de.get_drg_all(["D47Z1"], [])
        self.assertTrue("921" in drg_lst)
 
        drg_lst = de.get_drg_all(["T3341XS"], [])
        self.assertTrue("923" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




