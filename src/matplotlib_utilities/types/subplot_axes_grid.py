"""Type alias for the grid of Matplotlib Axes held by the graph maker."""

from __future__ import annotations

from matplotlib.axes import Axes

type SubplotAxesGrid = tuple[tuple[Axes, ...], ...]
