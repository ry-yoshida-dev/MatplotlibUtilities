from .keyword_enum import KeywordEnum


class ArrowStyle(KeywordEnum):
    """
    Shape of an arrow drawn between two points.

    Attributes
    ----------
    LINE
        A plain line without heads.
    HEAD_AT_END
        An open head at the end point.
    HEAD_AT_START
        An open head at the start point.
    HEADS_AT_BOTH
        Open heads at both points.
    FILLED_HEAD_AT_END
        A filled head at the end point.
    FILLED_HEAD_AT_START
        A filled head at the start point.
    FILLED_HEADS_AT_BOTH
        Filled heads at both points.
    BRACKET_AT_END
        A square bracket at the end point.
    BRACKET_AT_START
        A square bracket at the start point.
    BRACKETS_AT_BOTH
        Square brackets at both points.
    BAR_AT_BOTH
        Perpendicular bars at both points, as in a dimension line.
    SIMPLE
        A filled arrow whose shaft and head form one shape.
    FANCY
        A filled arrow with a tapered shaft.
    WEDGE
        A filled wedge that narrows toward the end point.
    """

    LINE = "-"
    HEAD_AT_END = "->"
    HEAD_AT_START = "<-"
    HEADS_AT_BOTH = "<->"
    FILLED_HEAD_AT_END = "-|>"
    FILLED_HEAD_AT_START = "<|-"
    FILLED_HEADS_AT_BOTH = "<|-|>"
    BRACKET_AT_END = "-["
    BRACKET_AT_START = "]-"
    BRACKETS_AT_BOTH = "]-["
    BAR_AT_BOTH = "|-|"
    SIMPLE = "simple"
    FANCY = "fancy"
    WEDGE = "wedge"
