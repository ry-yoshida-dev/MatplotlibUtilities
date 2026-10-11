from collections.abc import Sequence
from typing import Literal, TypedDict

from ....utils.color import MplColor


class HistKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by HistParameters.to_dict.

    Each key is a field of HistParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    bins: int | Sequence[float]
    range: tuple[float, float]
    density: bool
    cumulative: bool
    histtype: Literal["bar", "barstacked", "step", "stepfilled"]
    orientation: Literal["vertical", "horizontal"]
    rwidth: float
    log: bool
    stacked: bool
    color: MplColor | Sequence[MplColor]
    edgecolor: MplColor
    linewidth: float
