import unittest
from drgpy.msdrg import DRGEngine

class TestMCD18(unittest.TestCase):

    def test_mdcs18_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["N980"], ["00BF0ZZ"])
        self.assertTrue("858" not in drg_lst) # No OR Proc for 858
 
        drg_lst = de.get_drg_all(["Z21"], ["00BF0ZZ"])
        self.assertTrue("855" not in drg_lst) # No OR Proc for 855
 
        drg_lst = de.get_drg_all(["K6811"], [])
        self.assertTrue("863" in drg_lst)
 
        drg_lst = de.get_drg_all(["R502"], [])
        self.assertTrue("864" in drg_lst)
 
        drg_lst = de.get_drg_all(["A70"], [])
        self.assertTrue("866" in drg_lst)
 
        drg_lst = de.get_drg_all(["A0100"], [])
        self.assertTrue("869" in drg_lst)
 
        drg_lst = de.get_drg_all(["A021"], ["5A1955Z"])
        self.assertTrue("870" in drg_lst) # mechanical ventilation
        
        drg_lst = de.get_drg_all(["A021", "E0800"], [])
        self.assertTrue("871" in drg_lst)

    def test_mdcs18_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["N980"], ["00BF0ZZ"])
        self.assertTrue("858" not in drg_lst) # No OR Proc for 858
 
        drg_lst = de.get_drg_all(["Z21"], ["00BF0ZZ"])
        self.assertTrue("855" not in drg_lst) # No OR Proc for 855
 
        drg_lst = de.get_drg_all(["K6811"], [])
        self.assertTrue("863" in drg_lst)
 
        drg_lst = de.get_drg_all(["R502"], [])
        self.assertTrue("864" in drg_lst)
 
        drg_lst = de.get_drg_all(["A70"], [])
        self.assertTrue("866" in drg_lst)
 
        drg_lst = de.get_drg_all(["A0100"], [])
        self.assertTrue("869" in drg_lst)
 
        drg_lst = de.get_drg_all(["A021"], ["5A1955Z"])
        self.assertTrue("870" in drg_lst) # mechanical ventilation
        
        drg_lst = de.get_drg_all(["A021", "E0800"], [])
        self.assertTrue("871" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




