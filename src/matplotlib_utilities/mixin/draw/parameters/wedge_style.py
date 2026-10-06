from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils.color import MplColor


@dataclass
class WedgeStyle(Subparameters):
    """
    Styling applied to every wedge of a pie chart (matplotlib wedgeprops).

    Attributes:
    ----------
    edgecolor: MplColor | None
        The color of the wedge outlines. A background color such as white
        separates neighboring wedges.
    linewidth: float | None
        The width of the wedge outlines.
    width: float | None
        The radial thickness of each wedge. A value below the pie radius
        turns the pie into a donut.
    alpha: float | None
        The opacity of the wedges.
    zorder: float | None
        The drawing order of the wedges.
    """
    edgecolor: MplColor | None = None
    linewidth: float | None = None
    width: float | None = None
    alpha: float | None = None
    zorder: float | None = None

    def __post_init__(self) -> None:
        if self.linewidth is not None and self.linewidth < 0:
            raise ValueError("linewidth must be non-negative")
        if self.width is not None and self.width <= 0:
            raise ValueError("width must be positive")
        if self.alpha is not None and not (0.0 <= self.alpha <= 1.0):
            raise ValueError("alpha must be between 0 and 1")
        if self.zorder is not None and self.zorder < 0:
            raise ValueError("zorder must be non-negative")
