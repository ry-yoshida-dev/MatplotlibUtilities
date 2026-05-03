from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils.color import MplColor
from .base import ArtistParameters, LabelParameters, LineStyleParameters


@dataclass
class LineParameters(
    LineStyleParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Parameters for the line.

    Attributes:
    ----------
    color: MplColor | None
        Line color (matplotlib ``color`` for ``axhline`` / ``axvline``).
    # inherited from LineStyleParameters
    linewidth: float | None
        The width of the line.
    linestyle: Linestyle | None
        The style of the line.
    antialiased: bool | None
        Whether to antialias the line.
    # inherited from LabelParameters
    label: str | None
        The label string.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha of the line.
    zorder: float | None
        The drawing order.
    """

    color: MplColor | None = None
