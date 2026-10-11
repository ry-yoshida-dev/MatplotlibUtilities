from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class RowColumnIndex:
    """
    A class for accessing the row and column of the subplot.

    Attributes:
    ----------
    row: int
        The row of the subplot.
    column: int
        The column of the subplot.
    """
    row_index: int 
    column_index: int

    def __post_init__(self) -> None:
        if self.row_index < 0:
            raise ValueError("row_index must be greater than or equal to 0")
        if self.column_index < 0:
            raise ValueError("column_index must be greater than or equal to 0")

    @property
    def tuple(self) -> tuple[int, int]:
        """
        Get the tuple of index of the row and column.
        """
        return self.row_index, self.column_index
