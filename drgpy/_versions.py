from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, order=True)
class DRGVersion:
    major: int
    minor: int
    effective_date: date

    @property
    def name(self):
        suffix = f".{self.minor}" if self.minor else ""
        return f"v{self.major}{suffix}"

    @property
    def appendix_f_filename(self):
        return "appendix_F_J.txt" if self.major <= 40 else "appendix_F_I.txt"


SUPPORTED_VERSIONS = (
    DRGVersion(36, 0, date(2018, 10, 1)),
    DRGVersion(37, 0, date(2019, 10, 1)),
    DRGVersion(38, 0, date(2020, 10, 1)),
    DRGVersion(39, 0, date(2021, 10, 1)),
    DRGVersion(40, 0, date(2022, 10, 1)),
    DRGVersion(41, 0, date(2023, 10, 1)),
    DRGVersion(41, 1, date(2024, 4, 1)),
    DRGVersion(42, 0, date(2024, 10, 1)),
    DRGVersion(42, 1, date(2025, 4, 1)),
    DRGVersion(43, 0, date(2025, 10, 1)),
    DRGVersion(43, 1, date(2026, 4, 1)),
)

VERSION_BY_NAME = {version.name: version for version in SUPPORTED_VERSIONS}
LATEST_VERSION = SUPPORTED_VERSIONS[-1]


def get_version(value=None):
    if value is None:
        return LATEST_VERSION
    if isinstance(value, DRGVersion):
        return value
    try:
        return VERSION_BY_NAME[value]
    except KeyError as exc:
        supported = ", ".join(VERSION_BY_NAME)
        raise ValueError(f"Unsupported MS-DRG version {value!r}; choose one of: {supported}") from exc


def get_version_for_date(value):
    if isinstance(value, str):
        value = date.fromisoformat(value)
    matches = [version for version in SUPPORTED_VERSIONS if version.effective_date <= value]
    if not matches:
        raise ValueError(f"No bundled MS-DRG version covers {value.isoformat()}")
    return matches[-1]
