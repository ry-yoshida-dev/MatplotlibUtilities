"""Enums for :meth:`matplotlib.axes.Axes.grid` keyword arguments."""

from __future__ import annotations

from enum import Enum


class GridWhich(Enum):
    """
    Which grid lines :meth:`matplotlib.axes.Axes.grid` affects.

    Attributes:
    ----------
    MAJOR: str
        Major grid lines.
    MINOR: str
        Minor grid lines.
    BOTH: str
        Both major and minor grid lines.
    """

    MAJOR = "major"
    MINOR = "minor"
    BOTH = "both"
    

class GridAxis(Enum):
    """
    Which axis :meth:`matplotlib.axes.Axes.grid` draws grid lines for.

    Attributes:
    ----------
    BOTH: str
        Both x and y axes.
    X: str
        X axis.
    Y: str
        Y axis.
    """

    BOTH = "both"
    X = "x"
    Y = "y"
