from collections.abc import Sequence
from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import HistKeywordArguments
from ....utils import HistType, Orientation
from ....utils.color import MplColor
from .base import ArtistParameters, LabelParameters


@dataclass(frozen=True)
class HistParameters(
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[HistKeywordArguments],
):
    """
    Parameters for the histogram.

    Attributes:
    ----------
    # own
    bins: int | Sequence[float] | None
        The number of equal-width bins, or the bin edges in increasing order.
    range: tuple[float, float] | None
        The lower and upper bounds of the bins. Values outside are ignored.
    density: bool | None
        Whether the bars show a probability density instead of counts.
    cumulative: bool | None
        Whether each bin also counts every bin before it.
    histtype: HistType | None
        The drawing style of the bars.
    orientation: Orientation | None
        Whether the bars stand vertically or run horizontally.
    rwidth: float | None
        The width of the bars as a fraction of the bin width.
    log: bool | None
        Whether the count axis is logarithmic.
    stacked: bool | None
        Whether several datasets are stacked on top of each other.
    color: MplColor | Sequence[MplColor] | None
        One color, or one color per dataset.
    edgecolor: MplColor | None
        The color of the bar outlines.
    linewidth: float | None
        The width of the bar outlines.
    # inherited from LabelParameters
    label: str | None
        The label of the histogram, used by the legend.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the bars.
    zorder: float | None
        The drawing order of the bars.
    """
    bins: int | Sequence[float] | None = None
    range: tuple[float, float] | None = None
    density: bool | None = None
    cumulative: bool | None = None
    histtype: HistType | None = None
    orientation: Orientation | None = None
    rwidth: float | None = None
    log: bool | None = None
    stacked: bool | None = None
    color: MplColor | Sequence[MplColor] | None = None
    edgecolor: MplColor | None = None
    linewidth: float | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        match self.bins:
            case int() as bin_count if bin_count <= 0:
                raise ValueError("bins must be positive when given as a count")
            case Sequence() as bin_edges if len(bin_edges) < 2:
                raise ValueError("bins must hold at least two edges")
            case _:
                pass
        if self.range is not None and self.range[0] >= self.range[1]:
            raise ValueError("range must be given as (lower, upper) with lower < upper")
        if self.rwidth is not None and not (0.0 < self.rwidth <= 1.0):
            raise ValueError("rwidth must be in (0, 1]")
        if self.linewidth is not None and self.linewidth < 0:
            raise ValueError("linewidth must be non-negative")
