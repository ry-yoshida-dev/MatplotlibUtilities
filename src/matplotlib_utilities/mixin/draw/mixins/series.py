# pyright: reportUnknownMemberType=false

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from matplotlib.collections import PathCollection
from numpy.typing import NDArray

from ..parameters import (
    BarhParameters,
    BarParameters,
    ErrorbarParameters,
    FillBetweenParameters,
    PlotParameters,
    ScatterParameters,
    StackplotParameters,
    StepParameters,
)
from ....protocols import MakerCanvas
from .argument_validator import ArgumentValidator
from ....types import NumericArray
from ....utils import SubplotIndex


class SeriesDrawMixin:
    """x/y (or height) data plots."""

    def plot(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex = 0,
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
        _ = subplot.plot(x, y, **subparams.to_dict)

    def scatter(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex = 0,
        subparams: ScatterParameters = ScatterParameters(),
    ) -> PathCollection:
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

        Returns
        -------
        PathCollection
            The drawn points, which set_colorbar accepts as mappable when
            they are colored by value.
        """
        subplot = self.access_subplot(index=index)
        return subplot.scatter(x=x, y=y, **subparams.to_dict)

    def bar(
        self: MakerCanvas,
        x: NumericArray,
        height: NumericArray,
        index: SubplotIndex = 0,
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
        ArgumentValidator.require_equal_length("x", x, "height", height)
        subplot = self.access_subplot(index=index)
        _ = subplot.bar(x, height, **subparams.to_dict)

    def barh(
        self: MakerCanvas,
        y: NumericArray,
        width: NumericArray,
        index: SubplotIndex = 0,
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
        ArgumentValidator.require_equal_length("y", y, "width", width)
        subplot = self.access_subplot(index=index)
        _ = subplot.barh(y, width, **subparams.to_dict)

    def step(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex = 0,
        subparams: StepParameters = StepParameters(),
    ) -> None:
        """
        Draw a step plot on the subplot.

        The value holds constant between neighboring x positions, which suits
        data that changes in discrete jumps such as counts or states.

        Parameters
        ----------
        x: NumericArray
            The x values of the data.
        y: NumericArray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: StepParameters
            The subparameters for the step plot.

        Raises
        ------
        ValueError
            If x and y do not hold the same number of entries.
        """
        ArgumentValidator.require_equal_length("x", x, "y", y)
        subplot = self.access_subplot(index=index)
        _ = subplot.step(x, y, **subparams.to_dict)

    def errorbar(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex = 0,
        yerr: NumericArray | float | None = None,
        xerr: NumericArray | float | None = None,
        subparams: ErrorbarParameters = ErrorbarParameters(),
    ) -> None:
        """
        Plot the data with error bars on the subplot.

        Parameters
        ----------
        x: NumericArray
            The x values of the data.
        y: NumericArray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        yerr: NumericArray | float | None
            The vertical error: one value for every point, one value per
            point, or a (2, N) array of lower and upper errors.
        xerr: NumericArray | float | None
            The horizontal error, in the same forms as yerr.
        subparams: ErrorbarParameters
            The subparameters for the error bar plot.

        Raises
        ------
        ValueError
            If x and y do not hold the same number of entries, if neither
            yerr nor xerr is given, or if an error array does not hold one
            entry per point.
        """
        ArgumentValidator.require_equal_length("x", x, "y", y)
        if yerr is None and xerr is None:
            raise ValueError("at least one of yerr and xerr must be given")
        for name, error in (("yerr", yerr), ("xerr", xerr)):
            if error is None:
                continue
            error_values = np.asarray(error, dtype=float)
            if error_values.ndim > 0 and error_values.shape[-1] != len(x):
                raise ValueError(
                    f"{name} must hold one entry per point, given shape {error_values.shape} for {len(x)} points"
                )
            if np.any(error_values < 0):
                raise ValueError(f"{name} must be non-negative")
        subplot = self.access_subplot(index=index)
        _ = subplot.errorbar(x, y, yerr=yerr, xerr=xerr, **subparams.to_dict)

    def fill_between(
        self: MakerCanvas,
        x: NumericArray,
        y1: NumericArray,
        index: SubplotIndex = 0,
        y2: NumericArray | float = 0.0,
        where: NDArray[np.bool_] | None = None,
        subparams: FillBetweenParameters = FillBetweenParameters(),
    ) -> None:
        """
        Fill the area between two curves on the subplot.

        A typical use is a confidence band drawn behind a line.

        Parameters
        ----------
        x: NumericArray
            The x values shared by both curves.
        y1: NumericArray
            The y values of the first curve.
        index: SubplotIndex
            The index of the subplot.
        y2: NumericArray | float
            The y values of the second curve, or a constant baseline.
        where: NDArray[np.bool_] | None
            Fill only where this mask is True.
        subparams: FillBetweenParameters
            The subparameters for the filled area.

        Raises
        ------
        ValueError
            If y1, y2 or where do not hold one entry per x value.
        """
        per_point_arguments: dict[str, NumericArray | NDArray[np.bool_] | float | None] = {
            "y1": y1,
            "y2": y2,
            "where": where,
        }
        for name, values in per_point_arguments.items():
            if values is not None and np.ndim(values) > 0 and len(np.asarray(values)) != len(x):
                raise ValueError(
                    f"{name} must hold one entry per x value, given {len(np.asarray(values))} for {len(x)}"
                )
        subplot = self.access_subplot(index=index)
        _ = subplot.fill_between(x, y1, y2, where=where, **subparams.to_dict)

    def stackplot(
        self: MakerCanvas,
        x: NumericArray,
        ys: Sequence[NumericArray],
        index: SubplotIndex = 0,
        labels: Sequence[str] | None = None,
        subparams: StackplotParameters = StackplotParameters(),
    ) -> None:
        """
        Draw a stacked area plot on the subplot.

        Each series is drawn on top of the previous ones, so the top edge
        shows the running total.

        Parameters
        ----------
        x: NumericArray
            The x values shared by every series.
        ys: Sequence[NumericArray]
            The series to stack, from the bottom layer up.
        index: SubplotIndex
            The index of the subplot.
        labels: Sequence[str] | None
            One legend label per series.
        subparams: StackplotParameters
            The subparameters for the stacked area plot.

        Raises
        ------
        ValueError
            If ys is empty, if a series does not hold one entry per x value,
            or if labels or colors do not hold one entry per series.
        """
        if len(ys) == 0:
            raise ValueError("ys must hold at least one series")
        for series_number, series in enumerate(ys):
            if len(series) != len(x):
                raise ValueError(
                    f"ys[{series_number}] must hold one entry per x value, given {len(series)} for {len(x)}"
                )
        per_series_arguments: dict[str, Sequence[object] | None] = {
            "labels": labels,
            "colors": subparams.colors,
        }
        for name, entries in per_series_arguments.items():
            if entries is not None and len(entries) != len(ys):
                raise ValueError(
                    f"{name} must hold one entry per series, given {len(entries)} for {len(ys)} series"
                )
        subplot = self.access_subplot(index=index)
        _ = subplot.stackplot(x, *ys, labels=() if labels is None else labels, **subparams.to_dict)
