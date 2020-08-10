from ._version import get_versions
from sfrmaker.gis import CRS
from sfrmaker.grid import StructuredGrid, UnstructuredGrid
from sfrmaker.lines import Lines
from sfrmaker.mf5to6 import Mf6SFR
from sfrmaker.rivdata import RivData
from sfrmaker.sfrdata import SFRData

__version__ = get_versions()['version']
del get_versions

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
