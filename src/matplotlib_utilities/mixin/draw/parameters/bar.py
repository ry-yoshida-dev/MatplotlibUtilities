from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import BarAlign
from ..keyword_arguments import BarKeywordArguments
from .base import ArtistParameters, ColorParameters, LabelParameters


@dataclass(frozen=True)
class BarParameters(
    ColorParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[BarKeywordArguments],
):
    """
    Parameters for the bar plot.

    Attributes:
    ----------
    # own
    width: float | None
        The width of the bars, measured along the category axis.
    bottom: float | None
        The value each bar starts from.
    align: BarAlign | None
        Whether each bar is centered on its position or starts at it.
    # inherited from ColorParameters
    facecolor: MplColor | None
        The color of the face of the artist.
    edgecolor: MplColor | None
        The color of the edge of the artist.
    # inherited from LabelParameters
    label: str | None
        The label of the bars, used by the legend.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the bars.
    zorder: float | None
        The drawing order of the bars.
    """
    width: float | None = None
    bottom: float | None = None
    align: BarAlign | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.width is not None and self.width <= 0:
            raise ValueError("width must be positive")
