from enum import Enum


class QuiverUnits(Enum):
    """Physical units for quiver arrow length and width scaling."""

    WIDTH = "width"
    HEIGHT = "height"
    DOTS = "dots"
    INCHES = "inches"
    X = "x"
    Y = "y"
    XY = "xy"
