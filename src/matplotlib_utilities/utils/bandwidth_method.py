from .keyword_enum import KeywordEnum


class BandwidthMethod(KeywordEnum):
    """
    Rule that picks the kernel density bandwidth of a violin plot.

    Attributes:
    ----------
    SCOTT: Scott's rule of thumb.
    SILVERMAN: Silverman's rule of thumb.
    """
    SCOTT = "scott"
    SILVERMAN = "silverman"
