from typing import Literal, TypedDict


class GridKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by GridParameters.to_dict.

    Each key is a field of GridParameters; fields left as None are omitted.
    """

    visible: bool
    which: Literal["major", "minor", "both"]
    axis: Literal["both", "x", "y"]
    alpha: float
