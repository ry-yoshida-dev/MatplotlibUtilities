from collections.abc import Sequence
from typing import Literal, TypedDict


class BoxplotKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by BoxplotParameters.to_dict.

    Each key is a field of BoxplotParameters; fields left as None are omitted.
    """

    orientation: Literal["vertical", "horizontal"]
    notch: bool
    whis: float | tuple[float, float]
    widths: float | Sequence[float]
    patch_artist: bool
    showmeans: bool
    meanline: bool
    showcaps: bool
    showbox: bool
    showfliers: bool
    zorder: float
