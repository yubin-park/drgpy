import unittest
from drgpy.msdrg import DRGEngine

class TestMCD23(unittest.TestCase):

    def test_mdcs23(self):

        de = DRGEngine()

        drg_lst = de.get_drg_all(["Z9989"], ["00BF0ZZ"])
        self.assertTrue("941" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z448"], [])
        self.assertTrue("946" in drg_lst)
        drg_lst = de.get_drg_all(["Z4823"], ["F003GKZ"])
        self.assertTrue("946" not in drg_lst)
        drg_lst = de.get_drg_all(["Z9989"], ["F003GKZ"])
        self.assertTrue("946" in drg_lst)
 
        drg_lst = de.get_drg_all(["E790"], [])
        self.assertTrue("948" in drg_lst)

        drg_lst = de.get_drg_all(["S0001XD"], [])
        self.assertTrue("950" in drg_lst)
 
        drg_lst = de.get_drg_all(["F17200"], [])
        self.assertTrue("951" in drg_lst)
 

if __name__=="__main__":
    unittest.main()




