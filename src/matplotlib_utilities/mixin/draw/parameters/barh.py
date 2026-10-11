from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import BarAlign
from ..keyword_arguments import BarhKeywordArguments
from .base import ArtistParameters, ColorParameters, LabelParameters


@dataclass(frozen=True)
class BarhParameters(
    ColorParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[BarhKeywordArguments],
):
    """
    Parameters for the horizontal bar plot.

    Attributes:
    ----------
    # own
    height: float | None
        The height of the bars, measured across the category axis.
    left: float | None
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
    height: float | None = None
    left: float | None = None
    align: BarAlign | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.height is not None and self.height <= 0:
            raise ValueError("height must be positive")
