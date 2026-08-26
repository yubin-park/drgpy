import argparse
from collections import defaultdict
from pathlib import Path

from drgpy import _appndxrdr as appndxrdr
from drgpy import _mdcsrdr as mdcsrdr
from drgpy._runtime_data import SCHEMA_VERSION, encode_payload
from drgpy._versions import SUPPORTED_VERSIONS, get_version


MDC_FILENAMES = (
    "mdcs_00_07.txt",
    "mdcs_08_11.txt",
    "mdcs_12_21.txt",
    "mdcs_22_25.txt",
)


def build_payload(version):
    version_info = get_version(version)
    version = version_info.name
    dxmap = defaultdict(list)
    prmap = defaultdict(list)
    for filename in MDC_FILENAMES:
        dxmap, prmap = mdcsrdr.read(
            f"data/{version}/{filename}",
            dxmap,
            prmap,
        )

    appendix_c = appndxrdr.read_c(f"data/{version}/appendix_C.txt")
    return {
        "schema_version": SCHEMA_VERSION,
        "version": version,
        "dxmap": dict(dxmap),
        "prmap": dict(prmap),
        "drgmap": appndxrdr.read_a(f"data/{version}/appendix_A.txt"),
        "ccmap": appendix_c.ccmap,
        "exmap": {
            key: sorted(value)
            for key, value in appendix_c.exmap.items()
        },
        "drg_exclusions": {
            key: sorted(value)
            for key, value in appendix_c.drg_exclusions.items()
        },
        "orpcsmap": appndxrdr.read_e(
            f"data/{version}/appendix_D_E.txt"
        ),
        "surgical_rank": appndxrdr.read_d(
            f"data/{version}/appendix_D_E.txt"
        ),
        "neoormap": sorted(
            appndxrdr.read_f(
                f"data/{version}/{version_info.appendix_f_filename}"
            )
        ),
    }


def build_snapshot(version, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"{version}.json.xz"
    destination.write_bytes(encode_payload(build_payload(version)))
    return destination


def main():
    parser = argparse.ArgumentParser(
        description="Generate deterministic compressed drgpy runtime datasets."
    )
    parser.add_argument(
        "versions",
        nargs="*",
        help="Versions to generate; defaults to every supported version.",
    )
    parser.add_argument(
        "--output-dir",
        default="drgpy/runtime_data",
        help="Destination directory for generated snapshots.",
    )
    args = parser.parse_args()
    versions = args.versions or [version.name for version in SUPPORTED_VERSIONS]
    for version in versions:
        destination = build_snapshot(version, args.output_dir)
        print(f"generated {destination}")


if __name__ == "__main__":
    main()
