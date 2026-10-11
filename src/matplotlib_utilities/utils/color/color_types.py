"""Re-export palette types from the color package and define the color types Matplotlib accepts."""

from __future__ import annotations

from typing import TypeAlias

from color import ColorType, HexType, HsvFloatType, RgbFloatType, RgbIntType, RgbaIntType
from matplotlib.typing import ColorType as MplColorType
from numpy.typing import ArrayLike

MplColor: TypeAlias = MplColorType
ScatterColorArg: TypeAlias = MplColor | ArrayLike

__all__ = [
    "ColorType",
    "HexType",
    "HsvFloatType",
    "MplColor",
    "RgbFloatType",
    "RgbIntType",
    "RgbaIntType",
    "ScatterColorArg",
]
