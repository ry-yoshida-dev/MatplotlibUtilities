from .keyword_enum import KeywordEnum


class StackBaseline(KeywordEnum):
    """
    Baseline of a stacked area plot (matplotlib ``baseline``).

    Attributes:
    ----------
    ZERO: Stack upward from zero.
    SYMMETRIC: Stack symmetrically around zero.
    WIGGLE: Minimize the sum of squared slopes (a streamgraph).
    WEIGHTED_WIGGLE: Like WIGGLE, weighted by the size of each layer.
    """
    ZERO = "zero"
    SYMMETRIC = "sym"
    WIGGLE = "wiggle"
    WEIGHTED_WIGGLE = "weighted_wiggle"
