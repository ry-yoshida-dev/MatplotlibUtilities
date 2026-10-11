from ..keyword_enum import KeywordEnum

from matplotlib.colors import Colormap
from matplotlib import colormaps

class ColorMap(KeywordEnum):
    # --- Perceptually Uniform Sequential ---
    VIRIDIS = 'viridis'
    PLASMA = 'plasma'
    INFERNO = 'inferno'
    MAGMA = 'magma'
    CIVIDIS = 'cividis'

    # --- Sequential ---
    GREYS = 'Greys'
    PURPLES = 'Purples'
    BLUES = 'Blues'
    GREENS = 'Greens'
    ORANGES = 'Oranges'
    REDS = 'Reds'
    YL_OR_BR = 'YlOrBr'
    YL_OR_RD = 'YlOrRd'
    OR_RD = 'OrRd'
    PU_RD = 'PuRd'
    RD_PU = 'RdPu'
    BU_PU = 'BuPu'
    GN_BU = 'GnBu'
    PU_BU = 'PuBu'
    YL_GN_BU = 'YlGnBu'
    PU_BU_GN = 'PuBuGn'
    BU_GN = 'BuGn'
    YL_GN = 'YlGn'

    # --- Sequential (2) ---
    BINARY = 'binary'
    GIST_YARG = 'gist_yarg'
    GIST_GRAY = 'gist_gray'
    GRAY = 'gray'
    BONE = 'bone'
    PINK = 'pink'
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'
    WINTER = 'winter'
    COOL = 'cool'
    WISTIA = 'Wistia'
    HOT = 'hot'
    AFMHOT = 'afmhot'
    GIST_HEAT = 'gist_heat'
    COPPER = 'copper'

    # --- Diverging ---
    PI_YG = 'PiYG'
    PR_GN = 'PRGn'
    BR_BG = 'BrBG'
    PU_OR = 'PuOr'
    RD_GY = 'RdGy'
    RD_BU = 'RdBu'
    RD_YL_BU = 'RdYlBu'
    RD_YL_GN = 'RdYlGn'
    SPECTRAL = 'Spectral'
    COOLWARM = 'coolwarm'
    BWR = 'bwr'
    SEISMIC = 'seismic'

    # --- Cyclic ---
    TWILIGHT = 'twilight'
    TWILIGHT_SHIFTED = 'twilight_shifted'
    HSV = 'hsv'

    # --- Qualitative ---
    PASTEL1 = 'Pastel1'
    PASTEL2 = 'Pastel2'
    PAIRED = 'Paired'
    ACCENT = 'Accent'
    DARK2 = 'Dark2'
    SET1 = 'Set1'
    SET2 = 'Set2'
    SET3 = 'Set3'
    TAB10 = 'tab10'
    TAB20 = 'tab20'
    TAB20B = 'tab20b'
    TAB20C = 'tab20c'

    # --- Miscellaneous ---
    TURBO = 'turbo'
    FLAG = 'flag'
    PRISM = 'prism'
    OCEAN = 'ocean'
    GIST_EARTH = 'gist_earth'
    TERRAIN = 'terrain'
    GIST_STERN = 'gist_stern'
    GNUPLOT = 'gnuplot'
    GNUPLOT2 = 'gnuplot2'
    CMRMAP = 'CMRmap'
    CUBEHELIX = 'cubehelix'
    BRG = 'brg'
    GIST_RAINBOW = 'gist_rainbow'
    RAINBOW = 'rainbow'
    JET = 'jet'
    NIPY_SPECTRAL = 'nipy_spectral'
    GIST_NCAR = 'gist_ncar'

    def is_reversed(self) -> bool:
        """
        Check if the colormap is reversed.

        Returns
        -------
        bool
            True if the colormap is reversed, False otherwise.
        """
        return self.value.endswith('_r')

    @property
    def colormap_object(self) -> Colormap:
        """
        Get the colormap object.

        Returns
        -------
        Colormap
            The colormap object.
        """
        # Using the modern 'colormaps' registry instead of the deprecated 'get_cmap'
        return colormaps[self.value]

    @property
    def reversed_object(self) -> Colormap:
        """
        Get the reversed version of the colormap object.

        Returns
        -------
        Colormap
            The reversed colormap object.
        """
        return self.colormap_object.reversed()