from collections.abc import Sequence
from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import BoxplotKeywordArguments
from ....utils import Orientation


@dataclass(frozen=True)
class BoxplotParameters(KeywordSubparameters[BoxplotKeywordArguments]):
    """
    Parameters for the box plot.

    Attributes:
    ----------
    orientation: Orientation | None
        Whether the boxes stand vertically or run horizontally.
    notch: bool | None
        Whether each box is notched around a confidence interval of its median.
    whis: float | tuple[float, float] | None
        The whisker reach, as a multiple of the interquartile range, or as the
        (lower, upper) percentiles the whiskers end at.
    widths: float | Sequence[float] | None
        The width of the boxes, or one width per box.
    patch_artist: bool | None
        Whether the boxes are drawn as filled patches instead of outlines.
    showmeans: bool | None
        Whether the mean of each dataset is marked.
    meanline: bool | None
        Whether the mean is drawn as a line across the box instead of a marker.
    showcaps: bool | None
        Whether caps are drawn at the ends of the whiskers.
    showbox: bool | None
        Whether the boxes are drawn.
    showfliers: bool | None
        Whether the outliers beyond the whiskers are drawn.
    zorder: float | None
        The drawing order of the boxes.
    """
    orientation: Orientation | None = None
    notch: bool | None = None
    whis: float | tuple[float, float] | None = None
    widths: float | Sequence[float] | None = None
    patch_artist: bool | None = None
    showmeans: bool | None = None
    meanline: bool | None = None
    showcaps: bool | None = None
    showbox: bool | None = None
    showfliers: bool | None = None
    zorder: float | None = None

    def __post_init__(self) -> None:
        match self.whis:
            case (lower_percentile, upper_percentile):
                if not (0.0 <= lower_percentile < upper_percentile <= 100.0):
                    raise ValueError("whis percentiles must satisfy 0 <= lower < upper <= 100")
            case float() | int() as whisker_reach if whisker_reach < 0:
                raise ValueError("whis must be non-negative")
            case _:
                pass
        match self.widths:
            case float() | int() as box_width if box_width <= 0:
                raise ValueError("widths must be positive")
            case Sequence() as box_widths if any(width <= 0 for width in box_widths):
                raise ValueError("widths must be positive")
            case _:
                pass
        if self.zorder is not None and self.zorder < 0:
            raise ValueError("zorder must be non-negative")
