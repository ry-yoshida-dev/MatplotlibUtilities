from .keyword_enum import KeywordEnum


class DrawStyle(KeywordEnum):
    """
    How the points of a line plot are connected.

    Attributes
    ----------
    DEFAULT
        Straight segments between neighboring points.
    STEPS
        Steps that change level at each point, the same as STEPS_PRE.
    STEPS_PRE
        Steps that change level at the start of each interval.
    STEPS_MID
        Steps that change level halfway between neighboring points.
    STEPS_POST
        Steps that change level at the end of each interval.
    """

    DEFAULT = "default"
    STEPS = "steps"
    STEPS_PRE = "steps-pre"
    STEPS_MID = "steps-mid"
    STEPS_POST = "steps-post"
