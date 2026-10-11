from .keyword_enum import KeywordEnum


class RotationMode(KeywordEnum):
    """
    Whether text is aligned before or after it is rotated.

    Attributes
    ----------
    DEFAULT
        Rotate the text first, then align its bounding box.
    ANCHOR
        Align the unrotated text first, then rotate it about that point.
    XTICK
        Align as suits an x tick label, keeping it next to its tick.
    YTICK
        Align as suits a y tick label, keeping it next to its tick.
    """

    DEFAULT = "default"
    ANCHOR = "anchor"
    XTICK = "xtick"
    YTICK = "ytick"
