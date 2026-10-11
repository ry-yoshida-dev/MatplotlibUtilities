from typing import TypedDict

from matplotlib.colors import Normalize

from ....utils.color import MplColor


class HexbinKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by HexbinParameters.to_dict.

    Each key is a field of HexbinParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    cmap: str
    vmin: float
    vmax: float
    norm: Normalize
    gridsize: int | tuple[int, int]
    mincnt: int
    extent: tuple[float, float, float, float]
    edgecolors: MplColor
    linewidths: float
