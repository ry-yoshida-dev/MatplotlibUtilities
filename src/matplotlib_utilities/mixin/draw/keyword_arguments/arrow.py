from typing import Literal, TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class ArrowKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ArrowParameters.to_dict.

    Each key is a field of ArrowParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    facecolor: MplColor
    edgecolor: MplColor
    linewidth: float
    linestyle: LineStyleType
    antialiased: bool
    width: float
    length_includes_head: bool
    head_width: float
    head_length: float
    shape: Literal["full", "left", "right"]
    overhang: float
    head_starts_at_zero: bool
    fill: bool
    color: MplColor
