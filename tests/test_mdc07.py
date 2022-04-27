import unittest
from drgpy.msdrg import DRGEngine

class TestMCD07(unittest.TestCase):

    def test_mdcs07_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["S36240A"], ["06184JB"])
        self.assertTrue("407" in drg_lst)
 
        drg_lst = de.get_drg_all(["S36240A"], ["0F140D8"])
        self.assertTrue("410" in drg_lst)
    
        drg_lst = de.get_drg_all(["S36240A"], ["0F540ZZ", "0F9900Z"])
        self.assertTrue("413" in drg_lst)
        drg_lst = de.get_drg_all(["S36240A"], ["0F540ZZ", "0FB40ZZ"])
        self.assertTrue("416" in drg_lst)
        drg_lst = de.get_drg_all(["S36240A"], ["0FB44ZZ"])
        self.assertTrue("419" in drg_lst)
       
        drg_lst = de.get_drg_all(["S36240A"], ["07JP0ZZ"])
        self.assertTrue("422" in drg_lst)
 
        drg_lst = de.get_drg_all(["S36240A"], ["008X3ZZ"])
        self.assertTrue("425" in drg_lst)
 
        drg_lst = de.get_drg_all(["K7469"], [])
        self.assertTrue("434" in drg_lst)
 
        drg_lst = de.get_drg_all(["C220"], [])
        self.assertTrue("437" in drg_lst)
 
        drg_lst = de.get_drg_all(["B252"], [])
        self.assertTrue("440" in drg_lst)
 
        drg_lst = de.get_drg_all(["B182"], [])
        self.assertTrue("443" in drg_lst)
 
        drg_lst = de.get_drg_all(["K8000"], [])
        self.assertTrue("446" in drg_lst)

    def test_mdcs07_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["S36240A"], ["06184JB"])
        self.assertTrue("407" in drg_lst)
 
        drg_lst = de.get_drg_all(["S36240A"], ["0F140D8"])
        self.assertTrue("410" in drg_lst)
    
        drg_lst = de.get_drg_all(["S36240A"], ["0F540ZZ", "0F9900Z"])
        self.assertTrue("413" in drg_lst)
        drg_lst = de.get_drg_all(["S36240A"], ["0F540ZZ", "0FB40ZZ"])
        self.assertTrue("416" in drg_lst)
        drg_lst = de.get_drg_all(["S36240A"], ["0FB44ZZ"])
        self.assertTrue("419" in drg_lst)
       
        drg_lst = de.get_drg_all(["S36240A"], ["07JP0ZZ"])
        self.assertTrue("422" in drg_lst)
 
        drg_lst = de.get_drg_all(["S36240A"], ["008X3ZZ"])
        self.assertTrue("425" in drg_lst)
 
        drg_lst = de.get_drg_all(["K7469"], [])
        self.assertTrue("434" in drg_lst)
 
        drg_lst = de.get_drg_all(["C220"], [])
        self.assertTrue("437" in drg_lst)
 
        drg_lst = de.get_drg_all(["B252"], [])
        self.assertTrue("440" in drg_lst)
 
        drg_lst = de.get_drg_all(["B182"], [])
        self.assertTrue("443" in drg_lst)
 
        drg_lst = de.get_drg_all(["K8000"], [])
        self.assertTrue("446" in drg_lst)
 
if __name__=="__main__":
    unittest.main()




