from typing import TypedDict

from matplotlib.typing import CapStyleType, DrawStyleType, JoinStyleType, LineStyleType

from ....utils.color import MplColor


class PlotKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by PlotParameters.to_dict.

    Each key is a field of PlotParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    label: str
    linewidth: float
    linestyle: LineStyleType
    antialiased: bool
    color: MplColor
    marker: str
    markersize: float
    markeredgewidth: float
    markeredgecolor: MplColor
    markerfacecolor: MplColor
    solid_capstyle: CapStyleType
    solid_joinstyle: JoinStyleType
    drawstyle: DrawStyleType
