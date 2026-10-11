from .keyword_enum import KeywordEnum


class JoinStyle(KeywordEnum):
    """
    How the corners between segments of a solid line are drawn.

    Attributes
    ----------
    MITER
        The outer edges meet at a sharp point.
    ROUND
        The corner is rounded off with a circular arc.
    BEVEL
        The corner is cut off with a straight edge.
    """

    MITER = "miter"
    ROUND = "round"
    BEVEL = "bevel"
