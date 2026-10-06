# pyright: reportUnknownMemberType=false

from __future__ import annotations

from ..parameters import BarhParameters, BarParameters, PlotParameters, ScatterParameters
from ....protocols import MakerCanvas
from ....types import NumericArray
from ....utils import SubplotIndex


class SeriesDrawMixin:
    """x/y (or height) data plots."""

    def plot(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex,
        subparams: PlotParameters = PlotParameters(),
    ) -> None:
        """
        Plot the data on the subplot.

        Parameters
        ----------
        x: NumericArray
            The x values of the data.
        y: NumericArray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: PlotParameters
            The subparameters for the plot.
        """
        subplot = self.access_subplot(index=index)
        subplot.plot(x, y, **subparams.to_dict)

    def scatter(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex,
        subparams: ScatterParameters = ScatterParameters(),
    ) -> None:
        """
        Scatter the data on the subplot.

        Parameters
        ----------
        x: NumericArray
            The x values of the data.
        y: NumericArray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: ScatterParameters
            The subparameters for the scatter plot.
        """
        subplot = self.access_subplot(index=index)
        subplot.scatter(x=x, y=y, **subparams.to_dict)

    def bar(
        self: MakerCanvas,
        x: NumericArray,
        height: NumericArray,
        index: SubplotIndex,
        subparams: BarParameters = BarParameters(),
    ) -> None:
        """
        Draw a bar plot on the subplot.

        Parameters
        ----------
        x: NumericArray
            The positions of the bars on the category axis.
        height: NumericArray
            The height of each bar, which is the value it encodes.
        index: SubplotIndex
            The index of the subplot.
        subparams: BarParameters
            The subparameters for the bar plot.

        Raises
        ------
        ValueError
            If x and height do not hold the same number of entries.
        """
        if len(x) != len(height):
            raise ValueError(
                f"x and height must hold the same number of entries, given {len(x)} and {len(height)}"
            )
        subplot = self.access_subplot(index=index)
        subplot.bar(x, height, **subparams.to_dict)

    def barh(
        self: MakerCanvas,
        y: NumericArray,
        width: NumericArray,
        index: SubplotIndex,
        subparams: BarhParameters = BarhParameters(),
    ) -> None:
        """
        Draw a horizontal bar plot on the subplot.

        Bars run along the x axis, so the categories sit on the y axis and
        their labels read horizontally. That suits a category whose name is
        too long to fit under a vertical bar.

        Parameters
        ----------
        y: NumericArray
            The positions of the bars on the category axis.
        width: NumericArray
            The length of each bar, which is the value it encodes.
        index: SubplotIndex
            The index of the subplot.
        subparams: BarhParameters
            The subparameters for the horizontal bar plot.

        Raises
        ------
        ValueError
            If y and width do not hold the same number of entries.
        """
        if len(y) != len(width):
            raise ValueError(
                f"y and width must hold the same number of entries, "
                f"given {len(y)} and {len(width)}"
            )
        subplot = self.access_subplot(index=index)
        subplot.barh(y, width, **subparams.to_dict)
