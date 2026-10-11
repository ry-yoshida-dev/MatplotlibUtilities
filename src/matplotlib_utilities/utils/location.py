from .keyword_enum import KeywordEnum


class Location(KeywordEnum):
    """
    Location options for matplotlib elements (e.g., colorbar, legend).
    
    Attributes:
    ----------
    LEFT: Place element on the left side of the axes.
    RIGHT: Place element on the right side of the axes.
    TOP: Place element on the top of the axes.
    BOTTOM: Place element on the bottom of the axes.
    """
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
