from .keyword_enum import KeywordEnum

class Marker(KeywordEnum):
    """
    Marker is the marker for the scatter plot.
    Ref: https://matplotlib.org/stable/api/markers_api.html
    """
    # Points, lines, and shapes
    POINT = "."
    PIXEL = ","
    CIRCLE = "o"
    SQUARE = "s"
    STAR = "*"
    PENTAGON = "p"
    HEXAGON1 = "h"
    HEXAGON2 = "H"
    DIAMOND = "D"
    THIN_DIAMOND = "d"
    OCTAGON = "8"

    # Triangles
    TRIANGLE_DOWN = "v"
    TRIANGLE_UP = "^"
    TRIANGLE_LEFT = "<"
    TRIANGLE_RIGHT = ">"

    # Tri (tri-pod)
    TRI_DOWN = "1"
    TRI_UP = "2"
    TRI_LEFT = "3"
    TRI_RIGHT = "4"

    # Plus and cross
    PLUS = "+"
    X = "x"
    PLUS_FILLED = "P"
    X_FILLED = "X"

    # Lines
    VLINE = "|"
    HLINE = "_"
