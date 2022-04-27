import unittest
from drgpy.msdrg import DRGEngine

class TestMCD11(unittest.TestCase):

    def test_mdcs11_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["A1810"], ["0TY00Z2"])
        self.assertTrue("652" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], ["0T1B0KC"])
        self.assertTrue("655" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], ["0410095"])
        self.assertTrue("661" in drg_lst)
        drg_lst = de.get_drg_all(["C676"], ["0410095"])
        self.assertTrue("658" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], ["0T5B0ZZ"])
        self.assertTrue("664" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["0VT07ZZ"])
        self.assertTrue("667" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["0TBB7ZX"])
        self.assertTrue("670" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["0THDX2Z"])
        self.assertTrue("672" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["02HV3DZ"])
        self.assertTrue("675" in drg_lst)
        drg_lst = de.get_drg_all(["E883"], ["0JH80XZ"])
        self.assertTrue("675" in drg_lst)
        drg_lst = de.get_drg_all(["E883"], ["3E0J7U0"])
        self.assertTrue("675" not in drg_lst)
        drg_lst = de.get_drg_all(["E1021"], ["3E0J7U0"])
        self.assertTrue("675" in drg_lst)

        drg_lst = de.get_drg_all(["R34"], [])
        self.assertTrue("684" in drg_lst)

        drg_lst = de.get_drg_all(["D090"], [])
        self.assertTrue("688" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], [])
        self.assertTrue("690" in drg_lst)

        # 692 is removed in v37
        #drg_lst = de.get_drg_all(["N200"], ["0TF7XZZ"])
        #self.assertTrue("692" in drg_lst)
        drg_lst = de.get_drg_all(["N200"], [])
        self.assertTrue("694" in drg_lst)
        drg_lst = de.get_drg_all(["N200", "E0800"], [])
        self.assertTrue("693" in drg_lst)

        drg_lst = de.get_drg_all(["R32"], [])
        self.assertTrue("696" in drg_lst)
 
        drg_lst = de.get_drg_all(["N37"], [])
        self.assertTrue("697" in drg_lst)
 
        drg_lst = de.get_drg_all(["I722"], [])
        self.assertTrue("700" in drg_lst)

    def test_mdcs11_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["A1810"], ["0TY00Z2"])
        self.assertTrue("652" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], ["0T1B0KC"])
        self.assertTrue("655" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], ["0410095"])
        self.assertTrue("661" in drg_lst)
        drg_lst = de.get_drg_all(["C676"], ["0410095"])
        self.assertTrue("658" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], ["0T5B0ZZ"])
        self.assertTrue("664" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["0VT07ZZ"])
        self.assertTrue("667" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["0TBB7ZX"])
        self.assertTrue("670" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["0THDX2Z"])
        self.assertTrue("672" in drg_lst)
 
        drg_lst = de.get_drg_all(["A1810"], ["02HV3DZ"])
        self.assertTrue("675" in drg_lst)
        drg_lst = de.get_drg_all(["E883"], ["0JH80XZ"])
        self.assertTrue("675" in drg_lst)
        drg_lst = de.get_drg_all(["E883"], ["3E0J7U0"])
        self.assertTrue("675" not in drg_lst)
        drg_lst = de.get_drg_all(["E1021"], ["3E0J7U0"])
        self.assertTrue("675" in drg_lst)

        drg_lst = de.get_drg_all(["R34"], [])
        self.assertTrue("684" in drg_lst)

        drg_lst = de.get_drg_all(["D090"], [])
        self.assertTrue("688" in drg_lst)

        drg_lst = de.get_drg_all(["A1810"], [])
        self.assertTrue("690" in drg_lst)

        # 692 is removed in v37
        #drg_lst = de.get_drg_all(["N200"], ["0TF7XZZ"])
        #self.assertTrue("692" in drg_lst)
        drg_lst = de.get_drg_all(["N200"], [])
        self.assertTrue("694" in drg_lst)
        drg_lst = de.get_drg_all(["N200", "E0800"], [])
        self.assertTrue("693" in drg_lst)

        drg_lst = de.get_drg_all(["R32"], [])
        self.assertTrue("696" in drg_lst)
 
        drg_lst = de.get_drg_all(["N37"], [])
        self.assertTrue("697" in drg_lst)
 
        drg_lst = de.get_drg_all(["I722"], [])
        self.assertTrue("700" in drg_lst)
 


if __name__=="__main__":
    unittest.main()




