from __future__ import annotations

from enum import Enum


class TableAxis(Enum):
    """
    Table axis.

    Attributes:
    ----------
    ROW: str
        Row axis.
    COLUMN: str
        Column axis.
    """

    ROW = "row"
    COLUMN = "column"

    @property
    def other_axis(self) -> TableAxis:
        """
        Get the other axis.
        """
        match self:
            case TableAxis.ROW:
                return TableAxis.COLUMN
            case TableAxis.COLUMN:
                return TableAxis.ROW
