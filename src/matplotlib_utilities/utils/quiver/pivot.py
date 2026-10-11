from ..keyword_enum import KeywordEnum


class QuiverPivot(KeywordEnum):
    """Pivot anchor for :meth:`matplotlib.axes.Axes.quiver`."""

    TAIL = "tail"
    MID = "mid"
    MIDDLE = "middle"
    TIP = "tip"
