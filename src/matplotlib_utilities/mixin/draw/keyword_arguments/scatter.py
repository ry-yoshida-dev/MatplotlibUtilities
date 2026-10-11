from collections.abc import Sequence
from typing import TypedDict

from numpy.typing import ArrayLike

from ....utils.color import MplColor, ScatterColorArg


class ScatterKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ScatterParameters.to_dict.

    Each key is a field of ScatterParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    cmap: str
    vmin: float
    vmax: float
    s: float | ArrayLike
    c: ScatterColorArg
    marker: str
    linewidths: float | Sequence[float]
    edgecolors: MplColor | Sequence[MplColor]
    plotnonfinite: bool
