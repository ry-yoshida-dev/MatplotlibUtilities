from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import ArrowStyle, Linestyle
from ....utils.color import MplColor
from ..keyword_arguments import ArrowPropertiesKeywordArguments


@dataclass(frozen=True)
class ArrowProperties(KeywordSubparameters[ArrowPropertiesKeywordArguments]):
    """
    Arrow drawn by an annotation, passed to Matplotlib as arrowprops.

    Attributes
    ----------
    arrowstyle: ArrowStyle
        The shape of the arrow.
    color: MplColor | None
        The color of the arrow.
    linewidth: float | None
        The width of the arrow line.
    linestyle: Linestyle | None
        The dash pattern of the arrow line.
    shrinkA: float | None
        The gap in points between the text and the start of the arrow.
    shrinkB: float | None
        The gap in points between the end of the arrow and the annotated point.
    alpha: float | None
        The alpha of the arrow.
    """

    arrowstyle: ArrowStyle = ArrowStyle.HEAD_AT_END
    color: MplColor | None = None
    linewidth: float | None = None
    linestyle: Linestyle | None = None
    shrinkA: float | None = None
    shrinkB: float | None = None
    alpha: float | None = None

    def __post_init__(self) -> None:
        if self.linewidth is not None and self.linewidth < 0:
            raise ValueError("linewidth must be non-negative")
        for name, gap in (("shrinkA", self.shrinkA), ("shrinkB", self.shrinkB)):
            if gap is not None and gap < 0:
                raise ValueError(f"{name} must be non-negative")
        if self.alpha is not None and not (0.0 <= self.alpha <= 1.0):
            raise ValueError("alpha must be between 0 and 1")
