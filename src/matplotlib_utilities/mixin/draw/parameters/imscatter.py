from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils import ColorMap


@dataclass(frozen=True)
class ImscatterParameters(Subparameters):
    """
    Parameters for the image scatter plot.

    Attributes:
    ----------
    zoom: float
        The scale of each image relative to its pixel size.
    cmap: ColorMap | None
        The colormap applied to two-dimensional (grayscale) images.
    is_framed: bool
        Whether a frame is drawn around each image.
    zorder: float | None
        The drawing order of the images.
    """
    zoom: float = 1.0
    cmap: ColorMap | None = None
    is_framed: bool = False
    zorder: float | None = None

    def __post_init__(self) -> None:
        if self.zoom <= 0:
            raise ValueError("zoom must be positive")
        if self.zorder is not None and self.zorder < 0:
            raise ValueError("zorder must be non-negative")
