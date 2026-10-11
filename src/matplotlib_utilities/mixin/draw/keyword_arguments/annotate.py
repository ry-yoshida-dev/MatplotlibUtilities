from typing import Literal, TypedDict

from ....utils.color import MplColor


class AnnotateKeywordArguments(TypedDict, total=False):
    """
    Keyword arguments produced by AnnotateParameters.to_dict.

    Each key is a field of AnnotateParameters; fields left as None are omitted.
    """

    alpha: float
    zorder: float
    xycoords: Literal[
        "data",
        "axes fraction",
        "axes points",
        "axes pixels",
        "figure fraction",
        "figure points",
        "figure pixels",
        "subfigure fraction",
        "subfigure points",
        "subfigure pixels",
        "polar",
        "offset points",
        "offset pixels",
        "offset fontsize",
    ]
    textcoords: Literal[
        "data",
        "axes fraction",
        "axes points",
        "axes pixels",
        "figure fraction",
        "figure points",
        "figure pixels",
        "subfigure fraction",
        "subfigure points",
        "subfigure pixels",
        "polar",
        "offset points",
        "offset pixels",
        "offset fontsize",
    ]
    arrowprops: dict[str, object]
    annotation_clip: bool
    color: MplColor
    fontsize: (
        float | Literal["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large", "smaller", "larger"]
    )
    fontweight: Literal["ultralight", "light", "normal", "medium", "semibold", "bold", "heavy", "black"] | int
    ha: Literal["left", "center", "right"]
    va: Literal["top", "center", "center_baseline", "baseline", "bottom"]
    rotation: float
    rotation_mode: Literal["default", "anchor", "xtick", "ytick"]
    visible: bool
