from dataclasses import dataclass

from .....utils import CapStyle, JoinStyle, Marker
from .....utils.color import MplColor


@dataclass(frozen=True)
class MarkerLineParameters:
    """
    Marker and line-end options shared by line plots and step plots.

    Attributes
    ----------
    color: MplColor | None
        The color of the line.
    marker: Marker | None
        The marker drawn at each point.
    markersize: float | None
        The size of the markers.
    markeredgewidth: float | None
        The width of the marker edges.
    markeredgecolor: MplColor | None
        The color of the marker edges.
    markerfacecolor: MplColor | None
        The color of the marker faces.
    solid_capstyle: CapStyle | None
        How the ends of a solid line are drawn.
    solid_joinstyle: JoinStyle | None
        How the corners of a solid line are drawn.
    """

    color: MplColor | None = None
    marker: Marker | None = None
    markersize: float | None = None
    markeredgewidth: float | None = None
    markeredgecolor: MplColor | None = None
    markerfacecolor: MplColor | None = None
    solid_capstyle: CapStyle | None = None
    solid_joinstyle: JoinStyle | None = None

    def __post_init__(self) -> None:
        if self.markersize is not None and self.markersize <= 0:
            raise ValueError("markersize must be positive")
        if self.markeredgewidth is not None and self.markeredgewidth <= 0:
            raise ValueError("markeredgewidth must be positive")
        post_init = getattr(super(), "__post_init__", None)
        if callable(post_init):
            _ = post_init()
