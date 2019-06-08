import unittest
from drgpy.msdrg import DRGEngine

class TestDRGEngine(unittest.TestCase):

    def test_basics(self):
        de = DRGEngine()
        el_lst = de.get_dxel(["A021"])
        print(el_lst)
        el_lst = de.get_dxel(["", "A021"])
        print(el_lst)
        el_lst = de.get_dxel(["G40B19"])
        print(el_lst)

        el_lst = de.get_prel(["02YA0Z0", "02YA0Z1"])
        print(el_lst)
        el_lst = de.get_prel(["02HA0RS"])
        print(el_lst)

if __name__=="__main__":
    unittest.main()




