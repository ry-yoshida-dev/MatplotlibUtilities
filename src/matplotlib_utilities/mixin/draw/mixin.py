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

from .parameters import (
    AnnotateParameters,
    ArrowParameters,
    ColorbarParameters,
    ImshowParameters,
    LegendParameters,
    LineParameters,
    Orientation,
    PlotParameters,
    ScatterParameters,
    BarParameters,
)
from ...protocols import MakerCanvas
from ...utils import SubplotIndex


class DrawMixin:
    """
    Drawing API on the graph maker (for example maker.scatter(...)).

    Concrete classes are expected to expose fig, ax, and
    access_subplot, which this mixin uses to dispatch drawing calls
    (see matplotlib_utilities.protocols.MakerCanvas).
    """

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

    def plot(
        self: MakerCanvas,
        x: np.ndarray,
        y: np.ndarray,
        index: SubplotIndex,
        subparams: PlotParameters = PlotParameters(),
    ) -> None:
        """
        Plot the data on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the data.
        y: np.ndarray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: PlotParameters
            The subparameters for the plot.
        """
        subplot = self.access_subplot(index=index)
        subplot.plot(x, y, **subparams.to_dict)

    def arrow(
        self: MakerCanvas,
        x: float,
        y: float,
        dx: float,
        dy: float,
        index: SubplotIndex,
        subparams: ArrowParameters = ArrowParameters(),
    ) -> None:
        """
        Draw an arrow from (x, y) to (x + dx, y + dy) on the subplot.

        Parameters
        ----------
        x, y
            Base coordinates of the arrow.
        dx, dy
            Arrow vector in data coordinates.
        index
            Subplot index.
        subparams
            Geometry and patch keyword arguments (width, head shape, color, etc.).
        """
        subplot = self.access_subplot(index=index)
        subplot.arrow(x, y, dx, dy, **subparams.to_dict)

    def scatter(
        self: MakerCanvas,
        x: np.ndarray,
        y: np.ndarray,
        index: SubplotIndex,
        subparams: ScatterParameters = ScatterParameters(),
    ) -> None:
        """
        Scatter the data on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the data.
        y: np.ndarray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: ScatterParameters
            The subparameters for the scatter plot.
        """
        subplot = self.access_subplot(index=index)
        subplot.scatter(x=x, y=y, **subparams.to_dict)

    def legend(
        self: MakerCanvas,
        index: SubplotIndex,
        subparams: LegendParameters = LegendParameters(),
    ) -> None:
        """
        Place a legend on the subplot.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        subparams: LegendParameters
            The subparameters for the legend.
        """
        subplot = self.access_subplot(index=index)
        subplot.legend(**subparams.to_dict)

    def line(
        self: MakerCanvas,
        value: float,
        orientation: Orientation,
        index: SubplotIndex,
        subparams: LineParameters = LineParameters(),
    ) -> None:
        """
        Draw a line on the subplot.

        Parameters
        ----------
        value: float
            The location of the line on the selected axis.
        orientation: Orientation
            The line orientation (vertical or horizontal).
        index: SubplotIndex
            The index of the subplot.
        subparams: LineParameters
            The subparameters for line styling.
        """
        subplot = self.access_subplot(index=index)
        draw = getattr(subplot, orientation.ax_line_attribute)
        match orientation:
            case Orientation.VERTICAL:
                draw(x=value, **subparams.to_dict)
            case Orientation.HORIZONTAL:
                draw(y=value, **subparams.to_dict)

    def annotate(
        self: MakerCanvas,
        text: str,
        xy: tuple[float, float],
        index: SubplotIndex,
        xytext: tuple[float, float] | None = None,
        subparams: AnnotateParameters = AnnotateParameters(),
    ) -> None:
        """
        Annotate a point on the subplot with text.

        Parameters
        ----------
        text
            The annotation string.
        xy
            The (x, y) point to annotate.
        index
            Subplot index.
        xytext
            If set, (x, y) where the text is drawn.
        subparams
            Coordinate systems, arrow properties, clipping, and text styling.
        """
        subplot = self.access_subplot(index=index)
        subplot.annotate(text, xy, xytext=xytext, **subparams.to_dict)

    def bar(
        self: MakerCanvas,
        x: np.ndarray,
        index: SubplotIndex,
        subparams: BarParameters = BarParameters(),
    ) -> None:
        """
        Draw a bar plot on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the bars.
        index: SubplotIndex
            The index of the subplot.
        subparams: BarParameters
            The subparameters for the bar plot.
        """
        subplot = self.access_subplot(index=index)
        subplot.bar(x, **subparams.to_dict)

    def imscatter(self: MakerCanvas) -> None:
        raise NotImplementedError("Not implemented yet.")

    def hist(self: MakerCanvas) -> None:
        raise NotImplementedError("Not implemented yet.")