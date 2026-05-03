from __future__ import annotations

from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils import GridAxis, GridWhich


@dataclass
class GridParameters(Subparameters):
    """
    Parameters for :meth:`matplotlib.axes.Axes.grid`.

    Attributes:
    ----------
    visible: bool
        Whether to show the grid.
    which: GridWhich
        Which grid lines to affect.
    axis: GridAxis
        Which axis to draw grid lines for.
    """

    visible: bool = True
    which: GridWhich = GridWhich.MAJOR
    axis: GridAxis = GridAxis.BOTH
