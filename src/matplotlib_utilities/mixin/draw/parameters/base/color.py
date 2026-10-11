from dataclasses import dataclass
from .....utils.color import MplColor


@dataclass(frozen=True)
class ColorParameters:
    """
    Base color parameters shared by patch-like artists.

    Attributes:
    ----------
    facecolor: MplColor | None
        The color of the face of the artist.
    edgecolor: MplColor | None
        The color of the edge of the artist.
    """
    facecolor: MplColor | None = None
    edgecolor: MplColor | None = None
