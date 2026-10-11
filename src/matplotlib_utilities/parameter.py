from dataclasses import dataclass, field

from .font_family import FontFamily

@dataclass(frozen=True)
class GraphParameters:
    """
    Parameters for the Matplotlib utilities.

    Attributes:
    ----------
    font_size: float
        The size of the font.
    font_family: FontFamily
        The font family. Select JAPANESE to draw Japanese labels.
    w_space: float
        The width of the space between the subplots.
    h_space: float
        The height of the space between the subplots.
    dpi: int
        The resolution of the image.
    figsize: tuple[float, float]
        The size of the figure.
    """
    font_size: float = 10.0
    font_family: FontFamily = FontFamily.DEFAULT
    w_space: float = 0.2
    h_space: float = 0.2
    dpi: int = 250
    figsize: tuple[float, float] = field(default_factory=lambda:(5.0, 3.0))

    def __post_init__(self) -> None:
        if self.font_size <= 0:
            raise ValueError(f"font_size must be greater than 0, got {self.font_size}")
        if self.w_space < 0:
            raise ValueError(f"w_space must be non-negative, got {self.w_space}")
        if self.h_space < 0:
            raise ValueError(f"h_space must be non-negative, got {self.h_space}")
        if self.dpi <= 0:
            raise ValueError(f"dpi must be greater than 0, got {self.dpi}")
        if self.figsize[0] <= 0 or self.figsize[1] <= 0:
            raise ValueError(f"figsize must be greater than 0, got {self.figsize}")
