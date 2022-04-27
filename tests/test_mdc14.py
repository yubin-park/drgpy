import unittest
from drgpy.msdrg import DRGEngine

class TestMCD14(unittest.TestCase):

    def test_mdcs14_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0"])
        self.assertTrue("785" not in drg_lst)
        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0", "0UB67ZZ"])
        self.assertTrue("785" in drg_lst)

        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0"])
        self.assertTrue("788" in drg_lst)
        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0", "0UB50ZZ"])
        self.assertTrue("788" not in drg_lst)
 
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D17Z9"])
        self.assertTrue("768" in drg_lst)
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D07Z3", "0KQM0ZZ"])
        self.assertTrue("768" not in drg_lst)
 
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D17Z9"])
        self.assertTrue("798" not in drg_lst)
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D17Z9", "0U573ZZ"])
        self.assertTrue("798" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z640"], ["10A00ZZ"])
        self.assertTrue("770" in drg_lst)
 
        drg_lst = de.get_drg_all(["O0000"], ["10A00ZZ"])
        self.assertTrue("819" not in drg_lst) # OR Procedure depends on DRG
 
        drg_lst = de.get_drg_all(["O0000", "Z370"], ["10D07Z3"])
        self.assertTrue("807" in drg_lst)
 
        drg_lst = de.get_drg_all(["O021"], [])
        self.assertTrue("779" in drg_lst)
 
        drg_lst = de.get_drg_all(["O0000"], [])
        self.assertTrue("833" in drg_lst)

        drg_lst = de.get_drg_all(["A34"], [])
        self.assertTrue("776" in drg_lst)
 
        drg_lst = de.get_drg_all(["O021"], [])
        self.assertTrue("779" in drg_lst)
 
        drg_lst = de.get_drg_all(["O0911"], [])
        self.assertTrue("998" in drg_lst)

    def test_mdcs14_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0"])
        self.assertTrue("785" not in drg_lst)
        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0", "0UB67ZZ"])
        self.assertTrue("785" in drg_lst)

        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0"])
        self.assertTrue("788" in drg_lst)
        drg_lst = de.get_drg_all(["Z640"], ["10D00Z0", "0UB50ZZ"])
        self.assertTrue("788" not in drg_lst)
 
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D17Z9"])
        self.assertTrue("768" in drg_lst)
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D07Z3", "0KQM0ZZ"])
        self.assertTrue("768" not in drg_lst)
 
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D17Z9"])
        self.assertTrue("798" not in drg_lst)
        drg_lst = de.get_drg_all(["Z640", "Z370"], ["10D17Z9", "0U573ZZ"])
        self.assertTrue("798" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z640"], ["10A00ZZ"])
        self.assertTrue("770" in drg_lst)
 
        drg_lst = de.get_drg_all(["O0000"], ["10A00ZZ"])
        self.assertTrue("819" not in drg_lst) # OR Procedure depends on DRG
 
        drg_lst = de.get_drg_all(["O0000", "Z370"], ["10D07Z3"])
        self.assertTrue("807" in drg_lst)
 
        drg_lst = de.get_drg_all(["O021"], [])
        self.assertTrue("779" in drg_lst)
 
        drg_lst = de.get_drg_all(["O0000"], [])
        self.assertTrue("833" in drg_lst)

        drg_lst = de.get_drg_all(["A34"], [])
        self.assertTrue("776" in drg_lst)
 
        drg_lst = de.get_drg_all(["O021"], [])
        self.assertTrue("779" in drg_lst)
 
        drg_lst = de.get_drg_all(["O0911"], [])
        self.assertTrue("998" in drg_lst) 

if __name__=="__main__":
    unittest.main()




