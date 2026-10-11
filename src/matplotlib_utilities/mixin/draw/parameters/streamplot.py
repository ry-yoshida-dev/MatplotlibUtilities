from dataclasses import dataclass

from matplotlib.colors import Normalize

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import StreamplotKeywordArguments
from ....utils import ArrowStyle, ColorMap, IntegrationDirection
from ....utils.color import MplColor


@dataclass(frozen=True)
class StreamplotParameters(KeywordSubparameters[StreamplotKeywordArguments]):
    """
    Parameters for the streamline plot.

    Attributes:
    ----------
    density: float | tuple[float, float] | None
        How closely the streamlines are packed, along both axes or along (x, y).
    linewidth: float | None
        The width of the streamlines.
    color: MplColor | None
        One color for every streamline. Leave unset to color by data instead.
    cmap: ColorMap | None
        The colormap used when the streamlines are colored by data.
    norm: Normalize | None
        The normalization used when the streamlines are colored by data.
    arrowsize: float | None
        The scaling factor of the arrow heads.
    arrowstyle: ArrowStyle | None
        The arrow style, for example "-|>" or "->".
    minlength: float | None
        The minimum streamline length in axes coordinates.
    maxlength: float | None
        The maximum streamline length in axes coordinates.
    integration_direction: IntegrationDirection | None
        The direction streamlines are traced from their seed points.
    broken_streamlines: bool | None
        Whether a streamline stops when it comes too close to another.
    zorder: float | None
        The drawing order of the streamlines.
    """
    density: float | tuple[float, float] | None = None
    linewidth: float | None = None
    color: MplColor | None = None
    cmap: ColorMap | None = None
    norm: Normalize | None = None
    arrowsize: float | None = None
    arrowstyle: ArrowStyle | None = None
    minlength: float | None = None
    maxlength: float | None = None
    integration_direction: IntegrationDirection | None = None
    broken_streamlines: bool | None = None
    zorder: float | None = None

    def __post_init__(self) -> None:
        match self.density:
            case float() | int() as packing if packing <= 0:
                raise ValueError("density must be positive")
            case (x_packing, y_packing) if x_packing <= 0 or y_packing <= 0:
                raise ValueError("density must be positive")
            case _:
                pass
        for name, value in (
            ("linewidth", self.linewidth),
            ("arrowsize", self.arrowsize),
            ("minlength", self.minlength),
            ("maxlength", self.maxlength),
        ):
            if value is not None and value <= 0:
                raise ValueError(f"{name} must be positive")
        if self.minlength is not None and self.maxlength is not None and self.minlength > self.maxlength:
            raise ValueError("minlength must be less than or equal to maxlength")
        if self.zorder is not None and self.zorder < 0:
            raise ValueError("zorder must be non-negative")
