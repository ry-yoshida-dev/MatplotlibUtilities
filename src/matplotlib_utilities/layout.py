from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Iterator

from .utils import TableAxis

@dataclass
class GraphLayout:
    """
    A class for layouting the matplotlib graphs.

    Attributes:
    ----------
    number: int
        The number of subplots.
    column: int
        The number of columns in the subplots.
    row: int
        The number of rows in the subplots.
    """
    number: int
    column: int
    row: int

    def __post_init__(self):
        if self.number < 1:
            raise ValueError("number must be greater than 0")
        if self.column < 1:
            raise ValueError("column must be greater than or equal to 1")
        if self.row < 1:
            raise ValueError("row must be greater than or equal to 1")
        if self.number > self.column * self.row:
            raise ValueError("number must be less than or equal to column * row")
        if math.ceil(self.number/self.column) != self.row:
            raise ValueError("number must be divisible by column")
        if math.ceil(self.number/self.row) != self.column:
            raise ValueError("number must be divisible by row")

    def __iter__(self) -> Iterator[tuple[int, int]]:
        """
        Iterate over the layout.

        Returns
        -------
        Iterator[tuple[int, int]]:
            The iterator of the layout.
        """
        counter = 0
        for row in range(self.row):
            for column in range(self.column):
                counter += 1
                if counter > self.number:
                    break
                yield row, column

    def __len__(self):
        """
        Get the number of subplots.

        Returns
        -------
        int:
            The number of subplots.
        """
        return self.number

    @classmethod
    def from_number(
        cls, 
        number: int, 
        axis: TableAxis = TableAxis.COLUMN,
        axis_value: int = 1,
        ) -> GraphLayout:
        """
        Create a layout from the number and axis.
        
        Parameters
        ----------
        number: int
            The number of subplots.
        axis: TableAxis
            The axis to layout on.
        axis_value: int
            The value of the axis.

        Returns
        -------
        Layout:
            The layout of matplotlib graphs.
        """
        other_axis_value = math.ceil(number/axis_value)
        match axis:
            case TableAxis.COLUMN:
                return cls(
                    number=number, 
                    column=axis_value, 
                    row=other_axis_value
                    )
            case TableAxis.ROW:
                return cls(
                    number=number, 
                    column=other_axis_value, 
                    row=axis_value
                    )

    @classmethod
    def from_row_column(
        cls, 
        row: int, 
        column: int,
        ) -> GraphLayout:
        """
        Create a layout from the row and column.

        Parameters
        ----------
        row: int
            The number of rows in the subplots.
        column: int
            The number of columns in the subplots.

        Returns
        -------
        Layout:
            The layout of matplotlib graphs.
        """
        return cls(
            number=row * column, 
            column=column, 
            row=row
            )

    def from_row_column_to_number(
        self,
        row_index: int,
        column_index: int,
        ) -> int:
        """
        Create a number from the row and column.

        Parameters
        ----------
        row_index: int
            The index of the row.
        column_index: int
            The index of the column.

        Returns
        -------
        int:
            The number of the subplot.
        """
        self._validate_row_column_index(
            row_index=row_index, 
            column_index=column_index
            )
        number = row_index * self.column + column_index
        self._validate_number(number=number)
        return number

    def from_number_to_row_column_index(
        self,
        number: int,
        ) -> tuple[int, int]:
        """
        Create a row and column from the number.

        Parameters
        ----------
        number: int
            The number of the subplot.

        Returns
        -------
        tuple[int, int]:
            The row and column of the subplot.
        """
        self._validate_number(number=number)
        row = number // self.column
        column = number % self.column
        return row, column

    def _validate_number(
        self, 
        number: int
        ) -> None:
        """
        Validate the number.

        Parameters
        ----------
        number: int
            The number to validate.
        """
        if number < 0:
            raise ValueError(f"input number is out of range, got {number}")
        if number >= self.number:
            raise ValueError(f"input number is out of range, got {number}")
    
    def _validate_row_column_index(
        self, 
        row_index: int, 
        column_index: int
        ) -> None:
        """
        Validate the row and column index.

        Parameters
        ----------
        row_index: int
            The index of the row.
        column_index: int
            The index of the column.
        """
        if row_index < 0:
            raise ValueError(f"row index is out of range, got {row_index}")
        if row_index >= self.row:
            raise ValueError(f"row index is out of range, got {row_index}")
        if column_index < 0:
            raise ValueError(f"column index is out of range, got {column_index}")
        if column_index >= self.column:
            raise ValueError(f"column index is out of range, got {column_index}")