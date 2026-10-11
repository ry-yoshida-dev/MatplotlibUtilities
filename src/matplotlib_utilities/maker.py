# pyright: reportUnknownMemberType=false

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.typing import RcKeyType

from .types import SubplotAxesGrid

from .utils import (
    SubplotIndex,
    RowColumnIndex,
    )
from .layout import GraphLayout
from .parameter import GraphParameters
from .mixin.axis import AxisMixin
from .mixin.draw import DrawMixin

GLOBAL_STYLE_KEYS: tuple[RcKeyType, ...] = ("font.size", "font.family")


class MatplotGraphMaker(DrawMixin, AxisMixin):
    """
    A class for making matplotlib graphs.

    Attributes:
    ----------
    layout: GraphLayout
        The layout of the matplotlib graphs.
    parameters: GraphParameters
        The parameters for the MatplotGraphMaker.
    fig: Figure
        The figure of the matplotlib graphs.
    ax: SubplotAxesGrid
        The axes of the matplotlib graphs, indexed as ax[row][column].
    """
    def __init__(
        self,
        layout: GraphLayout | None = None,
        parameters: GraphParameters | None = None
        ) -> None:
        """
        Initialize the MatplotGraphMaker.

        Parameters
        ----------
        layout: GraphLayout
            The layout of the matplotlib graphs.
        parameters: GraphParameters
            The parameters for the MatplotGraphMaker.
        """
        self.layout: GraphLayout = layout or GraphLayout(number=1, column=1, row=1)
        self.parameters: GraphParameters = parameters or GraphParameters()
        self._original_style: dict[RcKeyType, object] = {key: plt.rcParams[key] for key in GLOBAL_STYLE_KEYS}
        self.fig: Figure = self._create_figure()
        self.ax: SubplotAxesGrid = self._create_axes_grid()

    def finalize(
        self,
        save_path: str | None = None,
        is_showing_result_enabled: bool = True
        ) -> None:
        """
        Finalize the matplotlib graphs.

        Hides the unused cells of the grid, saves the figure, shows it, then
        closes it and restores the global font settings changed for it.
        Showing blocks until the window is closed when run as a script.

        Parameters
        ----------
        save_path: str | None = None
            The path to save the figure.
        is_showing_result_enabled: bool = True
            Whether to show the result.
        """
        self.hide_unused_subplots()
        self.fig.subplots_adjust(
            wspace=self.parameters.w_space,
            hspace=self.parameters.h_space,
        )
        if save_path is not None:
            self.fig.savefig(save_path, bbox_inches="tight")
        if is_showing_result_enabled:
            plt.show()
        if not is_showing_result_enabled or not plt.isinteractive():
            plt.close(self.fig)
        plt.rcParams.update(self._original_style)

    def set_figure_title(self, title: str) -> None:
        """
        Set the title of the whole figure, above every subplot.

        Parameters
        ----------
        title: str
            The title text.
        """
        _ = self.fig.suptitle(title)

    def hide_unused_subplots(self) -> None:
        """
        Hide the cells of the grid that hold no subplot.

        A layout whose number of subplots does not fill its rows, such as 5
        subplots on 2 rows of 3, leaves empty axes in the last row. Hiding
        them removes their frames and ticks.
        """
        for number in range(self.layout.number, self.layout.row * self.layout.column):
            row_index, column_index = divmod(number, self.layout.column)
            self.ax[row_index][column_index].set_axis_off()

    def get_subplot_index_from_number(
        self,
        number: int
        ) -> SubplotIndex:
        """
        Get the subplot index from the number.

        Parameters
        ----------
        number: int
            The number of the subplot.
        """
        row_index, column_index = self.layout.from_number_to_row_column_index(number=number)
        return RowColumnIndex(
            row_index=row_index,
            column_index=column_index
            )

    def get_subplot_index_from_row_column(
        self,
        row_index: int,
        column_index: int
        ) -> SubplotIndex:
        """
        Get the subplot index from the row and column.

        Parameters
        ----------
        row_index: int
            The index of the row.
        column_index: int
            The index of the column.
        """
        return RowColumnIndex(
            row_index=row_index,
            column_index=column_index
            )

    def access_subplot(self, index: SubplotIndex) -> Axes:
        """
        Return the :class:`~matplotlib.axes.Axes` at the given subplot index.

        Used by drawing helpers; library users may call
        this for direct axes access.

        Parameters
        ----------
        index: SubplotIndex
            The subplot number in row-major order, or its row and column.

        Raises
        ------
        ValueError
            If the index lies outside the layout.
        """
        match index:
            case RowColumnIndex():
                _ = self.layout.from_row_column_to_number(
                    row_index=index.row_index,
                    column_index=index.column_index,
                )
                row_index, column_index = index.tuple
            case int():
                row_index, column_index = self.layout.from_number_to_row_column_index(number=index)
        return self.ax[row_index][column_index]

    def _create_figure(self) -> Figure:
        """
        Create the figure with the global style in parameters applied.

        Returns
        -------
        Figure
            The empty figure.
        """
        plt.rcParams["font.size"] = self.parameters.font_size
        self.parameters.font_family.apply()
        return plt.figure(
            dpi=self.parameters.dpi,
            figsize=self.parameters.figsize,
        )

    def _create_axes_grid(self) -> SubplotAxesGrid:
        """
        Create one Axes per cell of the layout grid.

        Returns
        -------
        SubplotAxesGrid
            The Axes, indexed as grid[row][column].
        """
        grid_spec = self.fig.add_gridspec(nrows=self.layout.row, ncols=self.layout.column)
        return tuple(
            tuple(self.fig.add_subplot(grid_spec[row_index, column_index]) for column_index in range(self.layout.column))
            for row_index in range(self.layout.row)
        )
