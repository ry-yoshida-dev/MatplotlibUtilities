from collections.abc import Sequence
from dataclasses import dataclass

from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.ticker import Formatter, Locator
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider

from ....subparameter import Subparameters
from ....types import NumericArray
from ....utils import ColorbarExtend, ColorbarSpacing, ColorMap, Location
from ..keyword_arguments import ColorbarKeywordArguments
from .base import ArtistParameters, CmapParameters, LabelParameters


@dataclass(frozen=True)
class ColorbarParameters(
    CmapParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Parameters for the colorbar.

    The colorbar is drawn in a new Axes appended next to the subplot, so its
    size is set by fraction and pad rather than by Matplotlib's shrink or
    aspect options.

    Attributes:
    ----------
    # own
    location: Location | None = None
        The side of the subplot where the colorbar Axes is created. It also
        determines the orientation of the colorbar. Defaults to the right.
    fraction: float = 0.15
        The size of the colorbar Axes as a fraction of the subplot.
    pad: float | None = None
        The gap between the subplot and the colorbar, in inches.
        Defaults to 0.05.
    extend: ColorbarExtend = ColorbarExtend.NEITHER
        Make pointed end(s) for out-of-range values.
    extendfrac: float | tuple[float, float] | None = None
        Length of triangular colorbar extensions as a fraction of the interior colorbar length.
    extendrect: bool = False
        If False the extensions are triangular.
        If True the extensions are rectangular.
    ticks: Sequence[float] | Locator | None = None
        If None, ticks are determined automatically from the input.
    format: str | Formatter | None = None
        If None, ScalarFormatter is used. Format strings are supported.
    drawedges: bool = False
        Whether to draw lines at color boundaries.
    boundaries: Sequence[float] | None = None
        If unset, the colormap is displayed on a 0-1 scale.
    values: Sequence[float] | None = None
        Must have a length 1 less than boundaries if boundaries is set.
    spacing: ColorbarSpacing | None = None
        For discrete colorbars, uniform gives each color the same space;
        proportional makes the space proportional to the data interval.
    # inherited from CmapParameters
    cmap: ColorMap | None
        The colormap of a colorbar built from image data. It must stay unset
        when the colorbar describes an existing mappable.
    vmin: float | None
        The minimum data value of a colorbar built from image data.
    vmax: float | None
        The maximum data value of a colorbar built from image data.
    # inherited from LabelParameters
    label: str | None
        The label of the colorbar's long axis.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha of the colorbar.
    zorder: float | None
        The drawing order of the colorbar Axes.
    """

    location: Location | None = None
    fraction: float = 0.15
    pad: float | None = None
    extend: ColorbarExtend = ColorbarExtend.NEITHER
    extendfrac: float | tuple[float, float] | None = None
    extendrect: bool = False
    ticks: Sequence[float] | Locator | None = None
    format: str | Formatter | None = None
    drawedges: bool = False
    boundaries: Sequence[float] | None = None
    values: Sequence[float] | None = None
    spacing: ColorbarSpacing | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.fraction <= 0 or self.fraction > 1:
            raise ValueError("fraction must be between 0 and 1")
        if self.pad is not None and (self.pad <= 0 or self.pad > 1):
            raise ValueError("pad must be between 0 and 1")
        if self.extendfrac is not None and isinstance(self.extendfrac, tuple) and len(self.extendfrac) != 2:
            raise ValueError("extendfrac tuple must have 2 elements")
        if self.extendrect and self.extend == ColorbarExtend.NEITHER:
            raise ValueError("extendrect can only be True if extend is not NEITHER")
        if self.boundaries is not None and self.values is not None and len(self.boundaries) != len(self.values) + 1:
            raise ValueError("boundaries must have a length 1 greater than values")

    @property
    def is_scale_set(self) -> bool:
        """
        Whether cmap, vmin or vmax is set, which only applies to a colorbar built from image data.
        """
        return self.cmap is not None or self.vmin is not None or self.vmax is not None

    @property
    def colorbar_keyword_arguments(self) -> ColorbarKeywordArguments:
        """
        Return the fields that Figure.colorbar accepts as keyword arguments.

        Returns
        -------
        ColorbarKeywordArguments
            The keyword arguments, without the fields left as None.
        """
        location = Location.RIGHT if self.location is None else self.location
        keyword_arguments = ColorbarKeywordArguments(
            location=location.value,
            extend=self.extend.value,
            extendrect=self.extendrect,
            drawedges=self.drawedges,
        )
        if self.extendfrac is not None:
            keyword_arguments["extendfrac"] = self.extendfrac
        if self.ticks is not None:
            keyword_arguments["ticks"] = self.ticks
        if self.format is not None:
            keyword_arguments["format"] = self.format
        if self.boundaries is not None:
            keyword_arguments["boundaries"] = self.boundaries
        if self.values is not None:
            keyword_arguments["values"] = self.values
        if self.spacing is not None:
            keyword_arguments["spacing"] = self.spacing.value
        if self.label is not None:
            keyword_arguments["label"] = self.label
        if self.alpha is not None:
            keyword_arguments["alpha"] = self.alpha
        return keyword_arguments

    def _get_vmin_vmax(self, image: NumericArray | None) -> tuple[float, float]:
        """
        Get vmin and vmax values, using image data if not specified.
        """
        vmin = self.vmin
        vmax = self.vmax
        if image is not None:
            if vmin is None:
                vmin = float(image.min())
            if vmax is None:
                vmax = float(image.max())
        if vmin is None or vmax is None:
            raise ValueError("Either image must be provided, or both vmin and vmax must be specified.")
        return vmin, vmax

    def create_scalar_mappable(self, image: NumericArray | None = None) -> ScalarMappable:
        """
        Create a ScalarMappable for the colorbar without displaying the image.
        """
        vmin, vmax = self._get_vmin_vmax(image)
        colormap = ColorMap.VIRIDIS if self.cmap is None else self.cmap
        norm = Normalize(vmin=vmin, vmax=vmax)
        scalar_mappable = ScalarMappable(norm=norm, cmap=colormap.colormap_object)
        scalar_mappable.set_array([])
        return scalar_mappable

    def create_cax(self, divider: AxesDivider) -> Axes:
        """
        Append colorbar axes to divider and return the new Axes.
        """
        location = Location.RIGHT if self.location is None else self.location
        pad = 0.05 if self.pad is None else self.pad
        cax = divider.append_axes(location.value, f"{self.fraction * 100}%", pad)
        if self.zorder is not None:
            cax.set_zorder(self.zorder)
        return cax
