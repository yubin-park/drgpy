import unittest
from drgpy.msdrg import DRGEngine

class TestMCD12(unittest.TestCase):

    def test_mdcs12_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z302"], ["07JP0ZZ"])
        self.assertTrue("708" in drg_lst)
        drg_lst = de.get_drg_all(["Z302"], ["0VT08ZZ", "0VT34ZZ"])
        self.assertTrue("708" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z302"], ["0TMD4ZZ"])
        self.assertTrue("710" in drg_lst)
         
        drg_lst = de.get_drg_all(["Z302"], ["0V1N0KK"])
        self.assertTrue("712" in drg_lst)

        drg_lst = de.get_drg_all(["Z302"], ["0V508ZZ"])
        self.assertTrue("714" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], ["DVY0KZZ"])
        self.assertTrue("716" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], [])
        self.assertTrue("724" in drg_lst)
 
        drg_lst = de.get_drg_all(["N400"], [])
        self.assertTrue("726" in drg_lst)
 
        drg_lst = de.get_drg_all(["A57"], [])
        self.assertTrue("728" in drg_lst)
 
        drg_lst = de.get_drg_all(["L293"], [])
        self.assertTrue("730" in drg_lst)

    def test_mdcs12_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z302"], ["07JP0ZZ"])
        self.assertTrue("708" in drg_lst)
        drg_lst = de.get_drg_all(["Z302"], ["0VT08ZZ", "0VT34ZZ"])
        self.assertTrue("708" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z302"], ["0TMD4ZZ"])
        self.assertTrue("710" in drg_lst)
         
        drg_lst = de.get_drg_all(["Z302"], ["0V1N0KK"])
        self.assertTrue("712" in drg_lst)

        drg_lst = de.get_drg_all(["Z302"], ["0V508ZZ"])
        self.assertTrue("714" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], ["DVY0KZZ"])
        self.assertTrue("716" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], [])
        self.assertTrue("724" in drg_lst)
 
        drg_lst = de.get_drg_all(["N400"], [])
        self.assertTrue("726" in drg_lst)
 
        drg_lst = de.get_drg_all(["A57"], [])
        self.assertTrue("728" in drg_lst)
 
        drg_lst = de.get_drg_all(["L293"], [])
        self.assertTrue("730" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




