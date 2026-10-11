from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import LineKeywordArguments
from ....utils.color import MplColor
from .base import ArtistParameters, LabelParameters, LineStyleParameters


@dataclass(frozen=True)
class LineParameters(
    LineStyleParameters,
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[LineKeywordArguments],
):
    """
    Parameters for the line.

    Attributes:
    ----------
    color: MplColor | None
        Line color (matplotlib ``color`` for ``axhline`` / ``axvline``).
    # inherited from LineStyleParameters
    linewidth: float | None
        The width of the line.
    linestyle: Linestyle | None
        The style of the line.
    antialiased: bool | None
        Whether to antialias the line.
    # inherited from LabelParameters
    label: str | None
        The label string.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha of the line.
    zorder: float | None
        The drawing order.
    """

    color: MplColor | None = None
