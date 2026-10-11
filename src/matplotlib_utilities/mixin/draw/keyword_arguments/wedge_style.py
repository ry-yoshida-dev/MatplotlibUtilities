from typing import TypedDict

from ....utils.color import MplColor


class WedgeStyleKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by WedgeStyle.to_dict.

    Each key is a field of WedgeStyle; fields left as None are omitted.
    """

    edgecolor: MplColor
    linewidth: float
    width: float
    alpha: float
    zorder: float
