import unittest
from drgpy.msdrg import DRGEngine

class TestMCD02(unittest.TestCase):

    def test_mdcs02(self):

        de = DRGEngine()

        drg_lst = de.get_drg_all(["I6000", "E0800"], ["031H09G"])
        self.assertTrue("020" in drg_lst)
       

if __name__=="__main__":
    unittest.main()




