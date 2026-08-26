import json
import lzma
from collections import defaultdict
from dataclasses import dataclass
from importlib.resources import files


SCHEMA_VERSION = 1


@dataclass
class RuntimeData:
    dxmap: dict
    prmap: dict
    drgmap: dict
    ccmap: dict
    exmap: dict
    drg_exclusions: dict
    orpcsmap: dict
    surgical_rank: dict
    neoormap: dict


def encode_payload(payload):
    serialized = json.dumps(
        payload,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return lzma.compress(serialized, format=lzma.FORMAT_XZ, preset=6)


def decode_payload(encoded, expected_version=None):
    payload = json.loads(lzma.decompress(encoded))
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Unsupported drgpy runtime data schema")
    if expected_version is not None and payload.get("version") != expected_version:
        raise ValueError(
            f"Runtime data version mismatch: expected {expected_version!r}, "
            f"found {payload.get('version')!r}"
        )
    return payload


def load_runtime_data(version):
    resource = files("drgpy.runtime_data").joinpath(f"{version}.json.xz")
    try:
        payload = decode_payload(resource.read_bytes(), expected_version=version)
    except FileNotFoundError as exc:
        raise ValueError(f"Runtime data for MS-DRG version {version!r} is unavailable") from exc

    return RuntimeData(
        dxmap=defaultdict(list, payload["dxmap"]),
        prmap=defaultdict(list, payload["prmap"]),
        drgmap=payload["drgmap"],
        ccmap=payload["ccmap"],
        exmap={key: set(value) for key, value in payload["exmap"].items()},
        drg_exclusions={
            key: set(value)
            for key, value in payload["drg_exclusions"].items()
        },
        orpcsmap=payload["orpcsmap"],
        surgical_rank=payload["surgical_rank"],
        neoormap={code: 1 for code in payload["neoormap"]},
    )
