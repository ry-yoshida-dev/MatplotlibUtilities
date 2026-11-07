"""
Re-export palette types from the color package and define the color types Matplotlib accepts.

MplColor is Matplotlib's ColorType: a color name, a hex string, or an RGB(A)
tuple of floats in 0-1. ScatterColorArg also accepts one value per point.
"""

from __future__ import annotations

from color import (
    ColorType,
    HexType,
    HsvFloatType,
    RgbaIntType,
    RgbFloatType,
    RgbIntType,
)
from matplotlib.typing import ColorType as MplColorType
from numpy.typing import ArrayLike

type MplColor = MplColorType
type ScatterColorArg = MplColor | ArrayLike

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
