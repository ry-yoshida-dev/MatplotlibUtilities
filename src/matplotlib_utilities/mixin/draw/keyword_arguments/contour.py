from collections.abc import Sequence
from typing import Literal, TypedDict

from matplotlib.colors import Normalize
from matplotlib.typing import LineStyleType

from ....types import NumericArray
from ....utils.color import MplColor


class ContourKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ContourParameters.to_dict.

    Each key is a field of ContourParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    cmap: str
    vmin: float
    vmax: float
    norm: Normalize
    levels: int | Sequence[float] | NumericArray
    colors: MplColor | Sequence[MplColor]
    extend: Literal["neither", "both", "min", "max"]
    linewidths: float
    linestyles: LineStyleType
