from .keyword_enum import KeywordEnum


class StepWhere(KeywordEnum):
    """
    Where each step of a step plot changes level (matplotlib ``where`` / ``step``).

    Attributes:
    ----------
    PRE: The level changes at the left of each x position.
    POST: The level changes at the right of each x position.
    MID: The level changes halfway between neighboring x positions.
    """
    PRE = "pre"
    POST = "post"
    MID = "mid"
