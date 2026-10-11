from typing import Literal, TypedDict

from matplotlib.colors import Normalize


class ImshowKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ImshowParameters.to_dict.

    Each key is a field of ImshowParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    cmap: str
    vmin: float
    vmax: float
    norm: Normalize
    aspect: Literal["equal", "auto"] | float
    interpolation: Literal[
        "none",
        "nearest",
        "bilinear",
        "bicubic",
        "spline16",
        "spline36",
        "hanning",
        "hamming",
        "hermite",
        "kaiser",
        "quadric",
        "catrom",
        "gaussian",
        "bessel",
        "mitchell",
        "sinc",
        "lanczos",
        "blackman",
    ]
    interpolation_stage: Literal["auto", "data", "rgba"]
    origin: Literal["upper", "lower"]
    extent: tuple[float, float, float, float]
    filternorm: bool
    filterrad: float
    resample: bool
    url: str
