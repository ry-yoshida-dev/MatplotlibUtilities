# pyright: reportUnknownMemberType=false

from __future__ import annotations

from .mixins import (
    DistributionDrawMixin,
    ImageDrawMixin,
    ProportionDrawMixin,
    SeriesDrawMixin,
    VectorDrawMixin,
)
from .parameters import (
    AnnotateParameters,
    LegendParameters,
    LineParameters,
    Orientation,
    SpanParameters,
)
from ...protocols import MakerCanvas
from ...utils import SubplotIndex


class DrawMixin(
    DistributionDrawMixin,
    ImageDrawMixin,
    ProportionDrawMixin,
    SeriesDrawMixin,
    VectorDrawMixin,
):
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
        _ = subplot.legend(**subparams.to_dict)

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
        match orientation:
            case Orientation.VERTICAL:
                _ = subplot.axvline(x=value, **subparams.to_dict)
            case Orientation.HORIZONTAL:
                _ = subplot.axhline(y=value, **subparams.to_dict)

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
        _ = subplot.annotate(text, xy, xytext=xytext, **subparams.to_dict)

    def span(
        self: MakerCanvas,
        start: float,
        end: float,
        orientation: Orientation,
        index: SubplotIndex,
        subparams: SpanParameters = SpanParameters(),
    ) -> None:
        """
        Shade a band that spans the whole subplot.

        A vertical band covers an x range across the full height, which
        suits marking a period of interest; a horizontal band covers a
        y range across the full width, which suits marking a target range.

        Parameters
        ----------
        start: float
            Where the band begins on the selected axis.
        end: float
            Where the band ends on the selected axis.
        orientation: Orientation
            VERTICAL shades an x range; HORIZONTAL shades a y range.
        index: SubplotIndex
            The index of the subplot.
        subparams: SpanParameters
            The subparameters for the band.

        Raises
        ------
        ValueError
            If start is not less than end.
        """
        if start >= end:
            raise ValueError(f"start must be less than end, given {start} and {end}")
        subplot = self.access_subplot(index=index)
        match orientation:
            case Orientation.VERTICAL:
                _ = subplot.axvspan(start, end, **subparams.to_dict)
            case Orientation.HORIZONTAL:
                _ = subplot.axhspan(start, end, **subparams.to_dict)
