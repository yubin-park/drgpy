import unittest
from drgpy.msdrg import DRGEngine

class TestMCD06(unittest.TestCase):

    def test_mdcs06_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z4659"], ["008Q0ZZ"])
        self.assertTrue("328" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0UQG4ZZ"])
        self.assertTrue("331" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659", "E0800"], ["0DPQ3LZ"])
        self.assertTrue("332" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0DN83ZZ"])
        self.assertTrue("337" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0D5J4ZZ"])
        self.assertTrue("343" in drg_lst)
        drg_lst = de.get_drg_all(["C181"], ["0D5J4ZZ"])
        self.assertTrue("340" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0D5A3ZZ"])
        self.assertTrue("346" in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0DQ80ZZ", "0WQFXZ2"])
        self.assertTrue("346" in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0DQ80ZZ"])
        self.assertTrue("346" not in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["065Y3ZC"])
        self.assertTrue("349" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z4659"], ["0YQA3ZZ"])
        self.assertTrue("352" in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0YQA3ZZ", "0DQU3ZZ"])
        self.assertTrue("355" not in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0DQU3ZZ"])
        self.assertTrue("355" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z4659"], ["02BX0ZZ"])
        self.assertTrue("358" in drg_lst)
 
        drg_lst = de.get_drg_all(["S27812A"], [])
        self.assertTrue("370" in drg_lst)
 
        drg_lst = de.get_drg_all(["B699"], [])
        self.assertTrue("373" in drg_lst)
 
        drg_lst = de.get_drg_all(["C172"], [])
        self.assertTrue("376" in drg_lst)
 
        drg_lst = de.get_drg_all(["K252"], [])
        self.assertTrue("379" in drg_lst)
 
        drg_lst = de.get_drg_all(["E164"], [])
        self.assertTrue("382" in drg_lst)
        drg_lst = de.get_drg_all(["K263", "E0800"], [])
        self.assertTrue("383" in drg_lst)

        drg_lst = de.get_drg_all(["K5000"], [])
        self.assertTrue("387" in drg_lst)
 
        drg_lst = de.get_drg_all(["K5652"], [])
        self.assertTrue("390" in drg_lst)
 
        drg_lst = de.get_drg_all(["A0832"], [])
        self.assertTrue("392" in drg_lst)
 
        drg_lst = de.get_drg_all(["D131"], [])
        self.assertTrue("395" in drg_lst)

    def test_mdcs06_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z4659"], ["008Q0ZZ"])
        self.assertTrue("328" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0UQG4ZZ"])
        self.assertTrue("331" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659", "E0800"], ["0DPQ3LZ"])
        self.assertTrue("332" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0DN83ZZ"])
        self.assertTrue("337" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0D5J4ZZ"])
        self.assertTrue("343" in drg_lst)
        drg_lst = de.get_drg_all(["C181"], ["0D5J4ZZ"])
        self.assertTrue("340" in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["0D5A3ZZ"])
        self.assertTrue("346" in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0DQ80ZZ", "0WQFXZ2"])
        self.assertTrue("346" in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0DQ80ZZ"])
        self.assertTrue("346" not in drg_lst)

        drg_lst = de.get_drg_all(["Z4659"], ["065Y3ZC"])
        self.assertTrue("349" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z4659"], ["0YQA3ZZ"])
        self.assertTrue("352" in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0YQA3ZZ", "0DQU3ZZ"])
        self.assertTrue("355" not in drg_lst)
        drg_lst = de.get_drg_all(["Z4659"], ["0DQU3ZZ"])
        self.assertTrue("355" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z4659"], ["02BX0ZZ"])
        self.assertTrue("358" in drg_lst)
 
        drg_lst = de.get_drg_all(["S27812A"], [])
        self.assertTrue("370" in drg_lst)
 
        drg_lst = de.get_drg_all(["B699"], [])
        self.assertTrue("373" in drg_lst)
 
        drg_lst = de.get_drg_all(["C172"], [])
        self.assertTrue("376" in drg_lst)
 
        drg_lst = de.get_drg_all(["K252"], [])
        self.assertTrue("379" in drg_lst)
 
        drg_lst = de.get_drg_all(["E164"], [])
        self.assertTrue("382" in drg_lst)
        drg_lst = de.get_drg_all(["K263", "E0800"], [])
        self.assertTrue("383" in drg_lst)

        drg_lst = de.get_drg_all(["K5000"], [])
        self.assertTrue("387" in drg_lst)
 
        drg_lst = de.get_drg_all(["K5652"], [])
        self.assertTrue("390" in drg_lst)
 
        drg_lst = de.get_drg_all(["A0832"], [])
        self.assertTrue("392" in drg_lst)
 
        drg_lst = de.get_drg_all(["D131"], [])
        self.assertTrue("395" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




