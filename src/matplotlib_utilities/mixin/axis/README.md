# axis

## Overview

`AxisMixin`, the axis methods of `MatplotGraphMaker`: labels, limits, ticks, axis direction, titles and grids.

## Components

| Component | Description |
| --------- | ----------- |
| [`mixin.py`](./mixin.py) | `AxisMixin` |
| [`parameters/`](./parameters/README.md) | Parameter dataclasses of `set_grid` and tick styling |
| [`keyword_arguments/`](./keyword_arguments/README.md) | TypedDicts the parameters' `to_dict` returns |
| [`readme_figures/`](./readme_figures) | An example figure of every axis method, checked by `tests/test_readme_axis_figures.py` |

## Examples

```python
from matplotlib_utilities import GraphAxis, MatplotGraphMaker

maker = MatplotGraphMaker()
maker.plot(x=x, y=y)
maker.set_label(label="time [s]", axis=GraphAxis.X)
maker.set_lim(lower=0.0, upper=1.0, axis=GraphAxis.Y)
maker.set_title(title="Response")
maker.finalize()
```

One figure per axis method, generated from [`readme_figures/`](./readme_figures):

<img src="readme_figures/delete_axis_label.png" width="160" alt="delete_axis_label" title="delete_axis_label"/> <img src="readme_figures/invert.png" width="160" alt="invert" title="invert"/> <img src="readme_figures/set_grid.png" width="160" alt="set_grid" title="set_grid"/> <img src="readme_figures/set_label.png" width="160" alt="set_label" title="set_label"/> <img src="readme_figures/set_lim.png" width="160" alt="set_lim" title="set_lim"/> <img src="readme_figures/set_ticks.png" width="160" alt="set_ticks" title="set_ticks"/> <img src="readme_figures/set_title.png" width="160" alt="set_title" title="set_title"/>
