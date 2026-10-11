from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import StepWhere
from ..keyword_arguments import StepKeywordArguments
from .base import ArtistParameters, LabelParameters, LineStyleParameters, MarkerLineParameters


@dataclass(frozen=True)
class StepParameters(
    MarkerLineParameters,
    LineStyleParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[StepKeywordArguments],
):
    """
    Parameters for the step plot.

    The step plot sets the draw style from where, so unlike PlotParameters
    it has no drawstyle field.

    Attributes
    ----------
    where: StepWhere | None
        Where each step changes level relative to its x position.
    color, marker, markersize, markeredgewidth, markeredgecolor, markerfacecolor, solid_capstyle, solid_joinstyle
        Inherited from MarkerLineParameters.
    linewidth, linestyle, antialiased
        Inherited from LineStyleParameters.
    label
        Inherited from LabelParameters.
    alpha, zorder
        Inherited from ArtistParameters.
    """

    where: StepWhere | None = None
