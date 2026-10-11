from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ....utils import CoordinateSystem, FontSize, FontWeight, HorizontalAlignment, RotationMode, VerticalAlignment
from ....utils.color import MplColor
from ..keyword_arguments import AnnotateKeywordArguments
from .arrow_properties import ArrowProperties
from .base import ArtistParameters


@dataclass(frozen=True)
class AnnotateParameters(
    ArtistParameters,
    KeywordSubparameters[AnnotateKeywordArguments],
):
    """
    Optional keyword arguments for matplotlib.axes.Axes.annotate.

    Attributes
    ----------
    xycoords: CoordinateSystem | None
        The coordinate system that xy is given in. The offset systems are
        not accepted here.
    textcoords: CoordinateSystem | None
        The coordinate system that xytext is given in.
    arrowprops: ArrowProperties | None
        The arrow drawn from the text to the annotated point. None draws
        no arrow.
    annotation_clip: bool | None
        Whether to clip the annotation outside the axes area.
    color: MplColor | None
        The color of the text.
    fontsize: float | FontSize | None
        The size of the font, in points or as a named size.
    fontweight: FontWeight | int | None
        The weight of the font, as a named weight or a number from 0 to 1000.
    ha: HorizontalAlignment | None
        The horizontal alignment of the text.
    va: VerticalAlignment | None
        The vertical alignment of the text.
    rotation: float | None
        The rotation of the text in degrees.
    rotation_mode: RotationMode | None
        Whether the text is aligned before or after it is rotated.
    visible: bool | None
        Whether the annotation is visible.
    alpha, zorder
        Inherited from ArtistParameters.
    """

    xycoords: CoordinateSystem | None = None
    textcoords: CoordinateSystem | None = None
    arrowprops: ArrowProperties | None = None
    annotation_clip: bool | None = None
    color: MplColor | None = None
    fontsize: float | FontSize | None = None
    fontweight: FontWeight | int | None = None
    ha: HorizontalAlignment | None = None
    va: VerticalAlignment | None = None
    rotation: float | None = None
    rotation_mode: RotationMode | None = None
    visible: bool | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.xycoords is not None and self.xycoords.is_offset:
            raise ValueError("xycoords cannot be an offset system; offsets apply to textcoords only")
        if isinstance(self.fontsize, (int, float)) and self.fontsize <= 0:
            raise ValueError("fontsize must be positive")
        if isinstance(self.fontweight, int) and not (0 <= self.fontweight <= 1000):
            raise ValueError("fontweight must be between 0 and 1000 when given as a number")
