import unittest
from drgpy.msdrg import DRGEngine

class TestMCD19(unittest.TestCase):

    def test_mdcs19_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["R4582"], ["00BF0ZZ"])
        self.assertTrue("876" not in drg_lst) # No OR Proc for 876
 
        drg_lst = de.get_drg_all(["F05"], [])
        self.assertTrue("880" in drg_lst)
 
        drg_lst = de.get_drg_all(["F329"], [])
        self.assertTrue("881" in drg_lst)
 
        drg_lst = de.get_drg_all(["F4000"], [])
        self.assertTrue("882" in drg_lst)
 
        drg_lst = de.get_drg_all(["F21"], [])
        self.assertTrue("883" in drg_lst)
 
        drg_lst = de.get_drg_all(["F0150"], [])
        self.assertTrue("884" in drg_lst)
 
        drg_lst = de.get_drg_all(["F200"], [])
        self.assertTrue("885" in drg_lst)
 
        drg_lst = de.get_drg_all(["F631"], [])
        self.assertTrue("886" in drg_lst)
 
        drg_lst = de.get_drg_all(["F4489"], [])
        self.assertTrue("887" in drg_lst)

        drg_lst = de.get_drg_all(['T6591XA','F23'],[])
        self.assertTrue("918" in drg_lst)

    def test_mdcs19_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["R4582"], ["00BF0ZZ"])
        self.assertTrue("876" not in drg_lst) # No OR Proc for 876
 
        drg_lst = de.get_drg_all(["F05"], [])
        self.assertTrue("880" in drg_lst)
 
        drg_lst = de.get_drg_all(["F329"], [])
        self.assertTrue("881" in drg_lst)
 
        drg_lst = de.get_drg_all(["F4000"], [])
        self.assertTrue("882" in drg_lst)
 
        drg_lst = de.get_drg_all(["F21"], [])
        self.assertTrue("883" in drg_lst)
 
        drg_lst = de.get_drg_all(["F0150"], [])
        self.assertTrue("884" in drg_lst)
 
        drg_lst = de.get_drg_all(["F200"], [])
        self.assertTrue("885" in drg_lst)
 
        drg_lst = de.get_drg_all(["F631"], [])
        self.assertTrue("886" in drg_lst)
 
        drg_lst = de.get_drg_all(["F4489"], [])
        self.assertTrue("887" in drg_lst)

        drg_lst = de.get_drg_all(['T6591XA','F23'],[])
        self.assertTrue("918" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




