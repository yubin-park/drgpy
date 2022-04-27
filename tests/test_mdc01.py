import unittest
from drgpy.msdrg import DRGEngine

class TestMCD01(unittest.TestCase):

    def test_mdcs01_v37(self):

        de = DRGEngine(version="v37")

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
        # used to be 036, now 101 in v37
        self.assertTrue("101" in drg_lst)

        drg_lst = de.get_drg_all(["I63232", "G8191"], ["03CL0ZZ"])
        self.assertTrue("038" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["021W08B"])
        self.assertTrue("039" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["008F0ZZ"])
        self.assertTrue("042" in drg_lst)
        drg_lst = de.get_drg_all(["G40001"], 
                        ["008F0ZZ", "0JH60BZ", "00HE0MZ"])
        self.assertTrue("041" in drg_lst)

        drg_lst = de.get_drg_all(["G041"], [])
        self.assertTrue("053" in drg_lst)

        drg_lst = de.get_drg_all(["C700"], [])
        self.assertTrue("055" in drg_lst)

        drg_lst = de.get_drg_all(["A5210"], [])
        self.assertTrue("057" in drg_lst)

        drg_lst = de.get_drg_all(["G110"], [])
        self.assertTrue("060" in drg_lst)

        drg_lst = de.get_drg_all(["G450"], ["3E03017"])
        self.assertTrue("063" in drg_lst)

        drg_lst = de.get_drg_all(["I6000", "A0222"], [])
        self.assertTrue("064" in drg_lst)

        drg_lst = de.get_drg_all(["I6000"], [])
        self.assertTrue("066" in drg_lst)

        drg_lst = de.get_drg_all(["I6000", "Z9282"], [])
        self.assertTrue("065" in drg_lst)

        drg_lst = de.get_drg_all(["G450"], [])
        self.assertTrue("069" in drg_lst)

        drg_lst = de.get_drg_all(["G3289"], [])
        self.assertTrue("072" in drg_lst)

        drg_lst = de.get_drg_all(["B020"], [])
        self.assertTrue("074" in drg_lst)

        drg_lst = de.get_drg_all(["A870"], [])
        self.assertTrue("076" in drg_lst)

        drg_lst = de.get_drg_all(["I674"], [])
        self.assertTrue("079" in drg_lst)

        drg_lst = de.get_drg_all(["E035"], [])
        self.assertTrue("081" in drg_lst)

        drg_lst = de.get_drg_all(["S061X3A"], [])
        self.assertTrue("084" in drg_lst)

        drg_lst = de.get_drg_all(["S020XXA"], [])
        self.assertTrue("087" in drg_lst)

        drg_lst = de.get_drg_all(["S060X0A"], [])
        self.assertTrue("090" in drg_lst)

        drg_lst = de.get_drg_all(["A881"], [])
        self.assertTrue("093" in drg_lst)

        drg_lst = de.get_drg_all(["A0221"], [])
        self.assertTrue("096" in drg_lst)

        drg_lst = de.get_drg_all(["A066"], [])
        self.assertTrue("099" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], [])
        self.assertTrue("101" in drg_lst)

        drg_lst = de.get_drg_all(["F0781"], [])
        self.assertTrue("103" in drg_lst)

    def test_mdcs01_v40(self):

        de = DRGEngine(version="v40")

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
        # used to be 036, now 101 in v37
        self.assertTrue("101" in drg_lst)

        drg_lst = de.get_drg_all(["I63232", "G8191"], ["03CL0ZZ"])
        self.assertTrue("038" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["021W08B"])
        self.assertTrue("039" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], ["008F0ZZ"])
        self.assertTrue("042" in drg_lst)
        drg_lst = de.get_drg_all(["G40001"], 
                        ["008F0ZZ", "0JH60BZ", "00HE0MZ"])
        self.assertTrue("041" in drg_lst)

        drg_lst = de.get_drg_all(["G041"], [])
        self.assertTrue("053" in drg_lst)

        drg_lst = de.get_drg_all(["C700"], [])
        self.assertTrue("055" in drg_lst)

        drg_lst = de.get_drg_all(["A5210"], [])
        self.assertTrue("057" in drg_lst)

        drg_lst = de.get_drg_all(["G110"], [])
        self.assertTrue("060" in drg_lst)

        drg_lst = de.get_drg_all(["G450"], ["3E03017"])
        self.assertTrue("063" in drg_lst)

        drg_lst = de.get_drg_all(["I6000", "A0222"], [])
        self.assertTrue("064" in drg_lst)

        drg_lst = de.get_drg_all(["I6000"], [])
        self.assertTrue("066" in drg_lst)

        drg_lst = de.get_drg_all(["I6000", "Z9282"], [])
        self.assertTrue("065" in drg_lst)

        drg_lst = de.get_drg_all(["G450"], [])
        self.assertTrue("069" in drg_lst)

        drg_lst = de.get_drg_all(["G3289"], [])
        self.assertTrue("072" in drg_lst)

        drg_lst = de.get_drg_all(["B020"], [])
        self.assertTrue("074" in drg_lst)

        drg_lst = de.get_drg_all(["A870"], [])
        self.assertTrue("076" in drg_lst)

        drg_lst = de.get_drg_all(["I674"], [])
        self.assertTrue("079" in drg_lst)

        drg_lst = de.get_drg_all(["E035"], [])
        self.assertTrue("081" in drg_lst)

        drg_lst = de.get_drg_all(["S061X3A"], [])
        self.assertTrue("084" in drg_lst)

        drg_lst = de.get_drg_all(["S020XXA"], [])
        self.assertTrue("087" in drg_lst)

        drg_lst = de.get_drg_all(["S060X0A"], [])
        self.assertTrue("090" in drg_lst)

        drg_lst = de.get_drg_all(["A881"], [])
        self.assertTrue("093" in drg_lst)

        drg_lst = de.get_drg_all(["A0221"], [])
        self.assertTrue("096" in drg_lst)

        drg_lst = de.get_drg_all(["A066"], [])
        self.assertTrue("099" in drg_lst)

        drg_lst = de.get_drg_all(["G40001"], [])
        self.assertTrue("101" in drg_lst)

        drg_lst = de.get_drg_all(["F0781"], [])
        self.assertTrue("103" in drg_lst)
       

if __name__=="__main__":
    unittest.main()




