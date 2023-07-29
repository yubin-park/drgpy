import unittest
from drgpy.msdrg import DRGEngine

class TestMCD00(unittest.TestCase):

    def test_mdcs00_v37(self):

        de = DRGEngine(version="v36")
        drg = de.get_drg(["O80","Z370","H6090","O691XX0",
                        "O700","O7182","Z3A39"],
                        ["0HQ9XZZ","10D07Z6","0UQMXZZ"])
        self.assertTrue(drg=="807") 
        drg = de.get_drg(["O80","Z370","H6090","O691XX0",
                        "O700","O7182","Z3A39"],
                        ["0HQ9XZZ","10D07Z6","0UQMXZZ", "0WQF0ZZ"])
        self.assertTrue(drg=="768") 

        drg = de.get_drg(["M47896","M48062","I2510","Z955",
                    "Z7902","E119","E785","I252","Z981",
                    "I10","Z7984","Z87891"],
                    ["0SB20ZZ","0SG00AJ"])
        self.assertTrue(drg=="460") 

        drg = de.get_drg(["T84060A","N029","M2170","Z96642","M461",
                    "D72829","K589","M26609","R208"],
                    ["0SR90JZ","0SP90JZ"])
        self.assertTrue(drg=="467")

        drg = de.get_drg(["T84060A","N029","M2170","Z96642","M461",
                    "D72829","K589","M26609","R208"],
                    ["0SWW4JZ", "0SP90JZ"])
        self.assertTrue(drg=="464")

if __name__=="__main__":
    unittest.main()




