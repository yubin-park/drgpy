from drgpy._versions import get_version_for_date
from drgpy.msdrg import DRGEngine


class DRGEngineAllVers:

    def __init__(self):
        self._engines = {}

    def get_engine(self, version):
        if version not in self._engines:
            self._engines[version] = DRGEngine(version=version)
        return self._engines[version]

    def get_drg(
            self,
            dx_lst,
            pr_lst,
            date,
            gender="F",
            is_alive=True,
            poa=None,
            discharge_status="01"):
        """Return the MS-DRG for the version effective on the supplied date."""
        version = get_version_for_date(date)
        return self.get_engine(version.name).get_drg(
            dx_lst,
            pr_lst,
            gender,
            is_alive,
            poa,
            discharge_status,
        )
