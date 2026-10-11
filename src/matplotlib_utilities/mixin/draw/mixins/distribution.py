# pyright: reportUnknownMemberType=false

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from matplotlib.collections import PolyCollection, QuadMesh

from ..parameters import (
    BoxplotParameters,
    HexbinParameters,
    Hist2dParameters,
    HistParameters,
    ViolinplotParameters,
)
from ....protocols import MakerCanvas
from .argument_validator import ArgumentValidator
from ....types import NumericArray
from ....utils import SubplotIndex


class DistributionDrawMixin:
    """Plots that summarize how values are distributed."""

    def hist(
        self: MakerCanvas,
        x: NumericArray | Sequence[NumericArray],
        index: SubplotIndex,
        subparams: HistParameters = HistParameters(),
    ) -> None:
        """
        Draw a histogram on the subplot.

        Parameters
        ----------
        x: NumericArray | Sequence[NumericArray]
            One dataset as a 1-D array, several datasets as a 2-D array with
            one dataset per column, or a sequence of 1-D arrays. Several
            datasets are drawn side by side or stacked.
        index: SubplotIndex
            The index of the subplot.
        subparams: HistParameters
            The subparameters for the histogram.

        Raises
        ------
        ValueError
            If x is not 1-D or 2-D, if it holds an empty dataset, or if color
            is a list that does not hold one entry per dataset.
        """
        datasets = _as_datasets(data=x, name="x")
        colors = subparams.color
        if isinstance(colors, list) and len(colors) != len(datasets):
            raise ValueError(
                f"color must hold one entry per dataset, given {len(colors)} for {len(datasets)} datasets"
            )
        subplot = self.access_subplot(index=index)
        _ = subplot.hist(datasets, **subparams.to_dict)

    def boxplot(
        self: MakerCanvas,
        data: NumericArray | Sequence[NumericArray],
        index: SubplotIndex,
        positions: Sequence[float] | None = None,
        tick_labels: Sequence[str] | None = None,
        subparams: BoxplotParameters = BoxplotParameters(),
    ) -> None:
        """
        Draw one box plot per dataset on the subplot.

        Each box spans the interquartile range with a line at the median;
        the whiskers and outliers show the spread beyond it.

        Parameters
        ----------
        data: NumericArray | Sequence[NumericArray]
            The datasets, one per box: a 1-D array for a single box, a 2-D
            array with one dataset per column, or a sequence of 1-D arrays.
        index: SubplotIndex
            The index of the subplot.
        positions: Sequence[float] | None
            The position of each box on the category axis.
        tick_labels: Sequence[str] | None
            One tick label per box.
        subparams: BoxplotParameters
            The subparameters for the box plot.

        Raises
        ------
        ValueError
            If data is not 1-D or 2-D, if it is empty or holds an empty
            dataset, or if positions, tick_labels or widths do not hold one
            entry per dataset.
        """
        datasets = _as_datasets(data=data, name="data")
        _validate_per_dataset_arguments(
            dataset_count=len(datasets),
            positions=positions,
            tick_labels=tick_labels,
            widths=subparams.widths,
        )
        subplot = self.access_subplot(index=index)
        _ = subplot.boxplot(datasets, positions=positions, tick_labels=tick_labels, **subparams.to_dict)

    def violinplot(
        self: MakerCanvas,
        data: NumericArray | Sequence[NumericArray],
        index: SubplotIndex,
        positions: Sequence[float] | None = None,
        subparams: ViolinplotParameters = ViolinplotParameters(),
    ) -> None:
        """
        Draw one violin plot per dataset on the subplot.

        Each violin outlines a kernel density estimate, so it shows the shape
        of the distribution that a box plot hides.

        Parameters
        ----------
        data: NumericArray | Sequence[NumericArray]
            The datasets, one per violin: a 1-D array for a single violin, a
            2-D array with one dataset per column, or a sequence of 1-D arrays.
        index: SubplotIndex
            The index of the subplot.
        positions: Sequence[float] | None
            The position of each violin on the category axis.
        subparams: ViolinplotParameters
            The subparameters for the violin plot.

        Raises
        ------
        ValueError
            If data is not 1-D or 2-D, if it is empty or holds an empty
            dataset, or if positions or widths do not hold one entry per
            dataset.
        """
        datasets = _as_datasets(data=data, name="data")
        _validate_per_dataset_arguments(
            dataset_count=len(datasets),
            positions=positions,
            tick_labels=None,
            widths=subparams.widths,
        )
        subplot = self.access_subplot(index=index)
        _ = subplot.violinplot(datasets, positions=positions, **subparams.to_dict)

    def hexbin(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex,
        c: NumericArray | None = None,
        subparams: HexbinParameters = HexbinParameters(),
    ) -> PolyCollection:
        """
        Bin the points into hexagons and color each hexagon on the subplot.

        Suited to scatter data too dense to read point by point.

        Parameters
        ----------
        x: NumericArray
            The x values of the points.
        y: NumericArray
            The y values of the points.
        index: SubplotIndex
            The index of the subplot.
        c: NumericArray | None
            One value per point. Each hexagon then shows the mean of its
            values instead of its point count.
        subparams: HexbinParameters
            The subparameters for the hexagonal binning plot.

        Returns
        -------
        PolyCollection
            The drawn hexagons, which set_colorbar accepts as mappable.

        Raises
        ------
        ValueError
            If x, y and c do not hold the same number of entries.
        """
        _validate_point_count(x=x, y=y, c=c)
        subplot = self.access_subplot(index=index)
        return subplot.hexbin(x, y, C=c, **subparams.to_dict)

    def hist2d(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        index: SubplotIndex,
        subparams: Hist2dParameters = Hist2dParameters(),
    ) -> QuadMesh:
        """
        Draw a two-dimensional histogram of the points on the subplot.

        Parameters
        ----------
        x: NumericArray
            The x values of the points.
        y: NumericArray
            The y values of the points.
        index: SubplotIndex
            The index of the subplot.
        subparams: Hist2dParameters
            The subparameters for the two-dimensional histogram.

        Returns
        -------
        QuadMesh
            The drawn bins, which set_colorbar accepts as mappable.

        Raises
        ------
        ValueError
            If x and y do not hold the same number of entries.
        """
        _validate_point_count(x=x, y=y, c=None)
        subplot = self.access_subplot(index=index)
        histogram = subplot.hist2d(x, y, **subparams.to_dict)
        return histogram[3]


