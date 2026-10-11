from ..keyword_enum import KeywordEnum


class ColorbarExtend(KeywordEnum):
    """
    Extend options for matplotlib colorbar.

    Attributes:
    ----------
    NEITHER: No extensions.
    BOTH: Extend on both ends.
    MIN: Extend on minimum end.
    MAX: Extend on maximum end.
    """
    NEITHER = "neither"
    BOTH = "both"
    MIN = "min"
    MAX = "max"
