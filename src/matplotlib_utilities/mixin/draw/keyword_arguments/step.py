from typing import Literal, TypedDict

from matplotlib.typing import CapStyleType, JoinStyleType, LineStyleType

from ....utils.color import MplColor


class StepKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by StepParameters.to_dict.

    Each key is a field of StepParameters; fields left as None are omitted.
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
    where: Literal["pre", "post", "mid"]
