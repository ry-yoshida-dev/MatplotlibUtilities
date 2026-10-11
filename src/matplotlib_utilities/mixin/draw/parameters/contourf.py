from collections.abc import Sequence
from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import Hatch
from ..keyword_arguments import ContourfKeywordArguments
from .base import ArtistParameters, ContourLevelParameters


@dataclass(frozen=True)
class ContourfParameters(
    ContourLevelParameters,
    ArtistParameters,
    KeywordSubparameters[ContourfKeywordArguments],
):
    """
    Parameters for the filled contour plot.

    Attributes:
    ----------
    # own
    hatches: Sequence[Hatch | None] | None
        The patterns cycled over the filled bands; None leaves a band plain.
    # inherited from ContourLevelParameters
    levels: int | Sequence[float] | NumericArray | None
        The number of contour levels, or the levels themselves.
    colors: MplColor | Sequence[MplColor] | None
        One color for every band, or one color per band.
    extend: ColorbarExtend | None
        Whether values outside the levels are filled as well.
    # inherited from NormParameters
    norm: Normalize | None
        The normalization applied before colormap mapping.
    # inherited from CmapParameters
    cmap: ColorMap | None
        The colormap the bands are filled from.
    vmin: float | None
        The value mapped to the start of the colormap.
    vmax: float | None
        The value mapped to the end of the colormap.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the bands.
    zorder: float | None
        The drawing order of the bands.
    """
    hatches: Sequence[Hatch | None] | None = None
