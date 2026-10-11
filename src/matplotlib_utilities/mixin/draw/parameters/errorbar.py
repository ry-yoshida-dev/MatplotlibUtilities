from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import ErrorbarKeywordArguments
from ....utils import Linestyle, Marker
from ....utils.color import MplColor
from .base import ArtistParameters, LabelParameters


@dataclass(frozen=True)
class ErrorbarParameters(
    LabelParameters,
    ArtistParameters,
    KeywordSubparameters[ErrorbarKeywordArguments],
):
    """
    Parameters for the error bar plot.

    Attributes:
    ----------
    # own
    color: MplColor | None
        The color of the data line and markers.
    marker: Marker | None
        The marker drawn at each data point.
    markersize: float | None
        The size of the markers.
    linestyle: Linestyle | None
        The style of the line joining the data points.
    linewidth: float | None
        The width of the line joining the data points.
    ecolor: MplColor | None
        The color of the error bars. Defaults to the data color.
    elinewidth: float | None
        The width of the error bars.
    capsize: float | None
        The length of the error bar caps in points.
    capthick: float | None
        The thickness of the error bar caps.
    barsabove: bool | None
        Whether the error bars are drawn above the markers.
    errorevery: int | None
        Draw an error bar on every n-th data point only.
    # inherited from LabelParameters
    label: str | None
        The label of the series, used by the legend.
    # inherited from ArtistParameters
    alpha: float | None
        The opacity of the series.
    zorder: float | None
        The drawing order of the series.
    """
    color: MplColor | None = None
    marker: Marker | None = None
    markersize: float | None = None
    linestyle: Linestyle | None = None
    linewidth: float | None = None
    ecolor: MplColor | None = None
    elinewidth: float | None = None
    capsize: float | None = None
    capthick: float | None = None
    barsabove: bool | None = None
    errorevery: int | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        for name, value in (
            ("markersize", self.markersize),
            ("linewidth", self.linewidth),
            ("elinewidth", self.elinewidth),
            ("capsize", self.capsize),
            ("capthick", self.capthick),
        ):
            if value is not None and value < 0:
                raise ValueError(f"{name} must be non-negative")
        if self.errorevery is not None and self.errorevery <= 0:
            raise ValueError("errorevery must be positive")
