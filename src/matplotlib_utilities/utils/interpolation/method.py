from ..keyword_enum import KeywordEnum


class InterpolationMethod(KeywordEnum):
    """
    Interpolation methods for matplotlib imshow.

    These methods control how the image is resampled when displayed.
    """
    NONE = "none"
    NEAREST = "nearest"
    BILINEAR = "bilinear"
    BICUBIC = "bicubic"
    SPLINE16 = "spline16"
    SPLINE36 = "spline36"
    HANNING = "hanning"
    HAMMING = "hamming"
    HERMITE = "hermite"
    KAISER = "kaiser"
    QUADRIC = "quadric"
    CATROM = "catrom"
    GAUSSIAN = "gaussian"
    BESSEL = "bessel"
    MITCHELL = "mitchell"
    SINC = "sinc"
    LANCZOS = "lanczos"
    BLACKMAN = "blackman"
