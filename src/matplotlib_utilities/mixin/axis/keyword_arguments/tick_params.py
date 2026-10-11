from typing import TypedDict


class TickParamsKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by TickParamsParameters.to_dict.

    Each key is a field of TickParamsParameters; fields left as None are omitted.
    """

    bottom: bool
    left: bool
    right: bool
    top: bool
    labelbottom: bool
    labelleft: bool
    labelright: bool
    labeltop: bool
