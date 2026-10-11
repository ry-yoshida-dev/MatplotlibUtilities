from __future__ import annotations

from enum import Enum


class FontFamily(Enum):
    """
    Font family used for every text drawn on a figure.

    Matplotlib ships no font holding Japanese glyphs, so a label written in
    Japanese is drawn as tofu boxes unless a font that holds them is
    registered first. Selecting JAPANESE registers a bundled one.

    Attributes:
    ----------
    DEFAULT: str
        Leaves the font family in the rcParams untouched.
    JAPANESE: str
        A bundled font holding Japanese glyphs.
    """

    DEFAULT = "default"
    JAPANESE = "japanese"

    def apply(self) -> None:
        """
        Register this font family with Matplotlib.

        The family is set on the global rcParams. MatplotGraphMaker
        restores the previous family when it is finalized. DEFAULT does
        nothing.
        """
        match self:
            case FontFamily.DEFAULT:
                return
            case FontFamily.JAPANESE:
                import matplotlib_fontja

                matplotlib_fontja.japanize()
