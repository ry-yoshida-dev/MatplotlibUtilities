# pyright: reportUnknownMemberType=false

from __future__ import annotations

from .mixins import (
    ImageDrawMixin,
    SeriesDrawMixin,
    VectorDrawMixin,
)
from .parameters import (
    AnnotateParameters,
    LegendParameters,
    LineParameters,
    Orientation,
)
from ...protocols import MakerCanvas
from ...utils import SubplotIndex


class DrawMixin(ImageDrawMixin, SeriesDrawMixin, VectorDrawMixin):
    """
    Drawing API on the graph maker (for example maker.scatter(...)).

    Concrete classes are expected to expose fig, ax, and
    access_subplot, which this mixin uses to dispatch drawing calls
    (see matplotlib_utilities.protocols.MakerCanvas).
    """

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

    def imscatter(self: MakerCanvas) -> None:
        raise NotImplementedError("Not implemented yet.")

    def hist(self: MakerCanvas) -> None:
        raise NotImplementedError("Not implemented yet.")
