# MatplotlibUtilities

## Overview

MatplotlibUtilities (`matplotlib_utilities`) is a small Python library that wraps common Matplotlib workflows: subplot layout, typed “subparameter” dataclasses for plot kwargs, and a `MatplotGraphMaker` facade for scatter, plot, imshow, colorbars, legends, and annotations.

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

## Quick example

```python
import numpy as np
from matplotlib_utilities import (
    GraphLayout, 
    GraphParameters, 
    MatplotGraphMaker,
    PlotParameters,
    ScatterParameters,
    LegendParameters,
    GraphAxis,
)

layout = GraphLayout.from_row_column(row=1, column=2)
legend_params = LegendParameters(edgecolor="black")
graph_params = GraphParameters(figsize=(8, 1.5))
maker = MatplotGraphMaker(layout=layout, parameters=graph_params)

x = np.linspace(0, 1, 50)
y = np.sin(x * 10)
z = np.cos(x * 10)

idx0 = maker.get_subplot_index_from_number(number=0)
idx1 = maker.get_subplot_index_from_number(number=1)
maker.plot(index=idx0, x=x, y=y, subparams=PlotParameters())
maker.scatter(index=idx1, x=x, y=y, subparams=ScatterParameters(c=z, cmap="viridis", label="sin"))
maker.set_label(label="x", index=idx0, axis=GraphAxis.X)
maker.set_label(label="y", index=idx0, axis=GraphAxis.Y)
maker.legend(index=idx1, subparams=legend_params)
maker.finalize(is_showing_result_enabled=True)
```

## Japanese labels

Matplotlib ships no font holding Japanese glyphs, so Japanese text is drawn as tofu boxes
unless a font that holds them is registered first. Select `FontFamily.JAPANESE` and a bundled
font is registered for you:

```python
from matplotlib_utilities import FontFamily, GraphParameters, MatplotGraphMaker

maker = MatplotGraphMaker(parameters=GraphParameters(font_family=FontFamily.JAPANESE))
```

The family is set on the global rcParams, so it applies to every figure drawn afterwards.

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
    index=index,
    subparams=BarhParameters(height=0.45, facecolor="#2a78d6"),
)
maker.set_ticks(
    positions=list(positions),
    index=index,
    axis=GraphAxis.Y,
    labels=["市区町村道", "主要地方道・都道府県道", "一般国道"],
)
maker.invert(index=index, axis=GraphAxis.Y)
```

## Notes

- `requirements.txt` includes a Git dependency for `color` (used with typed color arguments in subparameters).
- Subplot indexing types live under [`src/matplotlib_utilities/utils/index/`](src/matplotlib_utilities/utils/index/README.md); `SubplotIndex` is also exported from the `matplotlib_utilities` package root.
