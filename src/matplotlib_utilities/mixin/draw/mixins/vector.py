# pyright: reportUnknownMemberType=false

from __future__ import annotations

import numpy as np

from ..parameters import ArrowParameters, QuiverParameters, StreamplotParameters
from ....protocols import MakerCanvas
from .argument_validator import ArgumentValidator
from ....types import NumericArray
from ....utils import SubplotIndex


class VectorDrawMixin:
    """Arrows and vector fields."""

    def arrow(
        self: MakerCanvas,
        x: float,
        y: float,
        dx: float,
        dy: float,
        index: SubplotIndex,
        subparams: ArrowParameters = ArrowParameters(),
    ) -> None:
        """
        Draw an arrow from (x, y) to (x + dx, y + dy) on the subplot.

        Parameters
        ----------
        x, y
            Base coordinates of the arrow.
        dx, dy
            Arrow vector in data coordinates.
        index
            Subplot index.
        subparams
            Geometry and patch keyword arguments (width, head shape, color, etc.).
        """
        subplot = self.access_subplot(index=index)
        _ = subplot.arrow(x, y, dx, dy, **subparams.to_dict)

    def quiver(
        self: MakerCanvas,
        u: NumericArray,
        v: NumericArray,
        index: SubplotIndex,
        x: NumericArray | None = None,
        y: NumericArray | None = None,
        c: NumericArray | None = None,
        subparams: QuiverParameters = QuiverParameters(),
    ) -> None:
        """
        Plot a 2D vector field on the subplot.

        Parameters
        ----------
        u, v
            Arrow direction components (x and y). Must match the shape of ``x`` and
            ``y`` when those are given; otherwise define the grid size when positions
            are omitted.
        index
            Subplot index.
        x, y
            Arrow base coordinates. Omit both (leave as default ``None`` here) to
            let Matplotlib use an integer mesh from the shape of ``u`` and ``v``.
            Matplotlib accepts 2–5 positional arguments; it does not treat
            ``None`` as "missing" for ``X`` / ``Y`` / ``C``.
        c
            Optional scalar data for colormap coloring (matplotlib ``C``).
            Omit to skip colormap coloring.
        subparams
            Arrow geometry, scaling, styling, and colormap keyword arguments.
        """
        ArgumentValidator.require_both_or_neither(x=x, y=y)
        subplot = self.access_subplot(index=index)
        positions: tuple[NumericArray, ...] = () if x is None or y is None else (x, y)
        color_data: tuple[NumericArray, ...] = () if c is None else (c,)
        _ = subplot.quiver(*positions, u, v, *color_data, **subparams.to_dict)

    def streamplot(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        u: NumericArray,
        v: NumericArray,
        index: SubplotIndex,
        color_values: NumericArray | None = None,
        subparams: StreamplotParameters = StreamplotParameters(),
    ) -> None:
        """
        Draw streamlines of a 2D vector field on the subplot.

        Parameters
        ----------
        x, y: NumericArray
            The evenly spaced grid coordinates, either 1-D or 2-D like u.
        u, v: NumericArray
            The x and y components of the vector field on the grid, indexed
            as u[row, column].
        index: SubplotIndex
            The index of the subplot.
        color_values: NumericArray | None
            One value per grid point that colors the streamlines through the
            colormap, for example the speed.
        subparams: StreamplotParameters
            The subparameters for the streamline plot.

        Raises
        ------
        ValueError
            If u and v are not 2-D arrays of the same shape, if color_values
            does not share that shape, or if color_values is combined with
            a fixed color.
        """
        if np.ndim(u) != 2 or np.shape(u) != np.shape(v):
            raise ValueError(
                f"u and v must be 2-D arrays of the same shape, given {np.shape(u)} and {np.shape(v)}"
            )
        if color_values is not None and np.shape(color_values) != np.shape(u):
            raise ValueError(
                f"color_values must have the shape of u, given {np.shape(color_values)} and {np.shape(u)}"
            )
        if color_values is not None and subparams.color is not None:
            raise ValueError("color_values cannot be combined with a fixed color")
        subplot = self.access_subplot(index=index)
        keyword_arguments = subparams.to_dict
        if color_values is not None:
            keyword_arguments["color"] = color_values
        _ = subplot.streamplot(x, y, u, v, **keyword_arguments)
