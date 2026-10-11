from collections.abc import Sequence
from typing import TypedDict

from ....utils.color import MplColor


class PieKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by PieParameters.to_dict.

    Each key is a field of PieParameters; fields left as None are omitted.
    """

    colors: Sequence[MplColor]
    explode: Sequence[float]
    autopct: str
    pctdistance: float
    labeldistance: float
    startangle: float
    counterclock: bool
    radius: float
    wedgeprops: dict[str, object]
