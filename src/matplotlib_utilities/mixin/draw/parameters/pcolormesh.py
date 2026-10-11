from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import PcolormeshKeywordArguments
from ....utils import Shading
from ....utils.color import MplColor
from .base import ArtistParameters, NormParameters


@dataclass(frozen=True)
class PcolormeshParameters(
    NormParameters,
    ArtistParameters,
    KeywordSubparameters[PcolormeshKeywordArguments],
):
    """
    Parameters for the pseudocolor mesh.

    Attributes:
    ----------
    # own
    shading: Shading | None
        How each cell is filled and how the coordinates are read.
    edgecolors: MplColor | None
        The color of the cell outlines. Outlines are hidden when unset.
    linewidth: float | None
        The width of the cell outlines.
    antialiased: bool | None
        Whether the cell edges are antialiased.
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
        The opacity of the mesh.
    zorder: float | None
        The drawing order of the mesh.
    """
    shading: Shading | None = None
    edgecolors: MplColor | None = None
    linewidth: float | None = None
    antialiased: bool | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.linewidth is not None and self.linewidth < 0:
            raise ValueError("linewidth must be non-negative")
