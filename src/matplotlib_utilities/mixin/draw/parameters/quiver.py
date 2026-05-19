from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils import QuiverAngles, QuiverPivot, QuiverUnits
from ....utils.color import MplColor
from .base import ArtistParameters, CmapParameters, LabelParameters, LineStyleParameters


@dataclass
class QuiverParameters(
    CmapParameters,
    LabelParameters,
    LineStyleParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Parameters for :meth:`matplotlib.axes.Axes.quiver`.

    Attributes:
    ----------
    # own
    scale: float | None
        Data values per unit of arrow length; smaller values yield longer arrows.
    scale_units: QuiverUnits | None
        Physical unit used with ``scale`` for arrow length.
    units: QuiverUnits | None
        Physical unit for arrow shaft width (and head geometry).
    width: float | None
        Shaft width in arrow units.
    headwidth: float | None
        Head width as a multiple of shaft width.
    headlength: float | None
        Head length as a multiple of shaft width.
    headaxislength: float | None
        Head length at the shaft intersection as a multiple of shaft width.
    minshaft: float | None
        Length below which the arrow scales, in units of head length.
    minlength: float | None
        Minimum arrow length as a multiple of shaft width.
    angles: QuiverAngles | None
        How arrow angles are determined (``'uv'`` or ``'xy'``).
    pivot: QuiverPivot | None
        Part of the arrow anchored at each (X, Y) location.
    color: MplColor | None
        Explicit arrow colors (ignored when colormap data ``C`` is passed to quiver).
    # inherited from CmapParameters
    cmap: str | None
        Colormap name when ``C`` is passed to quiver.
    vmin: float | None
        Lower bound for colormap normalization.
    vmax: float | None
        Upper bound for colormap normalization.
    # inherited from LabelParameters
    label: str | None
        Label string for legend and other uses.
    # inherited from LineStyleParameters
    linewidth: float | None
        Edge line width of arrow polygons.
    linestyle: Linestyle | None
        Line style of arrow edges.
    antialiased: bool | None
        Whether to antialias arrow edges.
    facecolor: MplColor | None
        Fill color of arrow polygons.
    edgecolor: MplColor | None
        Edge color of arrow polygons.
    # inherited from ArtistParameters
    alpha: float | None
        Opacity of the arrows.
    zorder: float | None
        Drawing order of the arrows.
    """

    scale: float | None = None
    scale_units: QuiverUnits | None = None
    units: QuiverUnits | None = None
    width: float | None = None
    headwidth: float | None = None
    headlength: float | None = None
    headaxislength: float | None = None
    minshaft: float | None = None
    minlength: float | None = None
    angles: QuiverAngles | None = None
    pivot: QuiverPivot | None = None
    color: MplColor | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.scale is not None and self.scale <= 0:
            raise ValueError("scale must be positive")
        if self.width is not None and self.width <= 0:
            raise ValueError("width must be positive")
        for name in ("headwidth", "headlength", "headaxislength"):
            value = getattr(self, name)
            if value is not None and value <= 0:
                raise ValueError(f"{name} must be positive")
        if self.minshaft is not None and self.minshaft < 1:
            raise ValueError("minshaft must be at least 1")
        if self.minlength is not None and self.minlength < 1:
            raise ValueError("minlength must be at least 1")