def _as_datasets(data: NumericArray | Sequence[NumericArray], name: str) -> list[NumericArray]:
    if isinstance(data, np.ndarray):
        match data.ndim:
            case 1:
                datasets = [data]
            case 2:
                datasets = list(data.T)
            case _:
                raise ValueError(f"{name} must be a 1-D or 2-D array, given shape {data.shape}")
    else:
        datasets = [np.asarray(dataset) for dataset in data]
    if len(datasets) == 0:
        raise ValueError(f"{name} must hold at least one dataset")
    if any(len(dataset) == 0 for dataset in datasets):
        raise ValueError(f"{name} must not hold an empty dataset")
    return datasets


def _validate_per_dataset_arguments(
    dataset_count: int,
    positions: Sequence[float] | None,
    tick_labels: Sequence[str] | None,
    widths: float | Sequence[float] | None,
) -> None:
    per_dataset_arguments: dict[str, Sequence[object] | None] = {
        "positions": positions,
        "tick_labels": tick_labels,
        "widths": widths if isinstance(widths, Sequence) else None,
    }
    for name, entries in per_dataset_arguments.items():
        if entries is not None and len(entries) != dataset_count:
            raise ValueError(
                f"{name} must hold one entry per dataset, given {len(entries)} for {dataset_count} datasets"
            )


def _validate_point_count(x: NumericArray, y: NumericArray, c: NumericArray | None) -> None:
    ArgumentValidator.require_equal_length("x", x, "y", y)
    if c is not None and len(c) != len(x):
        raise ValueError(f"c must hold one entry per point, given {len(c)} for {len(x)} points")
