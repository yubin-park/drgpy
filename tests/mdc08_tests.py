import unittest
from drgpy.msdrg import DRGEngine

class TestMCD08(unittest.TestCase):

    def test_mdcs08(self):

        de = DRGEngine()

        drg_lst = de.get_drg_all(["Z9716"], ["0RG1070"])
        self.assertTrue("455" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0RG8070"])
        self.assertTrue("458" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0RG607J"])
        self.assertTrue("460" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0SUR0BZ", "0SRB03Z"])
        self.assertTrue("462" in drg_lst)
        drg_lst = de.get_drg_all(["Z9716", "E0800"], 
                                ["0SRC06Z", "0SRF0J9"])
        self.assertTrue("461" in drg_lst)
        drg_lst = de.get_drg_all(["Z9716", "E0800"], 
                                ["0SRC06Z", "0SRC06Z"])
        self.assertTrue("461" not in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0HR1XJZ"])
        self.assertTrue("465" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0SPD0JC"])
        self.assertTrue("468" in drg_lst)
        drg_lst = de.get_drg_all(["Z9716"], ["0SPB0JZ", "0SRB01Z"])
        self.assertTrue("468" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0SR903Z"])
        self.assertTrue("470" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0RG03J0"])
        self.assertTrue("473" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0X6B0ZZ"])
        self.assertTrue("476" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0N934ZX"])
        self.assertTrue("479" in drg_lst)
     
        drg_lst = de.get_drg_all(["Z9716"], ["0Q863ZZ"])
        self.assertTrue("482" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0RRF0KZ"])
        self.assertTrue("483" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0MQP3ZZ"])
        self.assertTrue("489" in drg_lst)
        drg_lst = de.get_drg_all(["T8450XA"], ["0MQP3ZZ"])
        self.assertTrue("487" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["005W3ZZ"])
        self.assertTrue("520" in drg_lst)
        drg_lst = de.get_drg_all(["Z9716"], ["0RH03BZ"])
        self.assertTrue("518" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z9716"], ["0SWG48Z"])
        self.assertTrue("494" in drg_lst)
         
        drg_lst = de.get_drg_all(["Z9716"], ["0M530ZZ"])
        self.assertTrue("497" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0Q573ZZ"])
        self.assertTrue("499" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z9716"], ["0J860ZZ"])
        self.assertTrue("502" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0L8P4ZZ"])
        self.assertTrue("505" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0MC50ZZ"])
        self.assertTrue("506" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0R9G0ZZ"])
        self.assertTrue("508" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0RJJ4ZZ"])
        self.assertTrue("509" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0P8J0ZZ"])
        self.assertTrue("512" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["0HRGX74"])
        self.assertTrue("514" in drg_lst)

        drg_lst = de.get_drg_all(["Z9716"], ["008G0ZZ"])
        self.assertTrue("517" in drg_lst)





if __name__=="__main__":
    unittest.main()




