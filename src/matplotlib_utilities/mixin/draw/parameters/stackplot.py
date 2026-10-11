from collections.abc import Sequence
from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import StackplotKeywordArguments
from ....utils import StackBaseline
from ....utils.color import MplColor
from .base import ArtistParameters


@dataclass(frozen=True)
class StackplotParameters(
    ArtistParameters,
    KeywordSubparameters[StackplotKeywordArguments],
):
    """
    Parameters for the stacked area plot.

    Attributes:
    ----------
    # own
    colors: Sequence[MplColor] | None
        One color per layer. The property cycle is used when unset.
    baseline: StackBaseline | None
        The line the first layer is stacked from.
    edgecolor: MplColor | None
        The color of the layer outlines.
    linewidth: float | None
        The width of the layer outlines.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the layers.
    zorder: float | None
        The drawing order of the layers.
    """
    colors: Sequence[MplColor] | None = None
    baseline: StackBaseline | None = None
    edgecolor: MplColor | None = None
    linewidth: float | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.linewidth is not None and self.linewidth < 0:
            raise ValueError("linewidth must be non-negative")
