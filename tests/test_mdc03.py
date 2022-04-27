import unittest
from drgpy.msdrg import DRGEngine

class TestMCD03(unittest.TestCase):

    def test_mdcs03_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["A690"], ["07T00ZZ"])
        self.assertTrue("130" in drg_lst)
        drg_lst = de.get_drg_all(["T753XXA"], ["07T00ZZ", "09HD05Z"])
        self.assertTrue("129" in drg_lst)

        drg_lst = de.get_drg_all(["T753XXA"], ["00J00ZZ"])
        self.assertTrue("132" in drg_lst)
 
        drg_lst = de.get_drg_all(["T753XXA"], ["008F0ZZ"])
        self.assertTrue("134" in drg_lst)
 
        drg_lst = de.get_drg_all(["T753XXA"], ["095B0ZZ"])
        self.assertTrue("136" in drg_lst)
 
        drg_lst = de.get_drg_all(["T753XXA"], ["0C00X7Z"])
        self.assertTrue("138" in drg_lst)

        drg_lst = de.get_drg_all(["T753XXA"], ["0C580ZZ"])
        self.assertTrue("139" in drg_lst)

        drg_lst = de.get_drg_all(["C000"], [])
        self.assertTrue("148" in drg_lst)

        drg_lst = de.get_drg_all(["H8101"], [])
        self.assertTrue("149" in drg_lst)

        drg_lst = de.get_drg_all(["R040"], [])
        self.assertTrue("151" in drg_lst)

        drg_lst = de.get_drg_all(["A545"], [])
        self.assertTrue("153" in drg_lst)

        drg_lst = de.get_drg_all(["A186"], [])
        self.assertTrue("156" in drg_lst)

        drg_lst = de.get_drg_all(["A690"], [])
        self.assertTrue("159" in drg_lst)

    def test_mdcs03_v40(self):

        de = DRGEngine(version="v40")

        # NOTE: These DRGs disappeared in v40
        #drg_lst = de.get_drg_all(["A690"], ["07T00ZZ"])
        #self.assertTrue("130" in drg_lst)
        #drg_lst = de.get_drg_all(["T753XXA"], ["07T00ZZ", "09HD05Z"])
        #self.assertTrue("129" in drg_lst)
        #drg_lst = de.get_drg_all(["T753XXA"], ["00J00ZZ"])
        #self.assertTrue("132" in drg_lst)
        #drg_lst = de.get_drg_all(["T753XXA"], ["008F0ZZ"])
        #self.assertTrue("134" in drg_lst)
 
        drg_lst = de.get_drg_all(["T753XXA"], ["095B0ZZ"])
        self.assertTrue("136" in drg_lst)
 
        drg_lst = de.get_drg_all(["T753XXA"], ["0C00X7Z"])
        self.assertTrue("138" in drg_lst)

        drg_lst = de.get_drg_all(["T753XXA"], ["0C580ZZ"])
        self.assertTrue("139" in drg_lst)

        drg_lst = de.get_drg_all(["C000"], [])
        self.assertTrue("148" in drg_lst)

        drg_lst = de.get_drg_all(["H8101"], [])
        self.assertTrue("149" in drg_lst)

        drg_lst = de.get_drg_all(["R040"], [])
        self.assertTrue("151" in drg_lst)

        drg_lst = de.get_drg_all(["A545"], [])
        self.assertTrue("153" in drg_lst)

        drg_lst = de.get_drg_all(["A186"], [])
        self.assertTrue("156" in drg_lst)

        drg_lst = de.get_drg_all(["A690"], [])
        self.assertTrue("159" in drg_lst)


if __name__=="__main__":
    unittest.main()




