from typing import TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class LineKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by LineParameters.to_dict.

    Each key is a field of LineParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    linewidth: float
    linestyle: LineStyleType
    antialiased: bool
    color: MplColor
