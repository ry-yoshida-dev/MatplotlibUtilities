# draw

## Overview

`DrawMixin`, the drawing methods of `MatplotGraphMaker`. Each takes its options as a frozen `*Parameters` dataclass whose `to_dict` returns a TypedDict, so type checkers check every keyword argument against the Matplotlib `Axes` method it is unpacked into.

## Components

| Component | Description |
| --------- | ----------- |
| [`mixin.py`](./mixin.py) | `DrawMixin`, which composes the family mixins and adds `legend`, `line`, `annotate` and `span` |
| [`mixins/`](./mixins/README.md) | Drawing methods grouped by plot family |
| [`parameters/`](./parameters/README.md) | Parameter dataclasses of the drawing methods |
| [`keyword_arguments/`](./keyword_arguments/README.md) | TypedDicts the parameters' `to_dict` returns |
| [`readme_figures/`](./readme_figures) | An example figure of every drawing method, checked by `tests/test_readme_figures.py` |

## Examples

```python
from matplotlib_utilities import ColorMap, ImshowParameters, MatplotGraphMaker

maker = MatplotGraphMaker()
image = maker.imshow(image=values, subparams=ImshowParameters(cmap=ColorMap.VIRIDIS))
maker.set_colorbar(mappable=image)
maker.finalize()
```

One figure per drawing method, generated from [`readme_figures/`](./readme_figures):

| Family | Figures |
| ------ | ------- |
| distribution | <img src="readme_figures/distribution/boxplot.png" width="160" alt="boxplot" title="boxplot"/> <img src="readme_figures/distribution/hexbin.png" width="160" alt="hexbin" title="hexbin"/> <img src="readme_figures/distribution/hist.png" width="160" alt="hist" title="hist"/> <img src="readme_figures/distribution/hist2d.png" width="160" alt="hist2d" title="hist2d"/> <img src="readme_figures/distribution/violinplot.png" width="160" alt="violinplot" title="violinplot"/> |
| image | <img src="readme_figures/image/colorbar.png" width="160" alt="colorbar" title="colorbar"/> <img src="readme_figures/image/contour.png" width="160" alt="contour" title="contour"/> <img src="readme_figures/image/contourf.png" width="160" alt="contourf" title="contourf"/> <img src="readme_figures/image/imscatter.png" width="160" alt="imscatter" title="imscatter"/> <img src="readme_figures/image/imshow.png" width="160" alt="imshow" title="imshow"/> <img src="readme_figures/image/pcolormesh.png" width="160" alt="pcolormesh" title="pcolormesh"/> |
| misc | <img src="readme_figures/misc/annotate.png" width="160" alt="annotate" title="annotate"/> <img src="readme_figures/misc/legend.png" width="160" alt="legend" title="legend"/> <img src="readme_figures/misc/line.png" width="160" alt="line" title="line"/> <img src="readme_figures/misc/span.png" width="160" alt="span" title="span"/> |
| proportion | <img src="readme_figures/proportion/pie.png" width="160" alt="pie" title="pie"/> |
| series | <img src="readme_figures/series/bar.png" width="160" alt="bar" title="bar"/> <img src="readme_figures/series/barh.png" width="160" alt="barh" title="barh"/> <img src="readme_figures/series/errorbar.png" width="160" alt="errorbar" title="errorbar"/> <img src="readme_figures/series/fill_between.png" width="160" alt="fill_between" title="fill_between"/> <img src="readme_figures/series/plot.png" width="160" alt="plot" title="plot"/> <img src="readme_figures/series/scatter.png" width="160" alt="scatter" title="scatter"/> <img src="readme_figures/series/stackplot.png" width="160" alt="stackplot" title="stackplot"/> <img src="readme_figures/series/step.png" width="160" alt="step" title="step"/> |
| vector | <img src="readme_figures/vector/arrow.png" width="160" alt="arrow" title="arrow"/> <img src="readme_figures/vector/quiver.png" width="160" alt="quiver" title="quiver"/> <img src="readme_figures/vector/streamplot.png" width="160" alt="streamplot" title="streamplot"/> |
