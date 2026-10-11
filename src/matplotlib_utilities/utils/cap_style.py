from .keyword_enum import KeywordEnum


class CapStyle(KeywordEnum):
    """
    How the ends of a solid line are drawn.

    Attributes
    ----------
    BUTT
        The line stops square at its end point.
    PROJECTING
        The line extends square past its end point by half its width.
    ROUND
        The line ends in a half circle centered on its end point.
    """

    BUTT = "butt"
    PROJECTING = "projecting"
    ROUND = "round"
