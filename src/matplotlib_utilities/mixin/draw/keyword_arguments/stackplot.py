from collections.abc import Sequence
from typing import Literal, TypedDict

from ....utils.color import MplColor


class StackplotKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by StackplotParameters.to_dict.

    Each key is a field of StackplotParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    colors: Sequence[MplColor]
    baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"]
    edgecolor: MplColor
    linewidth: float
