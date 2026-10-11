from .keyword_enum import KeywordEnum


class HistType(KeywordEnum):
    """
    Histogram drawing styles (matplotlib ``histtype``).

    Attributes:
    ----------
    BAR: One bar per bin; several datasets sit side by side.
    BAR_STACKED: One bar per bin; several datasets are stacked.
    STEP: An unfilled outline.
    STEP_FILLED: A filled outline.
    """
    BAR = "bar"
    BAR_STACKED = "barstacked"
    STEP = "step"
    STEP_FILLED = "stepfilled"
