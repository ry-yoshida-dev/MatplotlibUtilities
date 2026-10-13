from typing import Literal, TypedDict

from ....types import NumericArray
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
    bottom: float | NumericArray
    align: Literal["center", "edge"]
