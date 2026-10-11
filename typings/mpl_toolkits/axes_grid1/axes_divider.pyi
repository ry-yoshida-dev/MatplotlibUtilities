from matplotlib.axes import Axes

class AxesDivider:
    def append_axes(
        self,
        position: str,
        size: float | str,
        pad: float | str | None = None,
        *,
        axes_class: type[Axes] | None = None,
    ) -> Axes: ...
