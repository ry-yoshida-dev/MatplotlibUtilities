from typing import TypedDict

from matplotlib.colors import Normalize


class Hist2dKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by Hist2dParameters.to_dict.

    Each key is a field of Hist2dParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    cmap: str
    vmin: float
    vmax: float
    norm: Normalize
    bins: int | tuple[int, int]
    range: tuple[tuple[float, float], tuple[float, float]]
    density: bool
    cmin: float
    cmax: float
