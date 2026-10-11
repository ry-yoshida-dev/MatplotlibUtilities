from collections.abc import Sequence
from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import ViolinplotKeywordArguments
from ....utils import BandwidthMethod, Orientation
from ....utils.color import MplColor


@dataclass(frozen=True)
class ViolinplotParameters(KeywordSubparameters[ViolinplotKeywordArguments]):
    """
    Parameters for the violin plot.

    Attributes:
    ----------
    orientation: Orientation | None
        Whether the violins stand vertically or run horizontally.
    widths: float | Sequence[float] | None
        The maximum width of the violins, or one width per violin.
    showmeans: bool | None
        Whether a line marks the mean of each dataset.
    showmedians: bool | None
        Whether a line marks the median of each dataset.
    showextrema: bool | None
        Whether lines mark the minimum and maximum of each dataset.
    points: int | None
        The number of points the kernel density is evaluated at.
    bw_method: BandwidthMethod | float | None
        The rule that picks the kernel bandwidth, or the bandwidth factor.
    facecolor: MplColor | Sequence[MplColor] | None
        The fill color of the violins, or one color per violin.
    linecolor: MplColor | Sequence[MplColor] | None
        The color of the mean, median and extrema lines.
    """
    orientation: Orientation | None = None
    widths: float | Sequence[float] | None = None
    showmeans: bool | None = None
    showmedians: bool | None = None
    showextrema: bool | None = None
    points: int | None = None
    bw_method: BandwidthMethod | float | None = None
    facecolor: MplColor | Sequence[MplColor] | None = None
    linecolor: MplColor | Sequence[MplColor] | None = None

    def __post_init__(self) -> None:
        match self.widths:
            case float() | int() as violin_width if violin_width <= 0:
                raise ValueError("widths must be positive")
            case Sequence() as violin_widths if any(width <= 0 for width in violin_widths):
                raise ValueError("widths must be positive")
            case _:
                pass
        if self.points is not None and self.points < 2:
            raise ValueError("points must be at least 2")
        match self.bw_method:
            case float() | int() as bandwidth_factor if bandwidth_factor <= 0:
                raise ValueError("bw_method must be positive when given as a factor")
            case _:
                pass
