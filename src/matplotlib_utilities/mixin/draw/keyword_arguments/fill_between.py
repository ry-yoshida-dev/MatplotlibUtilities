from typing import Literal, TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class FillBetweenKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by FillBetweenParameters.to_dict.

    Each key is a field of FillBetweenParameters; fields left as None are omitted.
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
    step: Literal["pre", "post", "mid"]
    interpolate: bool
