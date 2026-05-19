from enum import Enum


class QuiverAngles(Enum):
    """Angle mode for :meth:`matplotlib.axes.Axes.quiver`."""

    UV = "uv"
    XY = "xy"
