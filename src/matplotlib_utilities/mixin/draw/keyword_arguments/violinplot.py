from collections.abc import Sequence
from typing import Literal, TypedDict

from ....utils.color import MplColor


class ViolinplotKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ViolinplotParameters.to_dict.

    Each key is a field of ViolinplotParameters; fields left as None are omitted.
    """

    orientation: Literal["vertical", "horizontal"]
    widths: float | Sequence[float]
    showmeans: bool
    showmedians: bool
    showextrema: bool
    points: int
    bw_method: Literal["scott", "silverman"] | float
    facecolor: MplColor | Sequence[MplColor]
    linecolor: MplColor | Sequence[MplColor]
