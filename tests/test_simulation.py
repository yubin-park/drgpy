import unittest

from drgpy.msdrg import DRGEngine
from drgpy.msdrg_allvers import DRGEngineAllVers


class TestSimulation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = DRGEngine("v43.1")

    def test_single_code_drg_candidates(self):
        self.assertEqual(
            self.engine.get_code_drg_candidates("A419", "diagnosis"),
            ["793", "870", "871", "872", "974", "975", "976"],
        )
        procedure_candidates = self.engine.get_code_drg_candidates(
            "0SG0071",
            "procedure",
        )
        self.assertIn("402", procedure_candidates)
        self.assertIn("448", procedure_candidates)
        self.assertIn("451", procedure_candidates)

    def test_invalid_candidate_code_type(self):
        with self.assertRaises(ValueError):
            self.engine.get_code_drg_candidates("A419", "invalid")

    def test_principal_diagnosis_simulation(self):
        simulations = self.engine.simulate_drg_permutations(
            ["I469", "A021"],
            ["B2151ZZ"],
        )
        self.assertEqual(
            [(result["principal_diagnosis"], result["drg"])
             for result in simulations],
            [("I469", "286"), ("A021", "871")],
        )
        self.assertEqual(
            simulations[0]["secondary_diagnoses"],
            ["A021"],
        )
        self.assertEqual(
            simulations[0]["matching_drgs"],
            ["286", "296"],
        )

    def test_distinct_possible_drgs(self):
        self.assertEqual(
            self.engine.get_possible_drgs(
                ["I871", "D62", "A021"],
                ["06JY0ZZ"],
            ),
            ["252", "811", "854"],
        )
        self.assertEqual(
            self.engine.get_possible_drgs([], ["02HA0RS"]),
            ["983"],
        )

    def test_poa_list_realigns_with_principal(self):
        diagnoses = ["I21A1", "E0800", "D62"]
        procedures = []
        list_results = self.engine.simulate_drg_permutations(
            diagnoses,
            procedures,
            poa=["Y", "N", "Y"],
        )
        dict_results = self.engine.simulate_drg_permutations(
            diagnoses,
            procedures,
            poa={"I21A1": "Y", "E0800": "N", "D62": "Y"},
        )
        self.assertEqual(list_results, dict_results)

        duplicate_results = self.engine.simulate_drg_permutations(
            ["I21A1", "I21A1", "E0800", "D62"],
            procedures,
            poa=["Y", "N", "N", "Y"],
        )
        self.assertEqual(duplicate_results, dict_results)

    def test_date_routed_simulation(self):
        engine = DRGEngineAllVers()
        self.assertIn(
            "402",
            engine.get_code_drg_candidates(
                "0SG0071",
                "2026-04-01",
                code_type="procedure",
            ),
        )
        self.assertEqual(
            engine.get_possible_drgs(
                ["I469", "A021"],
                ["B2151ZZ"],
                "2026-04-01",
            ),
            ["286", "871"],
        )


if __name__ == "__main__":
    unittest.main()
