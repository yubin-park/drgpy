import unittest
from drgpy.msdrg import DRGEngine

class TestMCD01(unittest.TestCase):

    def test_mdcs01(self):

        de = DRGEngine()

        drg_lst = de.get_drg_all(["I6000", "E0800"], ["031H09G"])
        self.assertTrue("020" in drg_lst)
        drg_lst = de.get_drg_all(["I6000", "E060"], ["031H09G"])
        self.assertTrue("021" in drg_lst)
        drg_lst = de.get_drg_all(["I6000"], ["031H09G"])
        self.assertTrue("022" in drg_lst)

        drg_lst = de.get_drg_all(["I6000", "E0800"], 
                                ["001607B", "0JH60DZ", "0JH60DZ"])
        self.assertTrue("023" in drg_lst)
        drg_lst = de.get_drg_all(["I6000", "E0800", "A066"], [])
        self.assertTrue("023" in drg_lst)
        drg_lst = de.get_drg_all(["I6000"], ["00H004Z"])
        self.assertTrue("023" in drg_lst)
        drg_lst = de.get_drg_all(["G40001"], 
                                ["0NH00NZ", "00H00MZ"])
        self.assertTrue("023" in drg_lst)
        drg_lst = de.get_drg_all(["I6000"], 
                                ["001607B", "0JH60DZ", "0JH60DZ"])
        self.assertTrue("024" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["009B0ZZ"])
        self.assertTrue("027" in drg_lst)
        drg_lst = de.get_drg_all(["G40001", "E0800"], ["009B0ZZ"])
        self.assertTrue("025" in drg_lst)
        drg_lst = de.get_drg_all(["G40001", "E060"], ["009B0ZZ"])
        self.assertTrue("026" in drg_lst)
        
        drg_lst = de.get_drg_all(["G40001", "E0800"], ["001U072"])
        self.assertTrue("028" in drg_lst)
        drg_lst = de.get_drg_all(["G40001", "E060"], ["001U072"])
        self.assertTrue("029" in drg_lst)
        drg_lst = de.get_drg_all(["G40001"], 
                        ["001U072", "0JH60BZ", "00HU0MZ"])
        self.assertTrue("029" in drg_lst)
        drg_lst = de.get_drg_all(["G40001"], ["001U072"])
        self.assertTrue("030" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["0016070"])
        self.assertTrue("033" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["037H3D6"])
        self.assertTrue("036" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["021W08B"])
        self.assertTrue("039" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["008F0ZZ"])
        self.assertTrue("042" in drg_lst)
        drg_lst = de.get_drg_all(["G40001"], 
                        ["008F0ZZ", "0JH60BZ", "00HE0MZ"])
        self.assertTrue("041" in drg_lst)



if __name__=="__main__":
    unittest.main()




