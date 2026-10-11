from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np

from .....types import NumericArray
from .....utils import ColorbarExtend
from .....utils.color import MplColor
from .norm import NormParameters


@dataclass(frozen=True)
class ContourLevelParameters(NormParameters):
    """
    Level and coloring options shared by line and filled contours.

    Attributes:
    ----------
    levels: int | Sequence[float] | NumericArray | None
        The number of contour levels, or the levels themselves in increasing
        order.
    colors: MplColor | Sequence[MplColor] | None
        One color for every level, or one color per level. It replaces the
        colormap, so cmap must stay unset.
    extend: ColorbarExtend | None
        Whether values outside the levels are colored as well.
    """

    levels: int | Sequence[float] | NumericArray | None = None
    colors: MplColor | Sequence[MplColor] | None = None
    extend: ColorbarExtend | None = None

    def __post_init__(self) -> None:
        match self.levels:
            case int() as level_count if level_count <= 0:
                raise ValueError("levels must be positive when given as a count")
            case int() | None:
                pass
            case level_values if bool(np.any(np.diff(np.asarray(level_values, dtype=float)) <= 0)):
                raise ValueError("levels must be strictly increasing")
            case _:
                pass
        if self.colors is not None and self.cmap is not None:
            raise ValueError("colors cannot be combined with cmap")
        super().__post_init__()
