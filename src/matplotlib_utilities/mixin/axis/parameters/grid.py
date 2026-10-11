from __future__ import annotations

from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import GridKeywordArguments
from ....utils import GridAxis, GridWhich


@dataclass(frozen=True)
class GridParameters(KeywordSubparameters[GridKeywordArguments]):
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
    alpha: float
        The alpha of the grid lines.
    """

    visible: bool = True
    which: GridWhich = GridWhich.MAJOR
    axis: GridAxis = GridAxis.BOTH
    alpha: float = 1.0
