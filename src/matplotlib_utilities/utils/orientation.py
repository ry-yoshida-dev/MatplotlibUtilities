from .keyword_enum import KeywordEnum


class Orientation(KeywordEnum):
    """
    Orientation options for matplotlib elements (e.g., colorbar, legend).
    
    Attributes:
    ----------
    VERTICAL: Vertical orientation.
    HORIZONTAL: Horizontal orientation.
    """
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
