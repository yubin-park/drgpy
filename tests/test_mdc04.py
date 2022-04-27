import unittest
from drgpy.msdrg import DRGEngine

class TestMCD04(unittest.TestCase):

    def test_mdcs04_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["T17820A"], ["025N0ZZ"])
        self.assertTrue("165" in drg_lst)

        drg_lst = de.get_drg_all(["T17820A"], ["008Q0ZZ"])
        self.assertTrue("168" in drg_lst)

        drg_lst = de.get_drg_all(["T17820A"], ["5A1522G"])
        # used to be 207, changed to 206 in v37
        self.assertTrue("206" in drg_lst)
        drg_lst = de.get_drg_all(["T17820A"], ["5A1955Z"])
        self.assertTrue("207" in drg_lst)
        drg_lst = de.get_drg_all(["T17820A"], ["5A1935Z"])
        self.assertTrue("208" in drg_lst)

        drg_lst = de.get_drg_all(["I2601"], [])
        # used to be 176, now 175 in v37
        self.assertTrue("175" in drg_lst)

        drg_lst = de.get_drg_all(["A0222", "A202"], [])
        self.assertTrue("177" in drg_lst)

        drg_lst = de.get_drg_all(["J1000"], [])
        self.assertTrue("179" not in drg_lst)
        drg_lst = de.get_drg_all(["J1000", "A481"], [])
        self.assertTrue("179" in drg_lst)
        drg_lst = de.get_drg_all(["A0222"], [])
        self.assertTrue("179" in drg_lst)

        drg_lst = de.get_drg_all(["C33"], [])
        self.assertTrue("182" in drg_lst)

        drg_lst = de.get_drg_all(["M9918"], [])
        self.assertTrue("185" in drg_lst)

        drg_lst = de.get_drg_all(["J90"], [])
        self.assertTrue("188" in drg_lst)

        drg_lst = de.get_drg_all(["J182"], [])
        self.assertTrue("189" in drg_lst)

        drg_lst = de.get_drg_all(["J411"], [])
        self.assertTrue("192" in drg_lst)

        drg_lst = de.get_drg_all(["B330"], [])
        self.assertTrue("195" in drg_lst)
        drg_lst = de.get_drg_all(["B330", "E0800"], [])
        self.assertTrue("193" in drg_lst)

        drg_lst = de.get_drg_all(["B4481"], [])
        self.assertTrue("198" in drg_lst)

        drg_lst = de.get_drg_all(["J930"], [])
        self.assertTrue("201" in drg_lst)
        drg_lst = de.get_drg_all(["J930", "E0800"], [])
        self.assertTrue("199" in drg_lst)

        drg_lst = de.get_drg_all(["A3700"], [])
        self.assertTrue("203" in drg_lst)

        drg_lst = de.get_drg_all(["G4732"], [])
        self.assertTrue("204" in drg_lst)

        drg_lst = de.get_drg_all(["E662"], [])
        self.assertTrue("206" in drg_lst)

    def test_mdcs04_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["T17820A"], ["025N0ZZ"])
        self.assertTrue("165" in drg_lst)

        drg_lst = de.get_drg_all(["T17820A"], ["008Q0ZZ"])
        self.assertTrue("168" in drg_lst)

        drg_lst = de.get_drg_all(["T17820A"], ["5A1522G"])
        # used to be 207, changed to 206 in v37
        self.assertTrue("206" in drg_lst)
        drg_lst = de.get_drg_all(["T17820A"], ["5A1955Z"])
        self.assertTrue("207" in drg_lst)
        drg_lst = de.get_drg_all(["T17820A"], ["5A1935Z"])
        self.assertTrue("208" in drg_lst)

        drg_lst = de.get_drg_all(["I2601"], [])
        self.assertTrue("175" in drg_lst)

        drg_lst = de.get_drg_all(["A0222", "A202"], [])
        self.assertTrue("177" in drg_lst)

        drg_lst = de.get_drg_all(["J1000"], [])
        self.assertTrue("179" not in drg_lst)
        drg_lst = de.get_drg_all(["J1000", "A481"], [])
        self.assertTrue("179" in drg_lst)
        drg_lst = de.get_drg_all(["A0222"], [])
        self.assertTrue("179" in drg_lst)

        drg_lst = de.get_drg_all(["C33"], [])
        self.assertTrue("182" in drg_lst)

        drg_lst = de.get_drg_all(["M9918"], [])
        self.assertTrue("185" in drg_lst)

        drg_lst = de.get_drg_all(["J90"], [])
        self.assertTrue("188" in drg_lst)

        drg_lst = de.get_drg_all(["J182"], [])
        self.assertTrue("189" in drg_lst)

        drg_lst = de.get_drg_all(["J411"], [])
        self.assertTrue("192" in drg_lst)

        drg_lst = de.get_drg_all(["B330"], [])
        self.assertTrue("195" in drg_lst)
        drg_lst = de.get_drg_all(["B330", "E0800"], [])
        self.assertTrue("193" in drg_lst)

        drg_lst = de.get_drg_all(["B4481"], [])
        self.assertTrue("198" in drg_lst)

        drg_lst = de.get_drg_all(["J930"], [])
        self.assertTrue("201" in drg_lst)
        drg_lst = de.get_drg_all(["J930", "E0800"], [])
        self.assertTrue("199" in drg_lst)

        drg_lst = de.get_drg_all(["A3700"], [])
        self.assertTrue("203" in drg_lst)

        drg_lst = de.get_drg_all(["G4732"], [])
        self.assertTrue("204" in drg_lst)

        drg_lst = de.get_drg_all(["E662"], [])
        self.assertTrue("206" in drg_lst)

if __name__=="__main__":
    unittest.main()




