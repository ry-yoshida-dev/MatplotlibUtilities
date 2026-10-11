from .keyword_enum import KeywordEnum


class HorizontalAlignment(KeywordEnum):
    """
    Which side of a text box sits at its x position.

    Attributes
    ----------
    LEFT
        The left edge of the text sits at the position.
    CENTER
        The text is centered on the position.
    RIGHT
        The right edge of the text sits at the position.
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
