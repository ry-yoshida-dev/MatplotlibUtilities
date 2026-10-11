from enum import Enum


class KeywordEnum(Enum):
    """
    Enum whose string member values are passed to Matplotlib as keyword argument values.

    Declaring the value type lets type checkers see what reaches Matplotlib
    when a parameter dataclass is converted to keyword arguments.
    """

    _value_: str
