import unittest

from drgpy.msdrg import DRGEngine


class TestGoldCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = DRGEngine("v43.1")

    def test_minimized_claim_derived_cases(self):
        cases = [
            ("ventilation", ["J95821"], ["5A1935Z"], "208"),
            ("intestinal_obstruction", ["K562", "K460"], ["0DTH0ZZ"], "330"),
            ("cholecystectomy", ["K8000", "J9811"], ["0FT44ZZ"], "418"),
            ("hip_replacement_mcc", ["S72001A", "J95821"], ["0SRR019"], "521"),
            ("hip_replacement", ["M80051A"], ["0SRR0J9"], "522"),
            ("infectious_or_procedure", ["A419", "K3532"], ["0DTJ4ZZ"], "853"),
            ("infectious_or_procedure_no_mcc", ["A419", "E871"], ["0T768DZ"], "854"),
            ("craniotomy_mcc", ["S065X0A", "S06A0XA"], ["009430Z"], "025"),
            ("vascular_procedure_cc", ["I871", "F840"], ["06JY0ZZ"], "253"),
            ("cardiac_catheterization", ["I469"], ["B2151ZZ"], "287"),
            ("joint_revision_cc", ["T8454XA", "D62"], ["0SRD0J9", "0SPD0JZ"], "467"),
            ("hip_femur_procedure_mcc", ["M80052A", "G928"], ["0QS706Z"], "480"),
            ("kidney_ureter_procedure_cc", ["N132", "A0472"], ["0T768DZ"], "660"),
            ("lung_resection_cc", ["C3411", "G90512"], ["0BTC4ZZ"], "164"),
            ("inguinal_hernia_cc", ["K4090", "I25810"], ["0YU50JZ"], "351"),
            ("ventral_hernia_cc", ["K433", "N390"], ["0WQF0ZZ"], "354"),
            ("biliary_disorder_mcc", ["K8309", "K831"], [], "444"),
            ("major_joint_replacement", ["M1711"], ["0SRC0J9"], "470"),
            ("cervical_fusion_cc", ["M4712", "G959"], ["0RG20A0"], "472"),
            ("upper_limb_procedure_cc", ["S42222A", "E871"], ["0PSD04Z"], "493"),
            ("urinary_disorder_mcc", ["T83518A", "A419"], [], "698"),
        ]
        for name, diagnoses, procedures, expected in cases:
            with self.subTest(name=name, expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_additional_claim_derived_severity_families(self):
        cases = [
            (["C3411", "A021"], ["0BTC4ZZ"], "163"),
            (["C3411", "D62"], ["0BTC4ZZ"], "164"),
            (["C3411"], ["0BTC4ZZ"], "165"),
            (["K4090", "A021"], ["0YU50JZ"], "350"),
            (["K4090", "D62"], ["0YU50JZ"], "351"),
            (["K4090"], ["0YU50JZ"], "352"),
            (["K433", "A021"], ["0WQF0ZZ"], "353"),
            (["K433", "D62"], ["0WQF0ZZ"], "354"),
            (["K433"], ["0WQF0ZZ"], "355"),
            (["K8309", "A021"], [], "444"),
            (["K8309", "D62"], [], "445"),
            (["K8309"], [], "446"),
            (["M1711", "A021"], ["0SRC0J9"], "469"),
            (["M1711"], ["0SRC0J9"], "470"),
            (["M4712", "A021"], ["0RG20A0"], "471"),
            (["M4712", "D62"], ["0RG20A0"], "472"),
            (["M4712"], ["0RG20A0"], "473"),
            (["S42222A", "A021"], ["0PSD04Z"], "492"),
            (["S42222A", "D62"], ["0PSD04Z"], "493"),
            (["S42222A"], ["0PSD04Z"], "494"),
            (["T83518A", "A021"], [], "698"),
            (["T83518A", "D62"], [], "699"),
            (["T83518A"], [], "700"),
        ]
        for diagnoses, procedures, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_claim_derived_severity_families(self):
        cases = [
            (["I871", "A021"], ["06JY0ZZ"], "252"),
            (["I871", "D62"], ["06JY0ZZ"], "253"),
            (["I871"], ["06JY0ZZ"], "254"),
            (["I469", "A021"], ["B2151ZZ"], "286"),
            (["I469"], ["B2151ZZ"], "287"),
            (["T8454XA", "A021"], ["0SRD0J9", "0SPD0JZ"], "466"),
            (["T8454XA", "D62"], ["0SRD0J9", "0SPD0JZ"], "467"),
            (["T8454XA"], ["0SRD0J9", "0SPD0JZ"], "468"),
            (["M80052A", "A021"], ["0QS706Z"], "480"),
            (["M80052A", "D62"], ["0QS706Z"], "481"),
            (["M80052A"], ["0QS706Z"], "482"),
            (["N132", "A021"], ["0T768DZ"], "659"),
            (["N132", "D62"], ["0T768DZ"], "660"),
            (["N132"], ["0T768DZ"], "661"),
        ]
        for diagnoses, procedures, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_craniotomy_severity_split(self):
        cases = [
            (["S065X0A", "S06A0XA"], "025"),
            (["S065X0A", "D62"], "026"),
            (["S065X0A"], "027"),
        ]
        for diagnoses, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, ["009430Z"]),
                    expected,
                )

    def test_ported_concordance_regressions(self):
        cases = [
            (
                "disc_device_takes_priority",
                ["Z9716"],
                ["005W3ZZ", "0RH03BZ"],
                "518",
            ),
            (
                "delivery_with_only_excluded_or_procedure",
                ["Z640", "Z370"],
                ["10D07Z3", "0KQM0ZZ"],
                "807",
            ),
            (
                "delivery_with_additional_nonexcluded_or_procedure",
                ["Z640", "Z370"],
                ["10D07Z3", "0KQM0ZZ", "0W3N0ZZ"],
                "768",
            ),
            (
                "delivery_or_procedure_ignores_except_list",
                ["Z640", "Z370"],
                ["10D17Z9", "0KQM0ZZ"],
                "768",
            ),
            (
                "newborn_significant_problem_precedes_normal_newborn",
                ["P003", "P221"],
                [],
                "794",
            ),
            (
                "normal_newborn_fallback_with_secondary",
                ["Z3800", "P599"],
                [],
                "795",
            ),
        ]
        for name, diagnoses, procedures, expected in cases:
            with self.subTest(name=name, expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
