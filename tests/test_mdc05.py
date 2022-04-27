import unittest
from drgpy.msdrg import DRGEngine

class TestMCD05(unittest.TestCase):

    def test_mdcs05_v37(self):

        de = DRGEngine(version="v37")

        drg_lst = de.get_drg_all(["Z95828"], ["02HA0RJ"])
        self.assertTrue("215" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["024F07J"])
        self.assertTrue("221" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["024F07J"])
        self.assertTrue("219" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["024F07J", "4A020N6"])
        self.assertTrue("218" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02HK0KZ", "0JH609Z"])
        self.assertTrue("227" in drg_lst)
        drg_lst = de.get_drg_all(["I092"], 
                    ["02HK0KZ", "0JH609Z", "4A020N6"])
        self.assertTrue("225" in drg_lst)
        drg_lst = de.get_drg_all(["I0981"], 
                    ["02HK0KZ", "0JH609Z", "4A020N6"])
        self.assertTrue("223" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z95828"], ["0210344"])
        self.assertTrue("228" not in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["0210344"])
        self.assertTrue("228" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["0210083"])
        self.assertTrue("236" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0210083", "0270346"])
        self.assertTrue("232" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], 
                                    ["0210083", "0270346"])
        self.assertTrue("231" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0210083", "4A020N6"])
        self.assertTrue("234" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["02BW0ZZ"])
        self.assertTrue("269" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["02160Z7"])
        self.assertTrue("272" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["0Y620ZZ"])
        self.assertTrue("241" in drg_lst)
       
        drg_lst = de.get_drg_all(["Z95828"], ["0JH604Z", "02H40JZ"])
        self.assertTrue("244" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["0JH608Z"])
        self.assertTrue("245" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02HN4KZ"])
        self.assertTrue("265" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02573ZK"])
        self.assertTrue("274" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["02553ZZ"])
        self.assertTrue("273" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02703D6"])
        self.assertTrue("249" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["02703D6"])
        self.assertTrue("248" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["02703D6", "02724TZ"])
        self.assertTrue("248" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0270346"])
        self.assertTrue("247" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["0270346"])
        self.assertTrue("246" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], 
                        ["0270346", "0270356", "02714TZ"])
        self.assertTrue("246" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0270346", "0270346"])
        self.assertTrue("247" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["02703Z6"])
        self.assertTrue("251" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["00HE0MZ"])
        self.assertTrue("254" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["0X600ZZ"])
        self.assertTrue("257" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["0JH604Z"])
        self.assertTrue("259" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["02QS0ZZ"])
        self.assertTrue("263" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["015K0ZZ"])
        self.assertTrue("264" in drg_lst) 

        drg_lst = de.get_drg_all(["I2101"], [])
        self.assertTrue("282" in drg_lst) 

        drg_lst = de.get_drg_all(["I2101"], ["4A020N6"])
        self.assertTrue("287" in drg_lst) 

        drg_lst = de.get_drg_all(["A3951", "E0800"], [])
        self.assertTrue("288" in drg_lst) 

        drg_lst = de.get_drg_all(["I0981"],["5A1522G"])
        # used to be 291, now 293 in v37
        self.assertTrue("293" in drg_lst) 

        drg_lst = de.get_drg_all(["I8010"],[])
        self.assertTrue("295" in drg_lst) 

        drg_lst = de.get_drg_all(["I462"],["5A1522G"])
        # used to be 296, now 298 in v37
        self.assertTrue("298" in drg_lst) 

        drg_lst = de.get_drg_all(["E0851", "D593"],[])
        self.assertTrue("299" in drg_lst) 
        drg_lst = de.get_drg_all(["E0851", "E0800"],[])
        self.assertTrue("301" in drg_lst) 

        drg_lst = de.get_drg_all(["I2510"],[])
        self.assertTrue("303" in drg_lst) 

        drg_lst = de.get_drg_all(["I10"],[])
        self.assertTrue("305" in drg_lst) 

        drg_lst = de.get_drg_all(["A5201"],[])
        self.assertTrue("307" in drg_lst) 

        drg_lst = de.get_drg_all(["I440"],[])
        self.assertTrue("310" in drg_lst) 

        drg_lst = de.get_drg_all(["R079"],[])
        self.assertTrue("313" in drg_lst) 

        drg_lst = de.get_drg_all(["A3681", "A000"],[])
        self.assertTrue("315" in drg_lst) 

    def test_mdcs05_v40(self):

        de = DRGEngine(version="v40")

        drg_lst = de.get_drg_all(["Z95828"], ["02HA0RS"]) #changed in v40
        self.assertTrue("215" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["024F07J"])
        self.assertTrue("221" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["024F07J"])
        self.assertTrue("219" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["024F07J", "4A020N6"])
        self.assertTrue("218" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02HK0KZ", "0JH609Z"])
        self.assertTrue("227" in drg_lst)
        drg_lst = de.get_drg_all(["I092"], 
                    ["02HK0KZ", "0JH609Z", "4A020N6"])
        self.assertTrue("225" in drg_lst)
        drg_lst = de.get_drg_all(["I0981"], 
                    ["02HK0KZ", "0JH609Z", "4A020N6"])
        self.assertTrue("223" in drg_lst)
        
        drg_lst = de.get_drg_all(["Z95828"], ["0210344"])
        self.assertTrue("228" not in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["0210344"])
        self.assertTrue("228" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["0210083"])
        self.assertTrue("236" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0210083", "0270346"])
        self.assertTrue("232" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], 
                                    ["0210083", "0270346"])
        self.assertTrue("231" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0210083", "4A020N6"])
        self.assertTrue("234" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["02BW0ZZ"])
        self.assertTrue("269" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["02160Z7"])
        self.assertTrue("272" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["0Y620ZZ"])
        self.assertTrue("241" in drg_lst)
       
        drg_lst = de.get_drg_all(["Z95828"], ["0JH604Z", "02H40JZ"])
        self.assertTrue("244" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["0JH608Z"])
        self.assertTrue("245" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02HN4KZ"])
        self.assertTrue("265" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02573ZK"])
        self.assertTrue("274" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["02553ZZ"])
        self.assertTrue("273" in drg_lst)

        drg_lst = de.get_drg_all(["Z95828"], ["02703D6", "02703Z6"])
        self.assertTrue("249" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["02703D6", "02703Z6"]) 
        self.assertTrue("248" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["02703D6", "02724TZ", "02703Z6"])
        self.assertTrue("248" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0270346", "02703Z6"])
        self.assertTrue("247" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828", "E0800"], ["0270346", "02703Z6"])
        self.assertTrue("246" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], 
                        ["0270346", "0270356", "02714TZ", "02703Z6"])
        self.assertTrue("246" in drg_lst)
        drg_lst = de.get_drg_all(["Z95828"], ["0270346", "0270346", "02703Z6"])
        self.assertTrue("247" in drg_lst)
 
        drg_lst = de.get_drg_all(["Z95828"], ["02703Z6"])
        self.assertTrue("251" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["00HE0MZ"])
        self.assertTrue("254" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["0X600ZZ"])
        self.assertTrue("257" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["0JH604Z"])
        self.assertTrue("259" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["02QS0ZZ"])
        self.assertTrue("263" in drg_lst) 

        drg_lst = de.get_drg_all(["Z95828"], ["015K0ZZ"])
        self.assertTrue("264" in drg_lst) 

        drg_lst = de.get_drg_all(["I2101"], [])
        self.assertTrue("282" in drg_lst) 

        drg_lst = de.get_drg_all(["I2101"], ["4A020N6"])
        self.assertTrue("287" in drg_lst) 

        drg_lst = de.get_drg_all(["A3951", "E0800"], [])
        self.assertTrue("288" in drg_lst) 

        drg_lst = de.get_drg_all(["I0981"],["5A1522G"])
        # used to be 291, now 293 in v37
        self.assertTrue("293" in drg_lst) 

        drg_lst = de.get_drg_all(["I8010"],[])
        self.assertTrue("295" in drg_lst) 

        drg_lst = de.get_drg_all(["I462"],["5A1522G"])
        # used to be 296, now 298 in v37
        self.assertTrue("298" in drg_lst) 

        # D593 removed from MCC in v40
        drg_lst = de.get_drg_all(["E0851", "D593", "A064"],[])
        self.assertTrue("299" in drg_lst) 
        drg_lst = de.get_drg_all(["E0851", "E0800"],[])
        self.assertTrue("301" in drg_lst) 

        drg_lst = de.get_drg_all(["I2510"],[])
        self.assertTrue("303" in drg_lst) 

        drg_lst = de.get_drg_all(["I10"],[])
        self.assertTrue("305" in drg_lst) 

        drg_lst = de.get_drg_all(["A5201"],[])
        self.assertTrue("307" in drg_lst) 

        drg_lst = de.get_drg_all(["I440"],[])
        self.assertTrue("310" in drg_lst) 

        drg_lst = de.get_drg_all(["R079"],[])
        self.assertTrue("313" in drg_lst) 

        drg_lst = de.get_drg_all(["A3681", "A000"],[])
        self.assertTrue("315" in drg_lst) 



if __name__=="__main__":
    unittest.main()




