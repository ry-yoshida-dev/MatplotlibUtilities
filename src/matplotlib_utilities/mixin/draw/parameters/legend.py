from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import FontSize, LegendLocation
from ..keyword_arguments import LegendKeywordArguments
from .base import ColorParameters


@dataclass(frozen=True)
class LegendParameters(
    ColorParameters,
    KeywordSubparameters[LegendKeywordArguments],
):
    """
    Parameters for the legend.

    Attributes:
    ----------
    # own
    loc: LegendLocation | None
        The location of the legend.
    bbox_to_anchor: tuple | None
        Box that is used to position the legend in conjunction with loc.
    ncol: int | None
        The number of columns that the legend has.
    fontsize: float | FontSize | None
        The font size of the legend.
    frameon: bool | None
        Whether the legend should be drawn on a frame.
    fancybox: bool | None
        Whether round edges should be enabled around the legend background.
    shadow: bool | None
        Whether to draw a shadow behind the legend.
    framealpha: float | None
        The alpha transparency of the legend background.
    title: str | None
        The legend title.
    title_fontsize: float | FontSize | None
        The font size of the legend title.
    # inherited from ColorParameters
    facecolor: MplColor | None
        The background color of the legend frame.
    edgecolor: MplColor | None
        The border color of the legend frame.
    """

    loc: LegendLocation | None = None
    bbox_to_anchor: tuple[float, ...] | None = None
    ncol: int | None = None
    fontsize: float | FontSize | None = None
    frameon: bool | None = None
    fancybox: bool | None = None
    shadow: bool | None = None
    framealpha: float | None = None
    title: str | None = None
    title_fontsize: float | FontSize | None = None
