from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import Hist2dKeywordArguments
from .base import ArtistParameters, NormParameters


@dataclass(frozen=True)
class Hist2dParameters(
    NormParameters,
    ArtistParameters,
    KeywordSubparameters[Hist2dKeywordArguments],
):
    """
    Parameters for the two-dimensional histogram.

    Attributes:
    ----------
    # own
    bins: int | tuple[int, int] | None
        The number of bins along both axes, or along (x, y).
    range: tuple[tuple[float, float], tuple[float, float]] | None
        The bounds of the bins as ((xmin, xmax), (ymin, ymax)).
    density: bool | None
        Whether the cells show a probability density instead of counts.
    cmin: float | None
        Hide cells whose count is below this.
    cmax: float | None
        Hide cells whose count is above this.
    # inherited from NormParameters
    norm: Normalize | None
        The normalization applied before colormap mapping.
    # inherited from CmapParameters
    cmap: ColorMap | None
        The colormap the cells are colored from.
    vmin: float | None
        The value mapped to the start of the colormap.
    vmax: float | None
        The value mapped to the end of the colormap.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the cells.
    zorder: float | None
        The drawing order of the cells.
    """
    bins: int | tuple[int, int] | None = None
    range: tuple[tuple[float, float], tuple[float, float]] | None = None
    density: bool | None = None
    cmin: float | None = None
    cmax: float | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        match self.bins:
            case int() as bin_count if bin_count <= 0:
                raise ValueError("bins must be positive")
            case (x_count, y_count) if x_count <= 0 or y_count <= 0:
                raise ValueError("bins must be positive")
            case _:
                pass
        if self.range is not None and any(lower >= upper for lower, upper in self.range):
            raise ValueError("range must be ((xmin, xmax), (ymin, ymax)) with each min < max")
        if self.cmin is not None and self.cmax is not None and self.cmin > self.cmax:
            raise ValueError("cmin must be less than or equal to cmax")
