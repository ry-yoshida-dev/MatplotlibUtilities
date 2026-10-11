from .keyword_enum import KeywordEnum


class ArrowShape(KeywordEnum):
    """
    shape for :meth:`matplotlib.axes.Axes.arrow` (left-half, right-half, or full arrow).
    """

    FULL = "full"
    LEFT = "left"
    RIGHT = "right"
