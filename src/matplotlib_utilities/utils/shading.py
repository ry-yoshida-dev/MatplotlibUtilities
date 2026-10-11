from .keyword_enum import KeywordEnum


class Shading(KeywordEnum):
    """
    Fill style of a pseudocolor mesh (matplotlib ``shading``).

    Attributes:
    ----------
    FLAT: One solid color per cell; coordinates mark the cell corners.
    NEAREST: One solid color per cell; coordinates mark the cell centers.
    GOURAUD: Colors are interpolated linearly between the vertices.
    AUTO: Choose FLAT or NEAREST from the shapes of the coordinates.
    """
    FLAT = "flat"
    NEAREST = "nearest"
    GOURAUD = "gouraud"
    AUTO = "auto"
