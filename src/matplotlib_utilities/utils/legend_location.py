from .keyword_enum import KeywordEnum


class LegendLocation(KeywordEnum):
    """
    Where a legend is placed inside its subplot.

    Attributes
    ----------
    BEST
        The position that overlaps the plotted data the least.
    UPPER_RIGHT, UPPER_LEFT, LOWER_LEFT, LOWER_RIGHT
        A corner of the subplot.
    RIGHT, CENTER_LEFT, CENTER_RIGHT, LOWER_CENTER, UPPER_CENTER
        The middle of an edge of the subplot; RIGHT is the same as
        CENTER_RIGHT.
    CENTER
        The center of the subplot.
    """

    BEST = "best"
    UPPER_RIGHT = "upper right"
    UPPER_LEFT = "upper left"
    LOWER_LEFT = "lower left"
    LOWER_RIGHT = "lower right"
    RIGHT = "right"
    CENTER_LEFT = "center left"
    CENTER_RIGHT = "center right"
    LOWER_CENTER = "lower center"
    UPPER_CENTER = "upper center"
    CENTER = "center"
