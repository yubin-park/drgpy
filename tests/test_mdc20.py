import unittest
from drgpy.msdrg import DRGEngine

class TestMCD20(unittest.TestCase):

    def test_mdcs20(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["R780"], ["HZ39ZZZ"])
        self.assertTrue("895" in drg_lst)
 
 
if __name__=="__main__":
    unittest.main()




