from dataclasses import dataclass, field

from .font_family import FontFamily

@dataclass
class GraphParameters:
    """
    Parameters for the Matplotlib utilities.

    Attributes:
    ----------
    font_size: int
        The size of the font.
    font_family: FontFamily
        The font family. Select JAPANESE to draw Japanese labels.
    point_size: int
        The size of the points.
    w_space: float
        The width of the space between the subplots.
    h_space: float
        The height of the space between the subplots.
    dpi: int
        The resolution of the image.
    figsize: tuple[float, float]
        The size of the figure.
    aspect_ratio: float
        The aspect ratio(height/width) of the figure.
    max_image_size: tuple[int, int]
        The maximum size of the image with shape(width, height).
    """
    font_size: float = 10.0
    font_family: FontFamily = FontFamily.DEFAULT
    point_size: float = 5.0
    w_space: float = 0.2
    h_space: float = 0.2
    dpi: int = 250
    figsize: tuple[float, float] = field(default_factory=lambda:(5.0, 3.0))
    aspect_ratio: float = 2.0 # height/width
    max_image_size: tuple[int, int] = (64, 128)

    def __post_init__(self):
        if self.font_size < 0:
            raise ValueError("font_size must be greater than 0")
        if self.point_size < 0:
            raise ValueError("point_size must be greater than 0")
        if self.w_space < 0:
            raise ValueError("w_space must be greater than 0")
        if self.h_space < 0:
            raise ValueError("h_space must be greater than 0")
        if self.dpi < 0:
            raise ValueError("dpi must be greater than 0")
        if self.figsize[0] <= 0 or self.figsize[1] <= 0:
            raise ValueError("figsize must be greater than 0")
        if self.aspect_ratio <= 0:
            raise ValueError("aspect_ratio must be greater than 0")
        if self.max_image_size[0] <= 0 or self.max_image_size[1] <= 0:
            raise ValueError("max_image_size must be greater than 0")

