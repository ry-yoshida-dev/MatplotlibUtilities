# pyright: reportUnknownMemberType=false

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from PIL.Image import Image as PILImage
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import Colorbar
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider

from ..parameters import ColorbarParameters, ImshowParameters
from ....protocols import MakerCanvas
from ....utils import SubplotIndex


class ImageDrawMixin:
    """Raster images and colorbars."""

    def set_colorbar(
        self: MakerCanvas,
        index: SubplotIndex | None = None,
        image: np.ndarray | None = None,
        subparams: ColorbarParameters = ColorbarParameters(),
    ) -> None:
        """
        Add a colorbar to a subplot without drawing image data on that subplot.

        Parameters
        ----------
        index: SubplotIndex | None = None
            The index of the subplot. If None, the colorbar is anchored from the first subplot
            (same figure; use when a single shared colorbar is intended).
        image: np.ndarray | None = None
            The image data to determine the colorbar scale from.
            If None, vmin and vmax must be specified in subparams.
        subparams: ColorbarParameters
            The subparameters for the colorbar.
        """
        sm: ScalarMappable = subparams.create_scalar_mappable(image)
        ax: Axes = self.ax.flat[0] if index is None else self.access_subplot(index=index)
        divider: AxesDivider = make_axes_locatable(ax)
        cax: Axes = subparams.create_cax(divider=divider)
        cbar: Colorbar = self.fig.colorbar(sm, cax=cax)
        if subparams.label is not None:
            cbar.set_label(subparams.label)

    def imshow(
        self: MakerCanvas,
        image: np.ndarray | PILImage,
        index: SubplotIndex,
        subparams: ImshowParameters = ImshowParameters(),
    ) -> None:
        """
        Show the image on the subplot.

        Parameters
        ----------
        image: np.ndarray | PIL.Image.Image
            Image data in a form Matplotlib accepts: a NumPy array (2-D grayscale
            or 3-D RGB, channel-last) or a PIL Image.
        index: SubplotIndex
            The index of the subplot.
        subparams: ImshowParameters
            The subparameters for the imshow plot.
        """
        subparams.__post_init__()
        subplot = self.access_subplot(index=index)
        subplot.imshow(image, **subparams.to_dict)
