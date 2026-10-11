from collections.abc import Sequence
from typing import Literal, TypedDict

from matplotlib.colors import Normalize

from ....types import NumericArray
from ....utils.color import MplColor


class ContourfKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ContourfParameters.to_dict.

    Each key is a field of ContourfParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    cmap: str
    vmin: float
    vmax: float
    norm: Normalize
    levels: int | Sequence[float] | NumericArray
    colors: MplColor | Sequence[MplColor]
    extend: Literal["neither", "both", "min", "max"]
    hatches: Sequence[Literal["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"] | None]
