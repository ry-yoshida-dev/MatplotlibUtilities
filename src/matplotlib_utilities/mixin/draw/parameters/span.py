from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import SpanKeywordArguments
from ....utils import Hatch, Linestyle
from ....utils.color import MplColor
from .base import ArtistParameters, ColorParameters, LabelParameters


@dataclass(frozen=True)
class SpanParameters(
    ColorParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[SpanKeywordArguments],
):
    """
    Parameters for a shaded band across the subplot.

    Attributes:
    ----------
    # own
    color: MplColor | None
        The color of both the face and the outline.
    linewidth: float | None
        The width of the outline.
    linestyle: Linestyle | None
        The style of the outline.
    hatch: Hatch | None
        The pattern drawn inside the face.
    # inherited from ColorParameters
    facecolor: MplColor | None
        The color of the face.
    edgecolor: MplColor | None
        The color of the outline.
    # inherited from LabelParameters
    label: str | None
        The label of the band, used by the legend.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the band.
    zorder: float | None
        The drawing order of the band.
    """
    color: MplColor | None = None
    linewidth: float | None = None
    linestyle: Linestyle | None = None
    hatch: Hatch | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.linewidth is not None and self.linewidth < 0:
            raise ValueError("linewidth must be non-negative")
