from __future__ import absolute_import, division, print_function

from .taxonomy import (
    NCBITaxonomyDB,
    ALL_RANKS,
    DEFAULT_RANKS,
)
from .blast import (
    SeqID,
    BlastFile,
)


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = [
    "NCBITaxonomyDB",
    "BlastFile",
    "SeqID",
    "ALL_RANKS",
    "DEFAULT_RANKS",
]
