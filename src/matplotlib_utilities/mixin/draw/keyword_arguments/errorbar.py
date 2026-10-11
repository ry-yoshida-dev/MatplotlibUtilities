from typing import TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class ErrorbarKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ErrorbarParameters.to_dict.

    Each key is a field of ErrorbarParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    color: MplColor
    marker: str
    markersize: float
    linestyle: LineStyleType
    linewidth: float
    ecolor: MplColor
    elinewidth: float
    capsize: float
    capthick: float
    barsabove: bool
    errorevery: int
