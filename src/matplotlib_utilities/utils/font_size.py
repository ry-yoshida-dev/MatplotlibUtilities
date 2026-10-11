from .keyword_enum import KeywordEnum


class FontSize(KeywordEnum):
    """
    Named font size, relative to the default font size.

    Attributes
    ----------
    XX_SMALL, X_SMALL, SMALL, MEDIUM, LARGE, X_LARGE, XX_LARGE
        Absolute size steps, MEDIUM being the default font size.
    SMALLER, LARGER
        One step smaller or larger than the default font size.
    """

    XX_SMALL = "xx-small"
    X_SMALL = "x-small"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    X_LARGE = "x-large"
    XX_LARGE = "xx-large"
    SMALLER = "smaller"
    LARGER = "larger"
