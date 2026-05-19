# pyright: reportUnknownMemberType=false

from __future__ import annotations

import numpy as np

from ..parameters import BarParameters, PlotParameters, ScatterParameters
from ....protocols import MakerCanvas
from ....utils import SubplotIndex


class SeriesDrawMixin:
    """x/y (or height) data plots."""

    def plot(
        self: MakerCanvas,
        x: np.ndarray,
        y: np.ndarray,
        index: SubplotIndex,
        subparams: PlotParameters = PlotParameters(),
    ) -> None:
        """
        Plot the data on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the data.
        y: np.ndarray
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
        x: np.ndarray,
        y: np.ndarray,
        index: SubplotIndex,
        subparams: ScatterParameters = ScatterParameters(),
    ) -> None:
        """
        Scatter the data on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the data.
        y: np.ndarray
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
        x: np.ndarray,
        index: SubplotIndex,
        subparams: BarParameters = BarParameters(),
    ) -> None:
        """
        Draw a bar plot on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the bars.
        index: SubplotIndex
            The index of the subplot.
        subparams: BarParameters
            The subparameters for the bar plot.
        """
        subplot = self.access_subplot(index=index)
        subplot.bar(x, **subparams.to_dict)
