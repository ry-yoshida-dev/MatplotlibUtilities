from dataclasses import dataclass


@dataclass(frozen=True)
class ArtistParameters:
    """
    Common artist kwargs shared by many matplotlib draw calls.
    """

    alpha: float | None = None
    zorder: float | None = None

    def __post_init__(self) -> None:
        if self.alpha is not None and not (0.0 <= self.alpha <= 1.0):
            raise ValueError("alpha must be between 0 and 1")
        if self.zorder is not None and self.zorder < 0:
            raise ValueError("zorder must be non-negative")
        post_init = getattr(super(), "__post_init__", None)
        if callable(post_init):
            _ = post_init()
