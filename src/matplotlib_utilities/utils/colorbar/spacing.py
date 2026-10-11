from ..keyword_enum import KeywordEnum


class ColorbarSpacing(KeywordEnum):
    """
    Spacing options for matplotlib colorbar.

    Attributes:
    ----------
    UNIFORM: Each color gets the same space.
    PROPORTIONAL: Space is proportional to the data interval.
    """
    UNIFORM = "uniform"
    PROPORTIONAL = "proportional"
