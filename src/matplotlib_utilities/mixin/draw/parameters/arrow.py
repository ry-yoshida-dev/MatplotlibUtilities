from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils import ArrowShape
from ....utils.color import MplColor
from .base import ArtistParameters, ColorParameters, LabelParameters, LineStyleParameters


@dataclass
class ArrowParameters(
    LineStyleParameters,
    ColorParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Optional keyword arguments for matplotlib.axes.Axes.arrow.

    Attributes:
    ----------
    # own
    width: float | None
        The width of the arrow.
    length_includes_head: bool | None
        Whether to include the head in the length.
    head_width: float | None
        The width of the head.
    head_length: float | None
        The length of the head.
    shape: ArrowShape | None
        The shape of the arrow.
    overhang: float | None
        The overhang of the arrow.
    head_starts_at_zero: bool | None
        Whether to start the head at zero.
    fill: bool | None
        Whether to fill the arrow.
    color: MplColor | None
        Shorthand that sets both face and edge color of the arrow patch
        (matplotlib ``color`` for ``Axes.arrow``). Takes precedence over
        ``facecolor`` / ``edgecolor`` when matplotlib resolves the artist.
    # inherited from LineStyleParameters
    linewidth: float | None
        The width of the arrow line.
    linestyle: Linestyle | None
        The style of the arrow line.
    antialiased: bool | None
        Whether to antialias the arrow.
    # inherited from ColorParameters
    facecolor: MplColor | None
        The fill color of the arrow patch.
    edgecolor: MplColor | None
        The edge color of the arrow patch.
    # inherited from LabelParameters
    label: str | None
        The label string for axis, legend, and other uses.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha of the arrow.
    zorder: float | None
        The drawing order.
    """

    width: float | None = None
    length_includes_head: bool | None = None
    head_width: float | None = None
    head_length: float | None = None
    shape: ArrowShape | None = None
    overhang: float | None = None
    head_starts_at_zero: bool | None = None
    fill: bool | None = None
    color: MplColor | None = None

    def __post_init__(self) -> None:
        """
        Validate parameters after initialization.
        """
        super().__post_init__()
        if self.width is not None and self.width <= 0:
            raise ValueError("width must be positive")
        if self.head_width is not None and self.head_width <= 0:
            raise ValueError("head_width must be positive")
        if self.head_length is not None and self.head_length <= 0:
            raise ValueError("head_length must be positive")
        if self.overhang is not None and self.overhang <= 0:
            raise ValueError("overhang must be positive")
