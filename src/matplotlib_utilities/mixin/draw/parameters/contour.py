from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import ContourKeywordArguments
from ....utils import Linestyle
from .base import ArtistParameters, ContourLevelParameters


@dataclass(frozen=True)
class ContourParameters(
    ContourLevelParameters,
    ArtistParameters,
    KeywordSubparameters[ContourKeywordArguments],
):
    """
    Parameters for the contour line plot.

    Attributes:
    ----------
    # own
    linewidths: float | None
        The width of the contour lines.
    linestyles: Linestyle | None
        The style of the contour lines.
    # inherited from ContourLevelParameters
    levels: int | Sequence[float] | NumericArray | None
        The number of contour levels, or the levels themselves.
    colors: MplColor | Sequence[MplColor] | None
        One color for every level, or one color per level.
    extend: ColorbarExtend | None
        Whether values outside the levels are colored as well.
    # inherited from NormParameters
    norm: Normalize | None
        The normalization applied before colormap mapping.
    # inherited from CmapParameters
    cmap: ColorMap | None
        The colormap the levels are colored from.
    vmin: float | None
        The value mapped to the start of the colormap.
    vmax: float | None
        The value mapped to the end of the colormap.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the lines.
    zorder: float | None
        The drawing order of the lines.
    """
    linewidths: float | None = None
    linestyles: Linestyle | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.linewidths is not None and self.linewidths <= 0:
            raise ValueError("linewidths must be positive")
