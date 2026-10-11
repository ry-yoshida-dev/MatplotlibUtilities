from typing import Literal, TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class SpanKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by SpanParameters.to_dict.

    Each key is a field of SpanParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    facecolor: MplColor
    edgecolor: MplColor
    color: MplColor
    linewidth: float
    linestyle: LineStyleType
    hatch: Literal["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]
