from .keyword_enum import KeywordEnum


class Hatch(KeywordEnum):
    """
    Pattern drawn inside a filled area.

    Attributes
    ----------
    FORWARD_DIAGONAL
        Lines rising to the right.
    BACK_DIAGONAL
        Lines falling to the right.
    VERTICAL
        Vertical lines.
    HORIZONTAL
        Horizontal lines.
    CROSS
        Vertical and horizontal lines.
    DIAGONAL_CROSS
        Lines in both diagonal directions.
    SMALL_CIRCLE
        Small circles.
    LARGE_CIRCLE
        Large circles.
    DOT
        Dots.
    STAR
        Stars.
    """

    FORWARD_DIAGONAL = "/"
    BACK_DIAGONAL = "\\"
    VERTICAL = "|"
    HORIZONTAL = "-"
    CROSS = "+"
    DIAGONAL_CROSS = "x"
    SMALL_CIRCLE = "o"
    LARGE_CIRCLE = "O"
    DOT = "."
    STAR = "*"
