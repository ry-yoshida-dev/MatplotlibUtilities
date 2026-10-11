from enum import Enum


class Linestyle(Enum):
    """
    Linestyle is the linestyle for the line plot.

    Named styles are strings; the others are Matplotlib dash patterns of the
    form (offset, (on, off, ...)) in points.
    Ref: https://matplotlib.org/stable/api/lines_api.html
    """

    _value_: str | tuple[int, tuple[int, ...]]

    SOLID = "solid"
    DOTTED = "dotted"
    DASHED = "dashed"
    DASHDOT = "dashdot"
    LOOSELY_DOTTED = (0, (1, 10))
    DENSELY_DOTTED = (0, (1, 1))
    LOOSELY_DASHED = (0, (5, 10))
    DENSELY_DASHED = (0, (5, 1))
    LOOSELY_DASHDOT = (0, (3, 10, 1, 10))
    DENSELY_DASHDOT = (0, (3, 1, 1, 1))
    DASHDOTDOT = (0, (3, 5, 1, 5, 1, 5))
    LOOSELY_DASHDOTDOT = (0, (3, 10, 1, 10, 1, 10))
    DENSELY_DASHDOTDOT = (0, (3, 1, 1, 1, 1, 1))
