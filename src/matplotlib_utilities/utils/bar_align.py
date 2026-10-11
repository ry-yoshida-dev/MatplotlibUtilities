from .keyword_enum import KeywordEnum


class BarAlign(KeywordEnum):
    """
    Where a bar sits relative to its position on the category axis.

    Attributes
    ----------
    CENTER
        The bar is centered on its position.
    EDGE
        The bar starts at its position; a negative width or height places
        it on the other side.
    """

    CENTER = "center"
    EDGE = "edge"
