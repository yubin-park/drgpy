import unittest
from drgpy.msdrg import DRGEngine

class TestMCD15(unittest.TestCase):

    def test_mdcs15_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["A33"], ["10D00Z0"])
        self.assertTrue("785" not in drg_lst)
 
        drg_lst = de.get_drg_all(["P003"], [])
        self.assertTrue("795" in drg_lst)
        drg_lst = de.get_drg_all(["P003", "J341"], [])
        self.assertTrue("795" in drg_lst)
        drg_lst = de.get_drg_all(["P003", "J341", "J340"], [])
        self.assertTrue("795" in drg_lst)

        drg_lst = de.get_drg_all(["P0701"], [])
        self.assertTrue("790" in drg_lst)
 
        drg_lst = de.get_drg_all(["P0700"], [])
        self.assertTrue("792" in drg_lst)
        drg_lst = de.get_drg_all(["P0700", "P034"], [])
        self.assertTrue("791" in drg_lst)
 
        drg_lst = de.get_drg_all(["P034"], [])
        self.assertTrue("793" in drg_lst)
 
        drg_lst = de.get_drg_all(["A33"], [])
        self.assertTrue("794" in drg_lst)

    def test_mdcs15_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["A33"], ["10D00Z0"])
        self.assertTrue("785" not in drg_lst)
 
        drg_lst = de.get_drg_all(["P003"], [])
        self.assertTrue("795" in drg_lst)
        drg_lst = de.get_drg_all(["P003", "J341"], [])
        self.assertTrue("795" in drg_lst)
        drg_lst = de.get_drg_all(["P003", "J341", "J340"], [])
        self.assertTrue("795" in drg_lst)

        drg_lst = de.get_drg_all(["P0701"], [])
        self.assertTrue("790" in drg_lst)
 
        # changed ICD10 codes in v40
        drg_lst = de.get_drg_all(["P0710"], [])
        self.assertTrue("792" in drg_lst)
        drg_lst = de.get_drg_all(["P0710", "P034"], [])
        self.assertTrue("791" in drg_lst)
 
        drg_lst = de.get_drg_all(["P034"], [])
        self.assertTrue("793" in drg_lst)
 
        drg_lst = de.get_drg_all(["A33"], [])
        self.assertTrue("794" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




