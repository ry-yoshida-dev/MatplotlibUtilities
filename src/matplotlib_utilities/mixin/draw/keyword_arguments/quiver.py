from typing import Literal, TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class QuiverKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by QuiverParameters.to_dict.

    Each key is a field of QuiverParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    facecolor: MplColor
    edgecolor: MplColor
    linewidth: float
    linestyle: LineStyleType
    antialiased: bool
    label: str
    cmap: str
    vmin: float
    vmax: float
    scale: float
    scale_units: Literal["width", "height", "dots", "inches", "x", "y", "xy"]
    units: Literal["width", "height", "dots", "inches", "x", "y", "xy"]
    width: float
    headwidth: float
    headlength: float
    headaxislength: float
    minshaft: float
    minlength: float
    angles: Literal["uv", "xy"]
    pivot: Literal["tail", "mid", "middle", "tip"]
    color: MplColor
