from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class SubplotNumber:
    """
    A class for accessing the number of the subplot.

    Attributes:
    ----------
    number: int
        The number of the subplot.
    """
    number: int
    row_index: int

    def __post_init__(self) -> None:
        if self.number < 0:
            raise ValueError("number must be greater than or equal to 0")

    @property
    def column(self) -> int:
        """
        Get the column index of the subplot.

        Returns
        -------
        int:
            The column index of the subplot.
        """
        return self.number // (self.row_index + 1)

    @property
    def tuple(self) -> tuple[int, int]:
        """
        Get the tuple of the row and column.
        
        Returns
        -------
        tuple[int, int]:
            The tuple of the row index and column index.
        """
        return self.row_index, self.column