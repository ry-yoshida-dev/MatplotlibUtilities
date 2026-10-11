# pyright: reportUnknownMemberType=false

from __future__ import annotations

import numpy as np
from PIL.Image import Image as PILImage
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.collections import QuadMesh
from matplotlib.colorbar import Colorbar
from matplotlib.contour import QuadContourSet
from matplotlib.image import AxesImage
from matplotlib.image import pil_to_array
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider

from ..parameters import (
    ColorbarParameters,
    ContourfParameters,
    ContourParameters,
    ImscatterParameters,
    ImshowParameters,
    PcolormeshParameters,
)
from ....protocols import MakerCanvas
from .argument_validator import ArgumentValidator
from ....types import NumericArray
from ....utils import SubplotIndex


class ImageDrawMixin:
    """Raster images, gridded values and colorbars."""

    def set_colorbar(
        self: MakerCanvas,
        index: SubplotIndex = 0,
        image: NumericArray | None = None,
        mappable: ScalarMappable | None = None,
        subparams: ColorbarParameters = ColorbarParameters(),
    ) -> Colorbar:
        """
        Add a colorbar next to a subplot.

        Pass the mappable returned by a draw call (imshow, contourf,
        pcolormesh, hexbin, hist2d, scatter) so the colorbar shares its
        colormap, normalization and levels. Pass image instead to build a
        standalone scale from the data range and the cmap, vmin and vmax of
        subparams.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot the colorbar is anchored to.
        image: NumericArray | None = None
            The image data to determine the colorbar scale from.
            If None and mappable is None, vmin and vmax must be specified in subparams.
        mappable: ScalarMappable | None = None
            The artist the colorbar describes.
        subparams: ColorbarParameters
            The subparameters for the colorbar.

        Returns
        -------
        Colorbar
            The colorbar that was added.

        Raises
        ------
        ValueError
            If both image and mappable are given, or if mappable is given
            together with cmap, vmin or vmax in subparams.
        """
        match mappable:
            case ScalarMappable() if image is not None:
                raise ValueError("image and mappable cannot both be given")
            case ScalarMappable() if subparams.is_scale_set:
                raise ValueError("cmap, vmin and vmax cannot be set when a mappable is given; set them on the draw call")
            case ScalarMappable():
                scalar_mappable = mappable
            case None:
                scalar_mappable = subparams.create_scalar_mappable(image)
        ax: Axes = self.access_subplot(index=index)
        divider: AxesDivider = make_axes_locatable(ax)
        cax: Axes = subparams.create_cax(divider=divider)
        return self.fig.colorbar(scalar_mappable, cax=cax, **subparams.colorbar_keyword_arguments)

    def imshow(
        self: MakerCanvas,
        image: NumericArray | PILImage,
        index: SubplotIndex = 0,
        subparams: ImshowParameters = ImshowParameters(),
    ) -> AxesImage:
        """
        Show the image on the subplot.

        Parameters
        ----------
        image: NumericArray | PIL.Image.Image
            Image data in a form Matplotlib accepts: a NumPy array (2-D grayscale
            or 3-D RGB, channel-last) or a PIL Image.
        index: SubplotIndex
            The index of the subplot.
        subparams: ImshowParameters
            The subparameters for the imshow plot.

        Returns
        -------
        AxesImage
            The drawn image, which set_colorbar accepts as mappable.
        """
        subplot = self.access_subplot(index=index)
        return subplot.imshow(image, **subparams.to_dict)

    def imscatter(
        self: MakerCanvas,
        x: NumericArray,
        y: NumericArray,
        images: list[NumericArray | PILImage],
        index: SubplotIndex = 0,
        subparams: ImscatterParameters = ImscatterParameters(),
    ) -> None:
        """
        Place an image at each point on the subplot instead of a marker.

        Parameters
        ----------
        x: NumericArray
            The x values of the points.
        y: NumericArray
            The y values of the points.
        images: list[NumericArray | PIL.Image.Image]
            One image per point, or a single image repeated at every point.
        index: SubplotIndex
            The index of the subplot.
        subparams: ImscatterParameters
            The subparameters for the image scatter plot.

        Raises
        ------
        ValueError
            If x and y do not hold the same number of entries, or if images
            holds neither one image nor one image per point.
        """
        ArgumentValidator.require_equal_length("x", x, "y", y)
        if len(images) not in (1, len(x)):
            raise ValueError(
                f"images must hold one image or one image per point, given {len(images)} for {len(x)} points"
            )
        images_per_point = images * len(x) if len(images) == 1 else images
        subplot = self.access_subplot(index=index)
        colormap = None if subparams.cmap is None else subparams.cmap.colormap_object
        for x_value, y_value, image in zip(map(float, x), map(float, y), images_per_point):
            pixels = pil_to_array(image) if isinstance(image, PILImage) else image
            offset_image = OffsetImage(pixels, zoom=subparams.zoom, cmap=colormap)
            image_box = AnnotationBbox(offset_image, (x_value, y_value), frameon=subparams.is_framed)
            if subparams.zorder is not None:
                image_box.set_zorder(subparams.zorder)
            _ = subplot.add_artist(image_box)
        subplot.update_datalim(np.column_stack([x, y]))
        subplot.autoscale_view()

    def contour(
        self: MakerCanvas,
        z: NumericArray,
        index: SubplotIndex = 0,
        x: NumericArray | None = None,
        y: NumericArray | None = None,
        is_labeled: bool = False,
        subparams: ContourParameters = ContourParameters(),
    ) -> QuadContourSet:
        """
        Draw contour lines of gridded values on the subplot.

        Parameters
        ----------
        z: NumericArray
            The values on a 2-D grid, indexed as z[row, column].
        index: SubplotIndex
            The index of the subplot.
        x, y: NumericArray | None
            The coordinates of the grid columns and rows, either 1-D or 2-D
            like z. Omit both to use the column and row numbers.
        is_labeled: bool
            Whether each contour line is labeled with its level.
        subparams: ContourParameters
            The subparameters for the contour line plot.

        Returns
        -------
        QuadContourSet
            The drawn contour lines, which set_colorbar accepts as mappable.

        Raises
        ------
        ValueError
            If z is not two-dimensional, or if only one of x and y is given.
        """
        subplot = self.access_subplot(index=index)
        contour_set = subplot.contour(*_grid_arguments(z=z, x=x, y=y), **subparams.to_dict)
        if is_labeled:
            _ = subplot.clabel(contour_set)
        return contour_set

    def contourf(
        self: MakerCanvas,
        z: NumericArray,
        index: SubplotIndex = 0,
        x: NumericArray | None = None,
        y: NumericArray | None = None,
        subparams: ContourfParameters = ContourfParameters(),
    ) -> QuadContourSet:
        """
        Draw filled contour bands of gridded values on the subplot.

        Pass the returned contour set to set_colorbar(mappable=...) to show the value scale.

        Parameters
        ----------
        z: NumericArray
            The values on a 2-D grid, indexed as z[row, column].
        index: SubplotIndex
            The index of the subplot.
        x, y: NumericArray | None
            The coordinates of the grid columns and rows, either 1-D or 2-D
            like z. Omit both to use the column and row numbers.
        subparams: ContourfParameters
            The subparameters for the filled contour plot.

        Returns
        -------
        QuadContourSet
            The drawn contour bands, which set_colorbar accepts as mappable.

        Raises
        ------
        ValueError
            If z is not two-dimensional, or if only one of x and y is given.
        """
        subplot = self.access_subplot(index=index)
        return subplot.contourf(*_grid_arguments(z=z, x=x, y=y), **subparams.to_dict)

    def pcolormesh(
        self: MakerCanvas,
        z: NumericArray,
        index: SubplotIndex = 0,
        x: NumericArray | None = None,
        y: NumericArray | None = None,
        subparams: PcolormeshParameters = PcolormeshParameters(),
    ) -> QuadMesh:
        """
        Color each cell of a grid by its value on the subplot.

        Unlike imshow, the cells may be unevenly spaced.

        Parameters
        ----------
        z: NumericArray
            The values on a 2-D grid, indexed as z[row, column].
        index: SubplotIndex
            The index of the subplot.
        x, y: NumericArray | None
            The coordinates of the cell edges or centers (see Shading).
            Omit both to use the column and row numbers.
        subparams: PcolormeshParameters
            The subparameters for the pseudocolor mesh.

        Returns
        -------
        QuadMesh
            The drawn mesh, which set_colorbar accepts as mappable.

        Raises
        ------
        ValueError
            If z is not two-dimensional, or if only one of x and y is given.
        """
        subplot = self.access_subplot(index=index)
        return subplot.pcolormesh(*_grid_arguments(z=z, x=x, y=y), **subparams.to_dict)


def _grid_arguments(
    z: NumericArray,
    x: NumericArray | None,
    y: NumericArray | None,
) -> tuple[NumericArray, ...]:
    if np.ndim(z) != 2:
        raise ValueError(f"z must be a 2-D array, given shape {np.shape(z)}")
    ArgumentValidator.require_both_or_neither(x=x, y=y)
    if x is None or y is None:
        return (z,)
    return (x, y, z)
