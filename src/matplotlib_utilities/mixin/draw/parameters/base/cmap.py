from __future__ import annotations

import math
from dataclasses import dataclass

from .....utils import ColorMap


@dataclass(frozen=True)
class CmapParameters:
    """
    Parameters for colormap scaling (cmap, vmin, vmax).

    Attributes
    ----------
    cmap: ColorMap | None
        The colormap that maps values to colors.
    vmin: float | None
        The value mapped to the lowest color.
    vmax: float | None
        The value mapped to the highest color.
    """

    cmap: ColorMap | None = None
    vmin: float | None = None
    vmax: float | None = None

    def __post_init__(self) -> None:
        self._validate_values()
        post_init = getattr(super(), "__post_init__", None)
        if callable(post_init):
            _ = post_init()

    def _validate_values(self) -> None:
        vmin = self.vmin
        vmax = self.vmax
        if vmin is None or vmax is None:
            return

        vmin, vmax = float(vmin), float(vmax)
        for name, value in (("vmin", vmin), ("vmax", vmax)):
            if not math.isfinite(value):
                raise ValueError(f"{name} must be finite")
        if vmin > vmax:
            raise ValueError("vmin must be less than or equal to vmax")
