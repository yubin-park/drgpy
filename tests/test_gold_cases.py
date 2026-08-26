import unittest

from drgpy.msdrg import DRGEngine


class TestGoldCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = DRGEngine("v43.1")

    def test_minimized_validation_samples(self):
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

    def test_additional_minimized_samples(self):
        cases = [
            ("knee_replacement_variant", ["M1711"], ["0SRC0JA"], "470"),
            ("copd_respiratory_failure", ["J441", "J9621"], [], "190"),
            ("intestinal_obstruction_medical", ["K56609"], [], "390"),
            ("subdural_hemorrhage", ["S06360A", "N186"], [], "085"),
            ("device_complication_sepsis", ["T8571XA", "A419"], [], "919"),
            (
                "lumbar_fusion",
                ["M4316"],
                ["0SG00AJ", "0SG0071"],
                "402",
            ),
            ("tibia_fracture_cc", ["S82141A", "D62"], ["0QSG34Z"], "493"),
            ("colectomy", ["Z433", "K567"], ["0DBM4ZZ"], "330"),
            ("carotid_stent", ["I6521"], ["037K3DZ"], "036"),
            ("atrial_fibrillation", ["I4820"], [], "310"),
            ("pulmonary_embolism", ["I2699"], [], "176"),
            ("craniotomy_tumor", ["C713"], ["00B70ZZ"], "027"),
            ("cervical_fusion", ["S12500A"], ["0RG10A0"], "473"),
            (
                "cholecystectomy_pancreatitis",
                ["K8510", "K8010"],
                ["0FT44ZZ"],
                "418",
            ),
            ("spinal_fusion", ["M4802"], ["0RG20K0"], "473"),
            ("hip_replacement_variant", ["M1612"], ["0SRB0JA"], "470"),
            ("femur_fracture", ["S72002A"], ["0QS704Z"], "482"),
            ("pericarditis", ["I3139"], [], "316"),
            ("aki_encephalopathy", ["N179", "G9341"], [], "682"),
            (
                "sepsis_urinary_procedure",
                ["A4159", "N136"],
                ["0T778DZ"],
                "854",
            ),
            ("transcatheter_valve", ["I080"], ["02RF38Z"], "267"),
            ("ureteral_obstruction", ["N130"], ["0T768DZ"], "661"),
            (
                "pacemaker",
                ["I495", "I452"],
                ["0JH606Z", "02H63JZ"],
                "243",
            ),
        ]
        for name, diagnoses, procedures, expected in cases:
            with self.subTest(name=name, expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_additional_rule_samples(self):
        cases = [
            ("diverticulitis", ["K5732"], [], "392"),
            ("cellulitis", ["L03115"], [], "603"),
            ("psychosis", ["F209"], [], "885"),
            ("hip_device_dislocation", ["T84020A"], [], "561"),
            ("femur_aftercare", ["S72041D", "A6920"], [], "560"),
            (
                "diaphragmatic_hernia_repair",
                ["K449"],
                ["0BUT4JZ"],
                "328",
            ),
            (
                "hip_fracture_replacement",
                ["S72011A"],
                ["0SRR0J9"],
                "522",
            ),
            ("pulmonary_embolism_mcc", ["I2699", "J9601"], [], "175"),
            (
                "intestinal_adhesiolysis",
                ["K5650", "K5090"],
                ["0DN84ZZ"],
                "336",
            ),
            ("myeloproliferative_disorder", ["D735", "K766"], [], "815"),
            ("intestinal_obstruction_medical", ["K567"], [], "390"),
            (
                "hip_fracture_replacement_variant",
                ["S72001A"],
                ["0SRR0J9"],
                "522",
            ),
            ("hip_contusion", ["S7001XA"], [], "605"),
            (
                "bladder_cancer_procedure",
                ["C679", "N131"],
                ["0TBB8ZZ"],
                "669",
            ),
            (
                "intestinal_obstruction_laparoscopy",
                ["K56609"],
                ["0WJG4ZZ"],
                "358",
            ),
            (
                "intestinal_obstruction_open_adhesiolysis",
                ["K56699"],
                ["0DN80ZZ"],
                "337",
            ),
            ("angina", ["I200"], [], "311"),
            (
                "intestinal_ischemia_resection",
                ["K551", "N390"],
                ["0DTF4ZZ"],
                "330",
            ),
            ("dementia", ["F0390"], [], "884"),
        ]
        for name, diagnoses, procedures, expected in cases:
            with self.subTest(name=name, expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_additional_high_risk_samples(self):
        cases = [
            (
                "neurostimulator_mcc",
                ["G20B2", "E43"],
                ["00H03MZ", "0JH60BZ"],
                "023",
            ),
            ("stroke_thrombectomy", ["I63412"], ["03CG3ZZ"], "024"),
            ("craniotomy_mcc", ["C7931", "G935"], ["00B70ZX"], "025"),
            (
                "aneurysm_craniotomy_cc",
                ["I671", "Z6842"],
                ["03VG3HZ"],
                "026",
            ),
            ("neurostimulator_no_cc", ["G250"], ["00H03MZ"], "027"),
            (
                "spinal_procedure_cc",
                ["T85113A", "G9600"],
                ["00HU0MZ"],
                "029",
            ),
            (
                "cabg_cath_mcc",
                ["I214", "R570"],
                ["02100Z9", "4A023N7"],
                "233",
            ),
            (
                "cabg_cath_no_mcc",
                ["I25110"],
                ["02100Z9", "4A023N7"],
                "234",
            ),
            (
                "cabg_no_cath_mcc",
                ["I25118", "J951"],
                ["02100Z9"],
                "235",
            ),
            ("cabg_no_cath", ["I214"], ["02100Z9"], "236"),
        ]
        for name, diagnoses, procedures, expected in cases:
            with self.subTest(name=name, expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_multiple_significant_trauma_precedence_samples(self):
        cases = [
            (
                ["S42491B", "D62", "S32591A"],
                ["0PSF04Z"],
                ["Y", "N", "Y"],
                "M",
                "01",
                "958",
            ),
            (
                ["S272XXA", "J9601", "S72032A"],
                [],
                ["Y", "Y", "Y"],
                "M",
                "51",
                "963",
            ),
            (
                ["S066XAA", "N179", "S32592A"],
                [],
                ["Y", "Y", "Y"],
                "M",
                "62",
                "964",
            ),
        ]
        for diagnoses, procedures, poa, gender, status, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.engine.get_drg(
                        diagnoses,
                        procedures,
                        gender=gender,
                        poa=poa,
                        discharge_status=status,
                    ),
                    expected,
                )

    def test_unrelated_operating_room_precedence_samples(self):
        cases = [
            (["K8020", "M8008XA"], ["0QU03JZ"], "982"),
            (["R569", "I420"], ["5A02216"], "982"),
            (["E871"], ["0SRC0J9"], "983"),
            (["R222"], ["0KBJ3ZX"], "983"),
        ]
        for diagnoses, procedures, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.engine.get_drg(diagnoses, procedures),
                    expected,
                )

    def test_additional_severity_family_samples(self):
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

    def test_severity_family_samples(self):
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
