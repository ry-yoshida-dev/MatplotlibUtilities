from typing import Literal, TypedDict

from matplotlib.colors import Normalize

from ....utils.color import MplColor


class PcolormeshKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by PcolormeshParameters.to_dict.

    Each key is a field of PcolormeshParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    cmap: str
    vmin: float
    vmax: float
    norm: Normalize
    shading: Literal["flat", "nearest", "gouraud", "auto"]
    edgecolors: MplColor
    linewidth: float
    antialiased: bool
