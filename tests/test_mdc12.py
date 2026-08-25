import unittest
from drgpy.msdrg import DRGEngine

class TestMCD12(unittest.TestCase):

    def test_mdcs12_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z302"], ["07JP0ZZ"], "M")
        self.assertTrue("708" in drg_lst)
        drg_lst = de.get_drg_all(["Z302"], ["0VT08ZZ", "0VT34ZZ"], "M")
        self.assertTrue("708" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z302"], ["0TMD4ZZ"], "M")
        self.assertTrue("710" in drg_lst)
         
        drg_lst = de.get_drg_all(["Z302"], ["0V1N0KK"], "M")
        self.assertTrue("712" in drg_lst)

        drg_lst = de.get_drg_all(["Z302"], ["0V508ZZ"], "M")
        self.assertTrue("714" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], ["DVY0KZZ"], "M")
        self.assertTrue("716" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], [], "M")
        self.assertTrue("724" in drg_lst)
 
        drg_lst = de.get_drg_all(["N400"], [], "M")
        self.assertTrue("726" in drg_lst)
 
        drg_lst = de.get_drg_all(["A57"], [], "M")
        self.assertTrue("728" in drg_lst)
 
        drg_lst = de.get_drg_all(["L293"], [], "M")
        self.assertTrue("730" in drg_lst)

    def test_mdcs12_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z302"], ["07JP0ZZ"], "M")
        self.assertTrue("708" in drg_lst)
        drg_lst = de.get_drg_all(["Z302"], ["0VT08ZZ", "0VT34ZZ"], "M")
        self.assertTrue("708" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z302"], ["0TMD4ZZ"], "M")
        self.assertTrue("710" in drg_lst)
         
        drg_lst = de.get_drg_all(["Z302"], ["0V1N0KK"], "M")
        self.assertTrue("712" in drg_lst)

        drg_lst = de.get_drg_all(["Z302"], ["0V508ZZ"], "M")
        self.assertTrue("714" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], ["DVY0KZZ"], "M")
        self.assertTrue("716" in drg_lst)
 
        drg_lst = de.get_drg_all(["C600"], [], "M")
        self.assertTrue("724" in drg_lst)
 
        drg_lst = de.get_drg_all(["N400"], [], "M")
        self.assertTrue("726" in drg_lst)
 
        drg_lst = de.get_drg_all(["A57"], [], "M")
        self.assertTrue("728" in drg_lst)
 
        drg_lst = de.get_drg_all(["L293"], [], "M")
        self.assertTrue("730" in drg_lst)

    def test_n400_requires_male_gender(self):
        de = DRGEngine(version="v43.1")

        self.assertEqual(de.get_drg(["N400"], [], gender="M"), "726")
        self.assertEqual(
            de.get_drg(["N400", "A021"], [], gender="M"),
            "725",
        )
        self.assertEqual(de.get_drg(["N400"], [], gender="F"), "000")

    def test_gender_is_normalized_and_validated(self):
        de = DRGEngine(version="v43.1")

        self.assertEqual(de.get_drg(["N400"], [], gender="m"), "726")
        with self.assertRaisesRegex(ValueError, "gender must be 'F' or 'M'"):
            de.get_drg(["N400"], [], gender="unknown")
 
if __name__=="__main__":
    unittest.main()



