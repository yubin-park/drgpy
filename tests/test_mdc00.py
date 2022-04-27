import unittest
from drgpy.msdrg import DRGEngine

class TestMCD00(unittest.TestCase):

    def test_mdcs00_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["I10", "E0800"], ["02YA0Z0"])
        self.assertTrue("001" in drg_lst)
        drg_lst = de.get_drg_all(["I10"], ["02YA0Z0"])
        self.assertTrue("002" in drg_lst)
        drg_lst = de.get_drg_all([], ["02HA0RS"])
        self.assertTrue("002" not in drg_lst)
        drg_lst = de.get_drg_all([], ["02HA0RS", "02PA0RZ"])
        self.assertTrue("002" in drg_lst)

        drg_lst = de.get_drg_all([], ["5A1522F"])
        self.assertTrue("003" in drg_lst)
        drg_lst = de.get_drg_all([], ["0B110F4", "5A1955Z"])
        self.assertTrue("003" in drg_lst)
        drg_lst = de.get_drg_all(["E0800"], ["0B110F4"])
        self.assertTrue("003" in drg_lst)
        drg_lst = de.get_drg_all(["A360"], ["0B110F4"])
        self.assertTrue("004" not in drg_lst)

        drg_lst = de.get_drg_all([], ["0FY00Z0", "0DY80Z0"])
        self.assertTrue("005" in drg_lst)
        drg_lst = de.get_drg_all(["I10", "E0800"], ["0FY00Z0"])
        self.assertTrue("005" in drg_lst)
        drg_lst = de.get_drg_all([], ["0DY80Z0"])
        self.assertTrue("005" in drg_lst)
        drg_lst = de.get_drg_all([], ["0FY00Z0"])
        self.assertTrue("006" in drg_lst)

        drg_lst = de.get_drg_all([], ["30230G2"])
        self.assertTrue("014" in drg_lst)

        drg_lst = de.get_drg_all([], ["0BYC0Z0"])
        self.assertTrue("007" in drg_lst)

        drg_lst = de.get_drg_all(["I120", "E0800"], ["0TY00Z0", "0FYG0Z0"])
        self.assertTrue("008" in drg_lst)
        drg_lst = de.get_drg_all(["I120"], ["0TY00Z0", "0FYG0Z0"])
        self.assertTrue("008" not in drg_lst)

        drg_lst = de.get_drg_all([], ["XW033C3"])
        self.assertTrue("016" in drg_lst)
        drg_lst = de.get_drg_all(["I10", "E0800"], ["30230AZ"])
        self.assertTrue("304" in drg_lst)
        drg_lst = de.get_drg_all([], ["30230AZ"])
        # in v37, this is 983, used to be 017
        self.assertTrue("983" in drg_lst) 

        drg_lst = de.get_drg_all(["E0800"], ["0FYG0Z0"])
        self.assertTrue("010" in drg_lst)

        drg_lst = de.get_drg_all(["A360", "E0800"], ["0B110F4"])
        self.assertTrue("011" in drg_lst)

        drg_lst = de.get_drg_all(["A360", "A000"], ["0B110F4"])
        self.assertTrue("012" in drg_lst)

        drg_lst = de.get_drg_all(["A360"], ["0B110F4"])
        self.assertTrue("013" in drg_lst)

    def test_mdcs00_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["I10", "E0800"], ["02YA0Z0"])
        self.assertTrue("001" in drg_lst)
        drg_lst = de.get_drg_all(["I10"], ["02YA0Z0"])
        self.assertTrue("002" in drg_lst)
        drg_lst = de.get_drg_all([], ["02HA0RS"])
        self.assertTrue("002" not in drg_lst)
        drg_lst = de.get_drg_all([], ["02HA0RS", "02PA0RZ"])
        self.assertTrue("002" in drg_lst)

        drg_lst = de.get_drg_all([], ["5A1522F"])
        self.assertTrue("003" in drg_lst)
        drg_lst = de.get_drg_all([], ["0B110F4", "5A1955Z"])
        self.assertTrue("003" in drg_lst)
        drg_lst = de.get_drg_all(["E0800"], ["0B110F4"])
        self.assertTrue("003" in drg_lst)
        drg_lst = de.get_drg_all(["A360"], ["0B110F4"])
        self.assertTrue("004" not in drg_lst)

        drg_lst = de.get_drg_all([], ["0FY00Z0", "0DY80Z0"])
        self.assertTrue("005" in drg_lst)
        drg_lst = de.get_drg_all(["I10", "E0800"], ["0FY00Z0"])
        self.assertTrue("005" in drg_lst)
        drg_lst = de.get_drg_all([], ["0DY80Z0"])
        self.assertTrue("005" in drg_lst)
        drg_lst = de.get_drg_all([], ["0FY00Z0"])
        self.assertTrue("006" in drg_lst)

        drg_lst = de.get_drg_all([], ["30233G2"]) # v40 change
        self.assertTrue("014" in drg_lst)

        drg_lst = de.get_drg_all([], ["0BYC0Z0"])
        self.assertTrue("007" in drg_lst)

        drg_lst = de.get_drg_all(["I120", "E0800"], ["0TY00Z0", "0FYG0Z0"])
        self.assertTrue("008" in drg_lst)
        drg_lst = de.get_drg_all(["I120"], ["0TY00Z0", "0FYG0Z0"])
        self.assertTrue("008" not in drg_lst)

        drg_lst = de.get_drg_all(["I10", "E0800"], ["30243C0"]) # v40 change
        self.assertTrue("016" in drg_lst)
        drg_lst = de.get_drg_all(["I10", "E0800"], ["30230AZ"])
        self.assertTrue("304" in drg_lst)
        drg_lst = de.get_drg_all([], ["30233AZ"])
        # in v37, this is 983, used to be 017 in v40 again
        self.assertTrue("017" in drg_lst) 

        drg_lst = de.get_drg_all(["E0800"], ["0FYG0Z0"])
        self.assertTrue("010" in drg_lst)

        drg_lst = de.get_drg_all(["A360", "E0800"], ["0B110F4"])
        self.assertTrue("011" in drg_lst)

        drg_lst = de.get_drg_all(["A360", "A000"], ["0B110F4"])
        self.assertTrue("012" in drg_lst)

        drg_lst = de.get_drg_all(["A360"], ["0B110F4"])
        self.assertTrue("013" in drg_lst)

if __name__=="__main__":
    unittest.main()




