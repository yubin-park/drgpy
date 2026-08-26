import unittest
from datetime import date

from drgpy._versions import LATEST_VERSION, get_version_for_date
from drgpy.msdrg import DRGEngine


class TestModernVersions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.v41 = DRGEngine("v41")
        cls.v42 = DRGEngine("v42")
        cls.v43_1 = DRGEngine("v43.1")

    def test_effective_date_routing(self):
        cases = {
            date(2023, 10, 1): "v41",
            date(2024, 4, 1): "v41.1",
            date(2024, 10, 1): "v42",
            date(2025, 4, 1): "v42.1",
            date(2025, 10, 1): "v43",
            date(2026, 4, 1): "v43.1",
        }
        for effective_date, expected in cases.items():
            self.assertEqual(get_version_for_date(effective_date).name, expected)
        self.assertEqual(LATEST_VERSION.name, "v43.1")

    def test_v41_rule_changes(self):
        self.assertEqual(
            self.v41.get_drg(["I350"], ["02QF0ZJ", "02QG0ZE", "025S0ZZ"]),
            "212",
        )
        self.assertEqual(self.v41.get_drg(["K3580"], ["0DTJ0ZZ"]), "399")
        self.assertEqual(
            self.v41.get_drg(["I4720"], ["0JH608Z", "02H63KZ"]),
            "277",
        )

    def test_v42_rule_changes(self):
        self.assertEqual(self.v42.get_drg(["I21A1"], ["02L70CK", "025S0ZZ"]), "317")
        self.assertEqual(self.v42.get_drg(["C9100"], ["D020DZZ"]), "850")
        self.assertEqual(
            self.v42.get_drg(["I25110"], ["027034Z", "02F03ZZ"]),
            "324",
        )
        self.assertEqual(
            self.v42.get_drg(
                ["M48061"],
                ["0SG10AJ", "0SG30AJ", "01NB0ZZ", "00NY0ZZ"],
            ),
            "448",
        )

    def test_v43_rule_changes(self):
        cases = [
            (["I2601"], ["02FP3Z0"], "173"),
            (["I21A1"], ["02VX3EZ", "02VW3DZ", "03LJ0BZ"], "209"),
            (["I21A1"], ["04V03DZ", "04VC3DZ"], "213"),
            (["I21A1"], ["02C03Z6"], "318"),
            (["I21A1", "A021"], ["02C03Z6", "0270346"], "359"),
        ]
        for diagnoses, procedures, expected in cases:
            self.assertEqual(self.v43_1.get_drg(diagnoses, procedures), expected)

    def test_v43_coronary_bypass_split_rules(self):
        cases = [
            (["02100Z9", "027034Z"], "232"),
            (["02100Z9", "4A023N7"], "234"),
            (["02100Z9", "06BQ4ZZ"], "236"),
        ]
        for procedures, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.v43_1.get_drg(["I25119"], procedures),
                    expected,
                )

    def test_v43_multiple_trauma_requires_distinct_body_sites(self):
        procedures = ["0RG20A0", "0RB30ZZ"]
        self.assertEqual(
            self.v43_1.get_drg(["S14126A", "S12501A"], procedures),
            "030",
        )
        self.assertEqual(
            self.v43_1.get_drg(["S062X0A", "S7400XA"], procedures),
            "959",
        )

    def test_v43_appendix_c_and_hac(self):
        self.assertEqual(len(self.v43_1.ccmap), 18391)
        self.assertEqual(len(self.v43_1.exmap), 1994)
        self.assertEqual(len(self.v43_1.drg_exclusions), 31)
        present = self.v43_1.get_features(["I21A1", "E0800"], [], poa=["Y", "Y"])
        acquired = self.v43_1.get_features(["I21A1", "E0800"], [], poa=["Y", "N"])
        self.assertEqual(present["_MCC"], 1)
        self.assertEqual(acquired["_MCC"], 0)

    def test_minimized_real_world_regressions(self):
        cases = [
            (self.v42, ["I25110"], ["027334Z"], "321"),
            (self.v42, ["I25110"], ["027034Z"], "322"),
            (self.v43_1, ["I25110"], ["02C03Z6", "0270346"], "360"),
            (self.v42, ["M48061"], ["0RG6070", "0RG6071"], "402"),
            (self.v42, ["M48061", "A021"], ["0RG7070", "0RG6071"], "426"),
            (self.v42, ["M48061", "D62"], ["0RG7070", "0RG6071"], "427"),
            (self.v42, ["M48061"], ["0RG7070", "0RG6071"], "428"),
            (self.v42, ["M48061", "A021"], ["0RG1070", "0RG1071"], "429"),
            (self.v42, ["M48061"], ["0RG1070", "0RG1071"], "430"),
            (self.v42, ["M48061", "A021"], ["0RG7070"], "447"),
            (self.v42, ["M48061"], ["0RG7070"], "448"),
            (self.v43_1, ["M4316"], ["0SG0071", "0SG30K1"], "448"),
            (self.v42, ["M48061", "A021"], ["0RG6070"], "450"),
            (self.v42, ["M48061"], ["0RG6070"], "451"),
        ]
        for engine, diagnoses, procedures, expected in cases:
            with self.subTest(version=engine.version, expected=expected):
                self.assertEqual(engine.get_drg(diagnoses, procedures), expected)


if __name__ == "__main__":
    unittest.main()
