from dataclasses import dataclass

from matplotlib.colors import Normalize

from .cmap import CmapParameters


@dataclass(frozen=True)
class NormParameters(CmapParameters):
    """
    Colormap scaling that also accepts an explicit normalization.

    Attributes:
    ----------
    norm: Normalize | None
        The normalization applied before colormap mapping, for example a
        LogNorm. It replaces vmin and vmax, so they must stay unset.
    """

    norm: Normalize | None = None

    def __post_init__(self) -> None:
        if self.norm is not None and (self.vmin is not None or self.vmax is not None):
            raise ValueError("norm cannot be combined with vmin or vmax; set the limits on norm instead")
        super().__post_init__()
