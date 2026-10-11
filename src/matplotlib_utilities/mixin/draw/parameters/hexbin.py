from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import HexbinKeywordArguments
from ....utils.color import MplColor
from .base import ArtistParameters, LabelParameters, NormParameters


@dataclass(frozen=True)
class HexbinParameters(
    NormParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[HexbinKeywordArguments],
):
    """
    Parameters for the hexagonal binning plot.

    Attributes:
    ----------
    # own
    gridsize: int | tuple[int, int] | None
        The number of hexagons along x, or along (x, y).
    mincnt: int | None
        Hide hexagons holding fewer points than this.
    extent: tuple[float, float, float, float] | None
        The binned region in data coordinates: (left, right, bottom, top).
    edgecolors: MplColor | None
        The color of the hexagon outlines.
    linewidths: float | None
        The width of the hexagon outlines.
    # inherited from NormParameters
    norm: Normalize | None
        The normalization applied before colormap mapping, for example a
        LogNorm for skewed counts.
    # inherited from CmapParameters
    cmap: ColorMap | None
        The colormap the hexagons are colored from.
    vmin: float | None
        The value mapped to the start of the colormap.
    vmax: float | None
        The value mapped to the end of the colormap.
    # inherited from LabelParameters
    label: str | None
        The label of the plot, used by the legend.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the hexagons.
    zorder: float | None
        The drawing order of the hexagons.
    """
    gridsize: int | tuple[int, int] | None = None
    mincnt: int | None = None
    extent: tuple[float, float, float, float] | None = None
    edgecolors: MplColor | None = None
    linewidths: float | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        match self.gridsize:
            case int() as hexagon_count if hexagon_count <= 0:
                raise ValueError("gridsize must be positive")
            case (x_count, y_count) if x_count <= 0 or y_count <= 0:
                raise ValueError("gridsize must be positive")
            case _:
                pass
        if self.mincnt is not None and self.mincnt < 0:
            raise ValueError("mincnt must be non-negative")
        if self.extent is not None and (self.extent[0] >= self.extent[1] or self.extent[2] >= self.extent[3]):
            raise ValueError("extent must be (left, right, bottom, top) with left < right and bottom < top")
        if self.linewidths is not None and self.linewidths < 0:
            raise ValueError("linewidths must be non-negative")
