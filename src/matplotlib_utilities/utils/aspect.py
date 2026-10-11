from .keyword_enum import KeywordEnum


class Aspect(KeywordEnum):
    """
    Aspect ratio options for matplotlib imshow.

    Attributes:
    ----------
    EQUAL: Ensures square pixels.
    AUTO: Adjusts to fit data.
    """
    EQUAL = "equal"
    AUTO = "auto"
