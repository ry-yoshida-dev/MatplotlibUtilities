from dataclasses import dataclass

from ....keyword_subparameter import KeywordSubparameters
from ..keyword_arguments import TickParamsKeywordArguments


@dataclass(frozen=True)
class TickParamsParameters(KeywordSubparameters[TickParamsKeywordArguments]):
    """
    Parameters for configuring tick marks and labels on matplotlib axes.

    Attributes:
    ----------
    bottom: bool = False
        Whether to show tick marks on the bottom axis.
    left: bool = False
        Whether to show tick marks on the left axis.
    right: bool = False
        Whether to show tick marks on the right axis.
    top: bool = False
        Whether to show tick marks on the top axis.
    labelbottom: bool = False
        Whether to show tick labels on the bottom axis.
    labelleft: bool = False
        Whether to show tick labels on the left axis.
    labelright: bool = False
        Whether to show tick labels on the right axis.
    labeltop: bool = False
        Whether to show tick labels on the top axis.
    """

    bottom: bool = False
    left: bool = False
    right: bool = False
    top: bool = False
    labelbottom: bool = False
    labelleft: bool = False
    labelright: bool = False
    labeltop: bool = False
