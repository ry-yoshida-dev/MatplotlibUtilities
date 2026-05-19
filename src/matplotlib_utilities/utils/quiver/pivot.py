from enum import Enum


class QuiverPivot(Enum):
    """Pivot anchor for :meth:`matplotlib.axes.Axes.quiver`."""

    TAIL = "tail"
    MID = "mid"
    MIDDLE = "middle"
    TIP = "tip"
