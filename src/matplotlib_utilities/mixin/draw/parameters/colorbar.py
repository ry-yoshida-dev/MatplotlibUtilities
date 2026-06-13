from dataclasses import dataclass, Field
from typing import Any, Protocol, Sequence

from matplotlib.axes import Axes
from matplotlib import colormaps
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.ticker import Formatter
from matplotlib.ticker import Locator

from ....subparameter import Subparameters
from ....types import NumericArray
from ....utils import ColorbarExtend, ColorbarSpacing, Location, Orientation
from .base import ArtistParameters, CmapParameters, LabelParameters


class _AxesDivider(Protocol):
    """Structural type for :class:`mpl_toolkits.axes_grid1.axes_divider.AxesDivider`."""

    def append_axes(
        self,
        position: str,
        size: str,
        pad: float | None = None,
        *,
        axes_class: type[Axes] | None = None,
        **kwargs: Any,
    ) -> Axes: ...


@dataclass
class ColorbarParameters(
    CmapParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Parameters for the colorbar.

    Attributes:
    ----------
    # own
    location: Location | None = None
        The location, relative to the parent Axes, where the colorbar Axes is created.
        It also determines the orientation of the colorbar.
    orientation: Orientation | None = None
        The orientation of the colorbar. It is preferable to set the location
        of the colorbar, as that also determines the orientation.
    fraction: float = 0.15
        Fraction of original Axes to use for colorbar.
    shrink: float = 1.0
        Fraction by which to multiply the size of the colorbar.
    aspect: float = 20
        Ratio of long to short dimensions.
    pad: float | None = None
        Fraction of original Axes between colorbar and new image Axes.
        Defaults to 0.05 if vertical, 0.15 if horizontal.
    anchor: tuple[float, float] | None = None
        The anchor point of the colorbar Axes.
        Defaults to (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal.
    panchor: tuple[float, float] | bool | None = None
        The anchor point of the colorbar parent Axes.
        If False, the parent axes anchor is unchanged.
        Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.
    extend: ColorbarExtend = ColorbarExtend.NEITHER
        Make pointed end(s) for out-of-range values.
    extendfrac: None | str | float | tuple[float, float] = None
        Length of triangular colorbar extensions as a fraction of the interior colorbar length.
        If auto, makes extensions the same lengths as interior boxes.
    extendrect: bool = False
        If False the extensions are triangular.
        If True the extensions are rectangular.
    ticks: None | list | Locator = None
        If None, ticks are determined automatically from the input.
    format: None | str | Formatter = None
        If None, ScalarFormatter is used. Format strings are supported.
    drawedges: bool = False
        Whether to draw lines at color boundaries.
    boundaries: None | Sequence = None
        If unset, the colormap is displayed on a 0-1 scale.
    values: None | Sequence = None
        Must have a length 1 less than boundaries if boundaries is set.
    spacing: ColorbarSpacing | None = None
        For discrete colorbars, uniform gives each color the same space;
        proportional makes the space proportional to the data interval.
    # inherited from CmapParameters
    cmap: str | None
        The colormap name used for mapping normalized values to colors.
    vmin: float | None
        The minimum data value represented by the color scale.
    vmax: float | None
        The maximum data value represented by the color scale.
    # inherited from LabelParameters
    label: str | None
        The label string for axis, legend, and other uses.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha of the colorbar.
    zorder: float | None
        The drawing order.
    """

    location: Location | None = None
    orientation: Orientation | None = None
    fraction: float = 0.15
    shrink: float = 1.0
    aspect: float = 20.0
    pad: float | None = None
    anchor: tuple[float, float] | None = None
    panchor: tuple[float, float] | bool | None = None
    extend: ColorbarExtend = ColorbarExtend.NEITHER
    extendfrac: None | str | float | tuple[float, float] = None
    extendrect: bool = False
    ticks: None | list[float] | Locator = None
    format: None | str | Formatter = None
    drawedges: bool = False
    boundaries: None | Sequence[float] = None
    values: None | Sequence[float] = None
    spacing: ColorbarSpacing | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.fraction <= 0 or self.fraction > 1:
            raise ValueError("fraction must be between 0 and 1")
        if self.shrink <= 0 or self.shrink > 1:
            raise ValueError("shrink must be between 0 and 1")
        if self.aspect <= 0:
            raise ValueError("aspect must be greater than 0")
        if self.pad is not None and (self.pad <= 0 or self.pad > 1):
            raise ValueError("pad must be between 0 and 1")
        if self.anchor is not None and len(self.anchor) != 2:
            raise ValueError("anchor must be a tuple of 2 floats")
        if self.panchor is not None and isinstance(self.panchor, tuple) and len(self.panchor) != 2:
            raise ValueError("panchor must be a tuple of 2 floats")
        if self.extend not in [ColorbarExtend.NEITHER, ColorbarExtend.BOTH, ColorbarExtend.MIN, ColorbarExtend.MAX]:
            raise ValueError("extend must be ColorbarExtend enum")
        if self.extendfrac is not None and isinstance(self.extendfrac, tuple) and len(self.extendfrac) != 2:
            raise ValueError("extendfrac tuple must have 2 elements")
        if self.extendrect and self.extend == ColorbarExtend.NEITHER:
            raise ValueError("extendrect can only be True if extend is not NEITHER")
        if self.drawedges and self.boundaries is None:
            raise ValueError("drawedges can only be True if boundaries is set")
        if self.boundaries is not None and self.values is not None and len(self.boundaries) != len(self.values) + 1:
            raise ValueError("boundaries must have a length 1 greater than values")

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
        if self.cmap is None:
            self.cmap = "viridis"
        cmap_obj = colormaps[self.cmap]
        norm = Normalize(vmin=vmin, vmax=vmax)
        sm = ScalarMappable(norm=norm, cmap=cmap_obj)
        sm.set_array([])
        return sm

    def create_cax(self, divider: _AxesDivider) -> Axes:
        """
        Append colorbar axes to divider and return the new Axes.
        """
        location = self.location.value if self.location is not None else Location.RIGHT.value
        pad = 0.05 if self.pad is None else self.pad
        return divider.append_axes(location, f"{self.fraction * 100}%", pad)

    def _to_dict_skip_field(self, field: Field[Any], value: Any) -> bool:
        return value == field.default
