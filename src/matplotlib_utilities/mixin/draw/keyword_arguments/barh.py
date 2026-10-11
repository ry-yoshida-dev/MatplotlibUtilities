from typing import Literal, TypedDict

from ....utils.color import MplColor


class BarhKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by BarhParameters.to_dict.

    Each key is a field of BarhParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    facecolor: MplColor
    edgecolor: MplColor
    height: float
    left: float
    align: Literal["center", "edge"]
