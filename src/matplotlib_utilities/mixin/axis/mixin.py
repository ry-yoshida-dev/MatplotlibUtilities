# pyright: reportUnknownMemberType=false

from __future__ import annotations

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
