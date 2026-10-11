from dataclasses import dataclass

from matplotlib.colors import Normalize

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import ImshowKeywordArguments
from ....utils import Aspect, InterpolationMethod, InterpolationStage, Origin
from .base import ArtistParameters, CmapParameters


@dataclass(frozen=True)
class ImshowParameters(
    CmapParameters,
    ArtistParameters,
    KeywordSubparameters[ImshowKeywordArguments],
):
    """
    Parameters for the imshow plot.

    Attributes:
    ----------
    # own
    norm: Normalize | None
        Data normalization before colormap mapping.
    aspect: Aspect | float | None
        The aspect ratio of the axes.
    interpolation: InterpolationMethod | None
        The interpolation method used for resampling.
    interpolation_stage: InterpolationStage | None
        The stage at which interpolation is performed.
    origin: Origin | None
        Place the [0, 0] index of the array in upper left or lower left.
    extent: tuple[float, float, float, float] | None
        Bounding box in data coordinates: (left, right, bottom, top).
    filternorm: bool
        Parameter for the antigrain image resize filter.
    filterrad: float
        Filter radius for filters that have a radius parameter.
    resample: bool
        Whether to use full resampling.
    url: str | None
        URL of the created AxesImage.
    # inherited from CmapParameters
    cmap: ColorMap | None
        The colormap name used to convert normalized values to RGBA.
    vmin: float | None
        The lower bound of the data range mapped to the colormap minimum.
    vmax: float | None
        The upper bound of the data range mapped to the colormap maximum.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha blending value between 0 and 1.
    zorder: float | None
        Drawing order of the image.
    """

    norm: Normalize | None = None
    aspect: Aspect | float | None = None
    interpolation: InterpolationMethod | None = None
    interpolation_stage: InterpolationStage | None = None
    origin: Origin | None = None
    extent: tuple[float, float, float, float] | None = None
    filternorm: bool = True
    filterrad: float = 4.0
    resample: bool = True
    url: str | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.filterrad <= 0:
            raise ValueError("filterrad must be greater than 0")
        if self.extent is not None and len(self.extent) != 4:
            raise ValueError("extent must be a tuple of 4 floats: (left, right, bottom, top)")
