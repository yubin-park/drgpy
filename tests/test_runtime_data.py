import unittest
from importlib.resources import files

from drgpy._runtime_data import encode_payload, load_runtime_data
from drgpy._versions import SUPPORTED_VERSIONS
from tools.build_runtime_data import build_payload


class TestRuntimeData(unittest.TestCase):

    def test_all_supported_versions_have_snapshots(self):
        runtime_data = files("drgpy.runtime_data")
        expected = {f"{version.name}.json.xz" for version in SUPPORTED_VERSIONS}
        actual = {
            resource.name
            for resource in runtime_data.iterdir()
            if resource.name.endswith(".json.xz")
        }
        self.assertEqual(actual, expected)

    def test_generated_snapshots_are_current(self):
        runtime_data = files("drgpy.runtime_data")
        for version in SUPPORTED_VERSIONS:
            with self.subTest(version=version.name):
                expected = encode_payload(build_payload(version.name))
                actual = runtime_data.joinpath(
                    f"{version.name}.json.xz"
                ).read_bytes()
                self.assertEqual(actual, expected)

    def test_loaded_runtime_data_preserves_public_maps(self):
        for version in SUPPORTED_VERSIONS:
            with self.subTest(version=version.name):
                payload = build_payload(version.name)
                runtime_data = load_runtime_data(version.name)
                self.assertEqual(dict(runtime_data.dxmap), payload["dxmap"])
                self.assertEqual(dict(runtime_data.prmap), payload["prmap"])
                self.assertEqual(runtime_data.drgmap, payload["drgmap"])
                self.assertEqual(runtime_data.ccmap, payload["ccmap"])
                self.assertEqual(
                    runtime_data.exmap,
                    {
                        key: set(value)
                        for key, value in payload["exmap"].items()
                    },
                )
                self.assertEqual(
                    runtime_data.drg_exclusions,
                    {
                        key: set(value)
                        for key, value in payload["drg_exclusions"].items()
                    },
                )
                self.assertEqual(runtime_data.orpcsmap, payload["orpcsmap"])
                self.assertEqual(
                    runtime_data.surgical_rank,
                    payload["surgical_rank"],
                )
                self.assertEqual(
                    set(runtime_data.neoormap),
                    set(payload["neoormap"]),
                )

    def test_generated_snapshot_total_stays_small(self):
        runtime_data = files("drgpy.runtime_data")
        total_size = sum(
            len(resource.read_bytes())
            for resource in runtime_data.iterdir()
            if resource.name.endswith(".json.xz")
        )
        self.assertLess(total_size, 4 * 1024 * 1024)


if __name__ == "__main__":
    unittest.main()
