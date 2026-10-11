from __future__ import annotations

from enum import Enum


class GraphAxis(Enum):
    """
    Graph axis.

    Attributes:
    ----------
    X: str
        X axis.
    Y: str
        Y axis.
    """

    X = "x"
    Y = "y"

    @property
    def other_axis(self) -> GraphAxis:
        """
        Get the other axis.

        Returns
        -------
        GraphAxis:
            The other axis.
        """
        match self:
            case GraphAxis.X:
                return GraphAxis.Y
            case GraphAxis.Y:
                return GraphAxis.X
