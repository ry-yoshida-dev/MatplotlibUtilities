from dataclasses import dataclass

from ....subparameter import Subparameters
from .base import ColorParameters


@dataclass
class BarhParameters(
    ColorParameters,
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
    label: str | None
        The label of the bars, used by the legend.
    # inherited from ColorParameters
    facecolor: MplColor | None
        The color of the face of the artist.
    edgecolor: MplColor | None
        The color of the edge of the artist.
    """
    height: float | None = None
    left: float | None = None
    align: str | None = None
    label: str | None = None
