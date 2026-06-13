# pyright: reportUnknownMemberType=false

from __future__ import annotations

from ..parameters import ArrowParameters, QuiverParameters
from ....protocols import MakerCanvas
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
        subplot.arrow(x, y, dx, dy, **subparams.to_dict)

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
        if (x is None) ^ (y is None):
            raise ValueError("x and y must both be provided or both omitted")
        subplot = self.access_subplot(index=index)
        kwargs = subparams.to_dict
        # Matplotlib optional X, Y, C means fewer positional args (2–5), not None.
        xy: tuple[NumericArray, ...]
        if x is not None:
            assert y is not None
            xy = (x, y)
        else:
            xy = ()
        color_data: tuple[NumericArray, ...] = () if c is None else (c,)
        subplot.quiver(*xy, u, v, *color_data, **kwargs)
