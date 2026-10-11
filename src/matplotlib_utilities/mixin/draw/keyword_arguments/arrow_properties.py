from typing import Literal, TypedDict

from matplotlib.typing import LineStyleType

from ....utils.color import MplColor


class ArrowPropertiesKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by ArrowProperties.to_dict.

    Each key is a field of ArrowProperties; fields left as None are omitted.
    """

    arrowstyle: Literal[
        "-", "->", "<-", "<->", "-|>", "<|-", "<|-|>", "-[", "]-", "]-[", "|-|", "simple", "fancy", "wedge"
    ]
    color: MplColor
    linewidth: float
    linestyle: LineStyleType
    shrinkA: float
    shrinkB: float
    alpha: float
