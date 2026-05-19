from typing import Any

from matplotlib.axes import Axes

class AxesDivider:
    def append_axes(
        self,
        position: str,
        size: str,
        pad: float | None = None,
        *,
        axes_class: type[Axes] | None = None,
        **kwargs: Any,
    ) -> Axes: ...
