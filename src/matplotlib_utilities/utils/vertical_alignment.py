from .keyword_enum import KeywordEnum


class VerticalAlignment(KeywordEnum):
    """
    Which part of a text box sits at its y position.

    Attributes
    ----------
    TOP
        The top edge of the text sits at the position.
    CENTER
        The text is centered on the position.
    CENTER_BASELINE
        The middle of the first line, measured from its baseline, sits at
        the position.
    BASELINE
        The baseline of the first line sits at the position.
    BOTTOM
        The bottom edge of the text sits at the position.
    """

    TOP = "top"
    CENTER = "center"
    CENTER_BASELINE = "center_baseline"
    BASELINE = "baseline"
    BOTTOM = "bottom"
