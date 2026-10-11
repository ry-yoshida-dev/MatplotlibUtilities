from typing import Literal, TypedDict

from ....utils.color import MplColor


class LegendKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by LegendParameters.to_dict.

    Each key is a field of LegendParameters; fields left as None are omitted.
    """

    facecolor: MplColor
    edgecolor: MplColor
    loc: Literal[
        "best",
        "upper right",
        "upper left",
        "lower left",
        "lower right",
        "right",
        "center left",
        "center right",
        "lower center",
        "upper center",
        "center",
    ]
    bbox_to_anchor: tuple[float, ...]
    ncol: int
    fontsize: (
        float | Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large", "smaller", "larger"]
    )
    frameon: bool
    fancybox: bool
    shadow: bool
    framealpha: float
    title: str
    title_fontsize: (
        float | Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large", "smaller", "larger"]
    )
