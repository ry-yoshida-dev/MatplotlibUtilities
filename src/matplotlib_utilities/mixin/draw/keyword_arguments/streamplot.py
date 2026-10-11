from typing import Literal, TypedDict

from matplotlib.colors import Normalize

from ....types import NumericArray
from ....utils.color import MplColor


class StreamplotKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by StreamplotParameters.to_dict.

    Each key is a field of StreamplotParameters; fields left as None are omitted.
    color also accepts the per-point values that Streamplot draws through the
    colormap.
    """

    density: float | tuple[float, float]
    linewidth: float
    color: MplColor | NumericArray
    cmap: str
    norm: Normalize
    arrowsize: float
    arrowstyle: Literal[
        "-", "->", "<-", "<->", "-|>", "<|-", "<|-|>", "-[", "]-", "]-[", "|-|", "simple", "fancy", "wedge"
    ]
    minlength: float
    maxlength: float
    integration_direction: Literal["forward", "backward", "both"]
    broken_streamlines: bool
    zorder: float
