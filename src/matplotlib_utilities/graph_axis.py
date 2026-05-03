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
    def label_set_attribute(self) -> str:
        """
        Get the attribute to set the label.

        Returns
        -------
        str:
            The attribute to set the label.
        """
        match self:
            case GraphAxis.X:
                return "set_xlabel"
            case GraphAxis.Y:
                return "set_ylabel"

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

    @property
    def limit_set_attribute(self) -> str:
        """
        Get the attribute to set the limit.
        """
        match self:
            case GraphAxis.X:
                return "set_xlim"
            case GraphAxis.Y:
                return "set_ylim"
