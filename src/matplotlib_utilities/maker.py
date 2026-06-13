# pyright: reportUnknownMemberType=false

import gc
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from .types import SubplotAxesArray

from .utils import (
    SubplotIndex,
    RowColumnIndex,
    )
from .layout import GraphLayout
from .parameter import GraphParameters
from .mixin.axis import AxisMixin
from .mixin.draw import DrawMixin


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
    ax: SubplotAxesArray
        The axes of the matplotlib graphs.
    axis: AxisMixin
        Axis API (labels, limits, tick visibility; e.g. maker.axis.set_label(...)).
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
        self.fig, self.ax = self._create_canvas()

    def finalize(
        self,
        save_path: str | None = None,
        is_showing_result_enabled: bool = True
        ) -> None:
        """
        Finalize the matplotlib graphs.
        -> Saving the figure and showing the result.

        Parameters
        ----------
        save_path: str | None = None
            The path to save the figure.
        is_showing_result_enabled: bool = True
            Whether to show the result.
        """
        self.fig.subplots_adjust(
            wspace=self.parameters.w_space,
            hspace=self.parameters.h_space,
        )
        if save_path is not None:
            self.fig.savefig(save_path, bbox_inches="tight")

        if is_showing_result_enabled:
            self.fig.show()
        else:
            plt.close(self.fig)
            gc.collect()

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
            The index of the subplot.
        """
        row_index, column_index = index.tuple
        return self.ax[row_index, column_index]

    def _create_canvas(self) -> tuple[Figure, SubplotAxesArray]:
        """
        Create a canvas for the matplotlib graphs.

        Returns
        -------
        tuple[Figure, SubplotAxesArray]:
            A tuple of the figure and the axes.
        """
        row = self.layout.row
        column = self.layout.column
        plt.rcParams["font.size"] = self.parameters.font_size
        fig = plt.figure(
            dpi=self.parameters.dpi,
            figsize=self.parameters.figsize,
        )
        ax = fig.subplots(nrows=row, ncols=column, squeeze=False)
        return fig, ax
