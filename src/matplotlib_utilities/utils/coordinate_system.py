from .keyword_enum import KeywordEnum


class CoordinateSystem(KeywordEnum):
    """
    Coordinate system that an annotation point or its text is given in.

    Attributes
    ----------
    DATA
        The data coordinates of the subplot.
    AXES_FRACTION
        Fractions of the subplot, (0, 0) at the lower left.
    AXES_POINTS
        Points from the lower left of the subplot.
    AXES_PIXELS
        Pixels from the lower left of the subplot.
    FIGURE_FRACTION
        Fractions of the figure, (0, 0) at the lower left.
    FIGURE_POINTS
        Points from the lower left of the figure.
    FIGURE_PIXELS
        Pixels from the lower left of the figure.
    SUBFIGURE_FRACTION
        Fractions of the subfigure, (0, 0) at the lower left.
    SUBFIGURE_POINTS
        Points from the lower left of the subfigure.
    SUBFIGURE_PIXELS
        Pixels from the lower left of the subfigure.
    POLAR
        (theta, r) in data coordinates.
    OFFSET_POINTS
        Points away from the annotated point. Valid only for the text.
    OFFSET_PIXELS
        Pixels away from the annotated point. Valid only for the text.
    OFFSET_FONTSIZE
        Multiples of the font size away from the annotated point. Valid
        only for the text.
    """

    DATA = "data"
    AXES_FRACTION = "axes fraction"
    AXES_POINTS = "axes points"
    AXES_PIXELS = "axes pixels"
    FIGURE_FRACTION = "figure fraction"
    FIGURE_POINTS = "figure points"
    FIGURE_PIXELS = "figure pixels"
    SUBFIGURE_FRACTION = "subfigure fraction"
    SUBFIGURE_POINTS = "subfigure points"
    SUBFIGURE_PIXELS = "subfigure pixels"
    POLAR = "polar"
    OFFSET_POINTS = "offset points"
    OFFSET_PIXELS = "offset pixels"
    OFFSET_FONTSIZE = "offset fontsize"

    @property
    def is_offset(self) -> bool:
        """
        Whether the system measures from the annotated point.

        Returns
        -------
        bool
            True for the offset systems, which only the text accepts.
        """
        match self:
            case CoordinateSystem.OFFSET_POINTS | CoordinateSystem.OFFSET_PIXELS | CoordinateSystem.OFFSET_FONTSIZE:
                return True
            case _:
                return False
