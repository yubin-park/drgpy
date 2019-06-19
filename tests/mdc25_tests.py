import unittest
from drgpy.msdrg import DRGEngine

class TestMCD25(unittest.TestCase):

    def test_mdcs25(self):

        de = DRGEngine()

        drg_lst = de.get_drg_all(["B20"], ["00BF0ZZ"])
        self.assertTrue("970" not in drg_lst)
        drg_lst = de.get_drg_all(["B20"], ["00BF0ZZ", "0016071"])
        self.assertTrue("970" in drg_lst)
 
        drg_lst = de.get_drg_all(["B20", "L081"], [])
        self.assertTrue("975" in drg_lst)
        drg_lst = de.get_drg_all(["B20"], [])
        self.assertTrue("977" in drg_lst)
 
 
if __name__=="__main__":
    unittest.main()




