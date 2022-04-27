import unittest
from drgpy.msdrg import DRGEngine

class TestMisc(unittest.TestCase):

    def test_misc_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg(['O99324', 'F1120', 'B1920', 'O9842', 'O701', 'F1210', 'Z370', 'Z3A40'],  
            ['3E033VJ', '4A1HX4Z', '10E0XZZ', '10907ZC'])

        


if __name__=="__main__":
    unittest.main()




