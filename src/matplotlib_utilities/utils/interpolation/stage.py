from ..keyword_enum import KeywordEnum


class InterpolationStage(KeywordEnum):
    """
    Interpolation stage for matplotlib imshow.

    Controls at which stage interpolation is performed:
    - 'data': Interpolate before colormapping
    - 'rgba': Interpolate after colormapping
    - 'auto': Automatically select the appropriate stage
    """
    AUTO = "auto"
    DATA = "data"
    RGBA = "rgba"
