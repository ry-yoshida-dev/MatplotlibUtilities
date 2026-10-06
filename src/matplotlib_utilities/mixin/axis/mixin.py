# pyright: reportUnknownMemberType=false

from __future__ import annotations

from collections.abc import Sequence

from ...protocols import MakerCanvas
from ...graph_axis import GraphAxis
from ...utils import SubplotIndex
from .parameters import GridParameters, TickParamsParameters


class AxisMixin:
    """
    Axis-related operations for :class:`MatplotGraphMaker`.
    """

    def set_label(
        self: MakerCanvas,
        label: str,
        index: SubplotIndex,
        axis: GraphAxis,
    ) -> None:
        """
        Set the label on the subplot.

        Parameters
        ----------
        label: str
            The label to set.
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to set the label on.
        """
        subplot = self.access_subplot(index=index)
        axis_attribute = axis.label_set_attribute
        getattr(subplot, axis_attribute)(label)

    def set_lim(
        self: MakerCanvas,
        lower: float,
        upper: float,
        index: SubplotIndex,
        axis: GraphAxis,
    ) -> None:
        """
        Set the limit on the subplot.

        Parameters
        ----------
        lower: float
            The lower limit.
        upper: float
            The upper limit.
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to set the limit on.
        """
        subplot = self.access_subplot(index=index)
        attribute = axis.limit_set_attribute
        getattr(subplot, attribute)(lower, upper)

    def set_ticks(
        self: MakerCanvas,
        positions: Sequence[float],
        index: SubplotIndex,
        axis: GraphAxis,
        labels: Sequence[str] | None = None,
    ) -> None:
        """
        Set the tick positions on the subplot, and optionally their labels.

        Parameters
        ----------
        positions: Sequence[float]
            The positions to place ticks at.
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to set the ticks on.
        labels: Sequence[str] | None
            The text to draw at each position. None keeps the numeric labels
            Matplotlib derives from the positions. When given, it must hold
            one label per position.

        Raises
        ------
        ValueError
            If labels is given and does not match positions in length.
        """
        if labels is not None and len(labels) != len(positions):
            raise ValueError(
                f"labels must hold one entry per position, "
                f"given {len(labels)} for {len(positions)} positions"
            )
        subplot = self.access_subplot(index=index)
        attribute = axis.ticks_set_attribute
        if labels is None:
            getattr(subplot, attribute)(list(positions))
            return
        getattr(subplot, attribute)(list(positions), list(labels))

    def invert(
        self: MakerCanvas,
        index: SubplotIndex,
        axis: GraphAxis,
    ) -> None:
        """
        Invert the direction of an axis on the subplot.

        Inverting the y axis puts the first entry at the top, which is the
        reading order of a horizontal bar chart.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to invert.
        """
        subplot = self.access_subplot(index=index)
        getattr(subplot, axis.invert_attribute)()

    def set_title(
        self: MakerCanvas,
        title: str,
        index: SubplotIndex,
    ) -> None:
        """
        Set the title on the subplot.

        Parameters
        ----------
        title: str
            The title text.
        index: SubplotIndex
            The index of the subplot.
        """
        subplot = self.access_subplot(index=index)
        subplot.set_title(title)

    def set_grid(
        self: MakerCanvas,
        index: SubplotIndex,
        subparams: GridParameters = GridParameters(),
    ) -> None:
        """
        Configure the grid on the subplot.

        Wraps :meth:`matplotlib.axes.Axes.grid`.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        subparams: GridParameters
            Grid settings.
        """
        subplot = self.access_subplot(index=index)
        subplot.grid(**subparams.to_dict)

    def set_grid_below(
        self: MakerCanvas,
        index: SubplotIndex,
        is_below: bool = True,
    ) -> None:
        """
        Place the grid lines and ticks below or above the drawn data.

        Matplotlib draws the grid above patches such as bars by default, so
        the lines cross them; placing it below keeps the bars whole.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        is_below: bool
            Whether the grid goes below every artist drawn on the subplot.
        """
        subplot = self.access_subplot(index=index)
        subplot.set_axisbelow(is_below)

    def delete_axis_label(
        self: MakerCanvas,
        index: SubplotIndex,
        subparams: TickParamsParameters = TickParamsParameters(),
    ) -> None:
        """
        Delete the axis label on the subplot.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        subparams: TickParamsParameters
            Tick visibility for labels.
        """
        subplot = self.access_subplot(index=index)
        subplot.tick_params(**subparams.to_dict)
