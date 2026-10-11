from dataclasses import dataclass

from .....utils import Linestyle


@dataclass(frozen=True)
class LineStyleParameters:
    """
    Common line-like kwargs shared by line and plot style artists.
    """

    linewidth: float | None = None
    linestyle: Linestyle | None = None
    antialiased: bool | None = None

    def __post_init__(self) -> None:
        if self.linewidth is not None and self.linewidth <= 0:
            raise ValueError("linewidth must be positive")
        post_init = getattr(super(), "__post_init__", None)
        if callable(post_init):
            _ = post_init()
