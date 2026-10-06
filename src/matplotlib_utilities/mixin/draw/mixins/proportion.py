# pyright: reportUnknownMemberType=false

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from ..parameters import PieParameters
from ....protocols import MakerCanvas
from ....types import NumericArray
from ....utils import SubplotIndex


class ProportionDrawMixin:
    """Part-of-a-whole plots."""

    def pie(
        self: MakerCanvas,
        values: NumericArray,
        index: SubplotIndex,
        labels: Sequence[str] | None = None,
        subparams: PieParameters = PieParameters(),
    ) -> None:
        """
        Draw a pie chart on the subplot.

        Each value becomes one wedge whose angle is its share of the total.

        Parameters
        ----------
        values: NumericArray
            The size of each wedge. Values are normalized by their sum.
        index: SubplotIndex
            The index of the subplot.
        labels: Sequence[str] | None
            One label per wedge, drawn next to it.
        subparams: PieParameters
            The subparameters for the pie chart.

        Raises
        ------
        ValueError
            If values is not one-dimensional, holds a negative or non-finite
            entry, or sums to zero, or if labels, colors or explode do not
            hold one entry per value.
        """
        wedge_sizes = np.asarray(values, dtype=float)
        if wedge_sizes.ndim != 1 or wedge_sizes.size == 0:
            raise ValueError(f"values must be a non-empty 1-D array, given shape {wedge_sizes.shape}")
        if not np.all(np.isfinite(wedge_sizes)):
            raise ValueError("values must be finite")
        if np.any(wedge_sizes < 0):
            raise ValueError("values must be non-negative")
        if wedge_sizes.sum() == 0:
            raise ValueError("values must not sum to zero")
        per_wedge_arguments: dict[str, Sequence[object] | None] = {
            "labels": labels,
            "colors": subparams.colors,
            "explode": subparams.explode,
        }
        for name, entries in per_wedge_arguments.items():
            if entries is not None and len(entries) != wedge_sizes.size:
                raise ValueError(
                    f"{name} must hold one entry per value, "
                    + f"given {len(entries)} for {wedge_sizes.size} values"
                )
        subplot = self.access_subplot(index=index)
        subplot.pie(wedge_sizes, labels=labels, **subparams.to_dict)
