import unittest
from drgpy.msdrg import DRGEngine

class TestMCD22(unittest.TestCase):

    def test_mdcs22_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["T3121"], ["5A1955Z"])
        self.assertTrue("933" in drg_lst)
        drg_lst = de.get_drg_all(["T3121"], ["5A1955Z", "0HR0X73"])
        self.assertTrue("927" in drg_lst)
 
        drg_lst = de.get_drg_all(["T2030XA"], [])
        self.assertTrue("934" in drg_lst)
        drg_lst = de.get_drg_all(["T2030XA", "J705", "E0800"], [])
        self.assertTrue("928" in drg_lst)
        drg_lst = de.get_drg_all(["T2030XA"], ["0HR0X73"])
        self.assertTrue("929" in drg_lst)
 
        drg_lst = de.get_drg_all(["T2000XA"], [])
        self.assertTrue("935" in drg_lst)

    def test_mdcs22_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["T3121"], ["5A1955Z"])
        self.assertTrue("933" in drg_lst)
        drg_lst = de.get_drg_all(["T3121"], ["5A1955Z", "0HR0X73"])
        self.assertTrue("927" in drg_lst)
 
        drg_lst = de.get_drg_all(["T2030XA"], [])
        self.assertTrue("934" in drg_lst)
        drg_lst = de.get_drg_all(["T2030XA", "J705", "E0800"], [])
        self.assertTrue("928" in drg_lst)
        drg_lst = de.get_drg_all(["T2030XA"], ["0HR0X73"])
        self.assertTrue("929" in drg_lst)
 
        drg_lst = de.get_drg_all(["T2000XA"], [])
        self.assertTrue("935" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




