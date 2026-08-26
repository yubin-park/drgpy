import unittest
from drgpy.msdrg import DRGEngine

class TestMCD24(unittest.TestCase):

    def test_mdcs24_v37(self):

        de = DRGEngine(version="v37")
        diagnoses = ["S062X0A", "S7400XA"]

        drg_lst = de.get_drg_all(diagnoses, ["001607B"])
        self.assertTrue("955" in drg_lst)
 
        drg_lst = de.get_drg_all(diagnoses, ["0L8J0ZZ"])
        self.assertTrue("956" in drg_lst)
 
        drg_lst = de.get_drg_all(diagnoses, ["XRGD0F3"])
        self.assertTrue("959" in drg_lst)

    def test_mdcs24_v40(self):

        de = DRGEngine(version="v40")
        diagnoses = ["S062X0A", "S7400XA"]

        drg_lst = de.get_drg_all(diagnoses, ["001607B"])
        self.assertTrue("955" in drg_lst)
 
        drg_lst = de.get_drg_all(diagnoses, ["0L8J0ZZ"])
        self.assertTrue("956" in drg_lst)
 
        drg_lst = de.get_drg_all(diagnoses, ["XRGD0F3"])
        self.assertTrue("959" in drg_lst)
 
if __name__=="__main__":
    unittest.main()


