from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import DrawStyle
from ..keyword_arguments import PlotKeywordArguments
from .base import ArtistParameters, LabelParameters, LineStyleParameters, MarkerLineParameters


@dataclass(frozen=True)
class PlotParameters(
    MarkerLineParameters,
    LineStyleParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[PlotKeywordArguments],
):
    """
    Parameters for the plot.

    Attributes
    ----------
    drawstyle: DrawStyle | None
        How neighboring points are connected.
    color, marker, markersize, markeredgewidth, markeredgecolor, markerfacecolor, solid_capstyle, solid_joinstyle
        Inherited from MarkerLineParameters.
    linewidth, linestyle, antialiased
        Inherited from LineStyleParameters.
    label
        Inherited from LabelParameters.
    alpha, zorder
        Inherited from ArtistParameters.
    """

    drawstyle: DrawStyle | None = None
