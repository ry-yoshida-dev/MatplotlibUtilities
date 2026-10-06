from dataclasses import dataclass

from ....subparameter import Subparameters
from .base import ArtistParameters, ColorParameters, LabelParameters


@dataclass
class BarParameters(
    ColorParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
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
    align: str | None
        The alignment of the bars against their tick positions.
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
    align: str | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.width is not None and self.width <= 0:
            raise ValueError("width must be positive")
