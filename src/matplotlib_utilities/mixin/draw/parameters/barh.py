from dataclasses import dataclass

from ....subparameter import Subparameters
from .base import ArtistParameters, ColorParameters, LabelParameters


@dataclass
class BarhParameters(
    ColorParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
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
    height: float | None = None
    left: float | None = None
    align: str | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.height is not None and self.height <= 0:
            raise ValueError("height must be positive")
