from collections.abc import Sequence
from typing import TypedDict

from matplotlib.ticker import Formatter, Locator


class ColorbarKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ColorbarParameters.colorbar_keyword_arguments.

    Each key is a field of ColorbarParameters that Figure.colorbar accepts;
    fields left as None are omitted.
    """

    location: str
    extend: str
    extendfrac: float | tuple[float, float]
    extendrect: bool
    ticks: Sequence[float] | Locator
    format: str | Formatter
    drawedges: bool
    boundaries: Sequence[float]
    values: Sequence[float]
    spacing: str
    label: str
    alpha: float
