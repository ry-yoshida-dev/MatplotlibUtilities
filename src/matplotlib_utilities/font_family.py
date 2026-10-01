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
        Leaves the font family in the rcParams untouched. A family set
        earlier, such as by a previous JAPANESE maker, stays in effect.
    JAPANESE: str
        A bundled font holding Japanese glyphs.
    """

    DEFAULT = "default"
    JAPANESE = "japanese"

    def apply(self) -> None:
        """
        Register this font family with Matplotlib.

        Takes effect for every figure drawn afterwards, since the family is
        set on the global rcParams. DEFAULT does nothing, so it does not
        undo a family applied before.
        """
        match self:
            case FontFamily.DEFAULT:
                return
            case FontFamily.JAPANESE:
                import matplotlib_fontja

                matplotlib_fontja.japanize()
