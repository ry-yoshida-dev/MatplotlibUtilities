from typing import Literal, TypedDict

from ....utils.color import MplColor


class BarKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by BarParameters.to_dict.

    Each key is a field of BarParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    facecolor: MplColor
    edgecolor: MplColor
    width: float
    bottom: float
    align: Literal["center", "edge"]
