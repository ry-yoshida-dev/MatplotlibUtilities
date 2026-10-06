from collections.abc import Sequence
from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils.color import MplColor
from .wedge_style import WedgeStyle


@dataclass
class PieParameters(Subparameters):
    """
    Parameters for the pie chart.

    Attributes:
    ----------
    colors: Sequence[MplColor] | None
        One color per wedge. The property cycle is used when unset.
    explode: Sequence[float] | None
        One radial offset per wedge, as a fraction of the radius.
    autopct: str | None
        A printf-style format that writes each wedge's percentage inside it,
        for example "%1.1f%%".
    pctdistance: float | None
        The distance of the percentage text from the center, relative to the
        radius.
    labeldistance: float | None
        The distance of the labels from the center, relative to the radius.
    startangle: float | None
        The angle in degrees, counterclockwise from the x axis, where the
        first wedge starts.
    counterclock: bool | None
        Whether the wedges run counterclockwise.
    radius: float | None
        The radius of the pie.
    wedgeprops: WedgeStyle | None
        Styling applied to every wedge, including opacity and drawing order.
    """
    colors: Sequence[MplColor] | None = None
    explode: Sequence[float] | None = None
    autopct: str | None = None
    pctdistance: float | None = None
    labeldistance: float | None = None
    startangle: float | None = None
    counterclock: bool | None = None
    radius: float | None = None
    wedgeprops: WedgeStyle | None = None

    def __post_init__(self) -> None:
        if self.explode is not None and any(offset < 0 for offset in self.explode):
            raise ValueError("explode must hold non-negative offsets")
        if self.radius is not None and self.radius <= 0:
            raise ValueError("radius must be positive")
        if self.pctdistance is not None and self.pctdistance < 0:
            raise ValueError("pctdistance must be non-negative")
        if self.labeldistance is not None and self.labeldistance < 0:
            raise ValueError("labeldistance must be non-negative")
