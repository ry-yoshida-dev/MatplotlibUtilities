# mixins

## Overview

Draw mixins composed by [`DrawMixin`](../mixin.py), grouped by plot family. Draw calls that produce a colormapped artist return it so it can be passed to `set_colorbar`.

## Components

| Path | Description |
| ---- | ----------- |
| [`argument_validator.py`](./argument_validator.py) | `ArgumentValidator` — shared length and presence checks on data arguments |
| [`distribution.py`](./distribution.py) | `DistributionDrawMixin` — hist, boxplot, violinplot, hexbin, hist2d |
| [`image.py`](./image.py) | `ImageDrawMixin` — imshow, set_colorbar, contour, contourf, pcolormesh, imscatter |
| [`proportion.py`](./proportion.py) | `ProportionDrawMixin` — pie |
| [`series.py`](./series.py) | `SeriesDrawMixin` — plot, scatter, bar, barh, step, errorbar, fill_between, stackplot |
| [`vector.py`](./vector.py) | `VectorDrawMixin` — arrow, quiver, streamplot |
