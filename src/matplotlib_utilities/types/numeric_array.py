"""Type alias for numeric NumPy arrays used in plot data."""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

type NumericArray = NDArray[np.integer[Any] | np.floating[Any]]
