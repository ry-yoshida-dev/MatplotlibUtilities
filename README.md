# MatplotlibUtilities

## Overview

MatplotlibUtilities (`matplotlib_utilities`) is a small Python library that wraps common Matplotlib workflows: subplot layout, typed “subparameter” dataclasses for plot kwargs, and a `MatplotGraphMaker` facade for line, bar, pie, distribution (histogram, box, violin, hexbin), contour, mesh, vector-field and image plots, plus colorbars, legends, and annotations. See [mixin/draw/README.md](src/matplotlib_utilities/mixin/draw/README.md) for every chart type with an example figure.

For package structure and modules, see [src/matplotlib_utilities/README.md](src/matplotlib_utilities/README.md).

## Installation

Install runtime dependencies from the repository root:

```bash
pip install -r requirements.txt
```

The test suite expects the package on the path (see `pythonpath` in `pyproject.toml`). From the repo root you can run:

```bash
pytest
```

You can also install the package in editable mode with `pip install -e .` from the repository root (see `pyproject.toml`).

The source passes `mypy --strict` and basedpyright with no warnings; both are configured in `pyproject.toml`:

```bash
pip install -e ".[dev]"
mypy
basedpyright
```

## Quick example

A single plot needs no layout and no index; every method draws on the first subplot by default:

```python
import numpy as np
from matplotlib_utilities import GraphAxis, MatplotGraphMaker

x = np.linspace(0, 1, 50)
maker = MatplotGraphMaker()
maker.plot(x=x, y=np.sin(x * 10))
maker.set_label(label="x", axis=GraphAxis.X)
maker.finalize(save_path="sin.png")
```

With several subplots, pass the subplot number (row-major, from 0) as `index`:

```python
import numpy as np
from matplotlib_utilities import (
    ColorMap,
    GraphLayout,
    GraphParameters,
    LegendParameters,
    MatplotGraphMaker,
    ScatterParameters,
)

x = np.linspace(0, 1, 50)
maker = MatplotGraphMaker(
    layout=GraphLayout.from_row_column(row=1, column=2),
    parameters=GraphParameters(figsize=(8, 3)),
)
maker.plot(x=x, y=np.sin(x * 10), index=0)
maker.scatter(
    x=x,
    y=np.sin(x * 10),
    index=1,
    subparams=ScatterParameters(c=np.cos(x * 10), cmap=ColorMap.VIRIDIS, label="sin"),
)
maker.legend(index=1, subparams=LegendParameters(edgecolor="black"))
maker.finalize()
```

`finalize` hides grid cells that hold no subplot, saves the figure when `save_path` is given, shows it, and closes it.

## Japanese labels

Matplotlib ships no font holding Japanese glyphs, so Japanese text is drawn as tofu boxes
unless a font that holds them is registered first. Select `FontFamily.JAPANESE` and a bundled
font is registered for you:

```python
from matplotlib_utilities import FontFamily, GraphParameters, MatplotGraphMaker

maker = MatplotGraphMaker(parameters=GraphParameters(font_family=FontFamily.JAPANESE))
```

The font family and size are set on the global rcParams while the maker is in use, and `finalize` restores the previous values.

## Horizontal bars

`barh` draws bars along the x axis, which suits categories whose names are too long to fit
under a vertical bar. Pair it with `set_ticks` to label them and `invert` to read top to
bottom:

```python
import numpy as np
from matplotlib_utilities import BarhParameters, GraphAxis

positions = np.arange(3)
maker.barh(
    y=positions,
    width=np.array([1832.3, 84.4, 19.9]),
    subparams=BarhParameters(height=0.45, facecolor="#2a78d6"),
)
maker.set_ticks(
    positions=list(positions),
    axis=GraphAxis.Y,
    labels=["市区町村道", "主要地方道・都道府県道", "一般国道"],
)
maker.invert(axis=GraphAxis.Y)
```

## Notes

- `requirements.txt` includes a Git dependency for `color`, whose palette types are re-exported from `utils`. Color fields in parameters take `MplColor`, which is Matplotlib's `ColorType`: a name, a hex string, or an RGB(A) tuple of floats in 0–1.
- Subplot indexing types live under [`src/matplotlib_utilities/utils/index/`](src/matplotlib_utilities/utils/index/README.md); `SubplotIndex` is also exported from the `matplotlib_utilities` package root.
