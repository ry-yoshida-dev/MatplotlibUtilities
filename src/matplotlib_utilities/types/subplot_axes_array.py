"""Type alias for the 2D NumPy grid of Matplotlib Axes from ``subplots(squeeze=False)``."""

from __future__ import annotations

from typing import Any

from numpy.typing import NDArray

type SubplotAxesArray = NDArray[Any]
