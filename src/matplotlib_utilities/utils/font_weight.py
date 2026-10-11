from .keyword_enum import KeywordEnum


class FontWeight(KeywordEnum):
    """
    Named font weight, from lightest to heaviest.

    Attributes
    ----------
    ULTRALIGHT, LIGHT, NORMAL, MEDIUM, SEMIBOLD, BOLD, HEAVY, BLACK
        Weight steps; NORMAL is the regular text weight.
    """

    ULTRALIGHT = "ultralight"
    LIGHT = "light"
    NORMAL = "normal"
    MEDIUM = "medium"
    SEMIBOLD = "semibold"
    BOLD = "bold"
    HEAVY = "heavy"
    BLACK = "black"
