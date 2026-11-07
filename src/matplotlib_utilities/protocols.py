"""Structural typing for graph makers consumed by draw/axis helpers."""

from __future__ import annotations

from typing import Protocol

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .types import SubplotAxesGrid
from .utils import SubplotIndex


class MakerCanvas(Protocol):
    """Structural type for hosts that expose fig, ax, and access_subplot."""

    fig: Figure
    ax: SubplotAxesGrid

    def access_subplot(self, index: SubplotIndex) -> Axes:
        """
        Return the Axes at the given subplot index.

        Parameters
        ----------
        index: SubplotIndex
            The subplot number in row-major order, or its row and column.
        """
        ...
