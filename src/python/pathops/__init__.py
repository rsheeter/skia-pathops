from ._pathops import (
    ArcSize,
    PathPen,
    Path,
    PathVerb,
    PathOp,
    FillType,
    op,
    simplify,
    OpBuilder,
    PathDirection,
    PathOpsError,
    UnsupportedVerbError,
    OpenPathError,
    bits2float,
    float2bits,
)

from .operations import (
    union,
    difference,
    intersection,
    xor,
)

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.0.0+unknown"
